from aip import AipNlp


class NLP():
    def __init__(self):
        """ 你的 APPID AK SK """
        APP_ID = '16043979'
        API_KEY = 'vr2XhyMVrjW7dWZOZjqeLsae'
        SECRET_KEY = 'RypiqTeFnVIED0zpKOxRIZHbc5a8a2wE'

        self.client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

    def lexical_analysis(self):
        '''词法分析接口向用户提供分词、词性标注、专名识别三大功能；
        能够识别出文本串中的基本词汇（分词），对这些词汇进行重组、标注组合后词汇的词性，
        并进一步识别出命名实体'''
        text = "百度是一家高科技公司"

        """ 调用词法分析 """
        resp = self.client.lexer(text)
        print('调用词法分析:%s'%resp)

    def Interdependent(self):
        '''依存句法分析
        依存句法分析接口可自动分析文本中的依存句法结构信息，
        利用句子中词与词之间的依存关系来表示词语的句法结构信息（如“主谓”、“动宾”、“定中”等结构关系），
        并用树状结构来表示整句的结构（如“主谓宾”、“定状补”等）。'''
        text = '我会唱小情歌'
        resp = self.client.depParser(text)
        print('依存句法分析,主谓宾:%s'%resp)

    def vector(self):
        '''词向量分析
        词向量表示接口提供中文词向量的查询功能。'''
        word = '张飞'
        resp = self.client.wordEmbedding(word)
        print(resp)

    def Dnn(self):
        '''中文DNN语言模型接口用于输出切词结果并给出每个词在句子中的概率值,判断一句话是否符合语言表达习惯。'''
        # word = '你饭吃在哪？'
        word = '你今天上班了吗'
        resp = self.client.dnnlm(word)
        # ppl	float	描述句子通顺的值：数值越低，句子越通顺
        print(resp)
        print('描述句子通顺的值:%s'%resp['ppl'])

    def compare(self):
        # 需要字数相等
        '''词义相似度'''
        word1 = '茶壶'
        word2 = '水瓶'
        resp = self.client.wordSimEmbedding(word1, word2)
        print(resp)
        # score 相似度分数，分数越接近1越相似
        print(resp['score'])

    def text_compare(self):
        # 短文本相似度
        text1 = "穿衣裳"

        text2 = "穿衣服"

        """ 调用短文本相似度 """
        resp = self.client.simnet(text1, text2)
        print(resp)

    def comment(self):
        '''评论观点抽取'''
        text = '苹果笔记本后盖不好看'
        """ 如果有可选参数 """
        options = {}
        options["type"] = 13

        """ 带参数调用评论观点抽取 """
        resp = self.client.commentTag(text, options)
        print(resp)
        print(resp['items'])

    def emotion(self):
        # 情感分析
        text = '今天天气不错'
        resp = self.client.sentimentClassify(text)
        print(resp)
        print(resp['items'])
        print('积极情绪概率:%s' % resp['items'][0]['positive_prob'])
        print('消极情绪概率:%s' % resp['items'][0]['negative_prob'])

    def Tag(self):
        '''文章标签'''
        # 文章标签服务能够针对网络各类媒体文章进行快速的内容理解，根据输入含有标题的文章，
        # 输出多个内容标签以及对应的置信度，用于个性化推荐、相似文章聚合、文本内容分析等场景。
        title = "iphone手机出现“白苹果”原因及解决办法，用苹果手机的可以看下"

        content = "如果下面的方法还是没有解决你的问题建议来我们门店看下成都市锦江区红星路三段99号银石广场24层01室。"

        """ 调用文章标签 """
        resp = self.client.keyword(title, content)
        print(resp)

    def Ar_classification(self):
        '''文章分类'''
        title = "美男齐聚！吴彦祖冯德伦谢霆锋一起颁奖"

        content = "今晚的金像奖，《特警新人类》主演吴彦祖、冯德伦、谢霆锋、李璨琛一起颁奖，今年是电影上映二十年。一开始只有冯德伦、李璨琛上台，说“他们两个有事来不了”，随后吴彦祖和谢霆锋也从VCR中“走”到了台上，他们现场问大家想不想看《特警新人类3》，气氛热烈。"

        """ 调用文章分类 """
        # 可能一个文章有多个分类
        resp = self.client.topic(title, content)
        print(resp)
        print(resp['item'])

    def modify(self):
        '''文本纠错'''
        text = "只能门锁"

        """ 调用文本纠错 """
        resp = self.client.ecnet(text)
        print(resp)
        print(resp['item'])
        print('文本错误，正确结果：%s' % resp['item']['correct_query'])

    def emotion_qingxu(self):
        text = '今天本来高兴的'
        """ 如果有可选参数 """
        options = {}
        options["scene"] = "default"

        """ 带参数调用对话情绪识别接口 """
        resp = self.client.emotion(text, options)
        print(resp)
        print(resp['items'])
        print(type(resp['items']))
        print('回复：%s' % resp['items'][0]['replies'])

    def News(self):
        '''新闻摘要'''
        # 没有勾选此接口

        content = "麻省理工学院的研究团队为无人机在仓库中使用RFID技术进行库存查找等工作，创造了一种..."

        maxSummaryLen = 300

        """ 调用新闻摘要接口 """
        resp = self.client.newsSummary(content, maxSummaryLen)
        print(resp)

        # """ 如果有可选参数 """
        # options = {}
        # options["title"] = "标题"
        #
        # """ 带参数调用新闻摘要接口 """
        # client.newsSummary(content, maxSummaryLen, options)


nlp_object = NLP()
# nlp_object.lexical_analysis()
# nlp_object.Interdependent()
# nlp_object.vector()
# nlp_object.Dnn()
# nlp_object.compare()
# nlp_object.text_compare()
# nlp_object.comment()
nlp_object.emotion()
# nlp_object.Tag()
# nlp_object.Ar_classification()
# nlp_object.modify()
# nlp_object.emotion_qingxu()
# nlp_object.News()
