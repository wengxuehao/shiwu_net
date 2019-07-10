import os

import time
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from shiwu.settings import BASE_DIR


class Vocie_Compose_View(View):
    def get(self, request):
        '''语音合成'''
        return render(request, 'voice/voice_compose.html')

    def post(self, request):
        content = request.POST.get('content')
        if content:

            by_content = content.encode('utf-8')
            # print(by_content)
            # print(content)
            from aip import AipSpeech

            """ 你的 APPID AK SK """
            APP_ID = '16037805'
            API_KEY = 'blMPEwR70GvrPXZLTQCFc9jC'
            SECRET_KEY = '0xGPAlkmsGLitMC9PoxzbRUFeQarfk5F'

            client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
            result = client.synthesis(by_content, 'zh', 1, {
                'vol': 5,
                'per': 4})
            t = time.time()

            # now_time = lambda: int(round(t * 1000))
            timeStamp = time.time()

            timeArray = time.localtime(timeStamp)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            print(otherStyleTime)
            print(type(otherStyleTime))
            filePath = os.path.join(BASE_DIR, "frontend/dist/static/media/voice" + '/' + otherStyleTime + '.mp3')
            # 语音合成成功，并保存
            # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
            if not isinstance(result, dict):
                with open(filePath, 'wb') as f:
                    f.write(result)
            return HttpResponse('语音合成成功')
        else:
            return HttpResponse('请先输入文字')
