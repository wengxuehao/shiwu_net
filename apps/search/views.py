import os

import time
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
# from image_tag import image_biaozhu
from shiwu.settings import BASE_DIR, APP_ID_BAIDU, API_KEY_BAIDU, SECRET_KEY_BAIDU
from .models import Recognize_model


class Recognize_Category_View(View):
    def get(self, request):
        '''查询识别种类'''
        categories = Recognize_model.objects.all()
        print(categories)
        return HttpResponse('ok')


class Character_recognition(View):
    def get(self, request):

        return render(request, 'search/char_search.html')

    def post(self, request):
        from aip import AipOcr
        pic = request.FILES.get("pic")

        # 将前端提交来的图片保存本地
        # fs = FileSystemStorage()
        # fs.save(pic.name, pic)
        # print(os.path.join(BASE_DIR, "frontend/dist/static/media/test"))
        if pic:
            with open(os.path.join(BASE_DIR, "frontend/dist/static/media/char/%s") % pic.name, 'wb') as f:
                for chunk in pic.chunks():
                    f.write(chunk)
                    # return HttpResponse('保存成功')

            """ 你的 APPID AK SK """

            client = AipOcr(APP_ID_BAIDU, API_KEY_BAIDU, SECRET_KEY_BAIDU)

            """ 读取图片 """

            def get_file_content(filePath):
                with open(filePath, 'rb') as fp:
                    return fp.read()

            image = get_file_content(os.path.join(BASE_DIR, "frontend/dist/static/media/char" + '/' + pic.name))

            """ 调用通用文字识别, 图片参数为本地图片 """
            client.basicGeneral(image)

            """ 如果有可选参数 """
            options = {}
            options["language_type"] = "CHN_ENG"
            options["detect_direction"] = "true"
            options["detect_language"] = "true"
            options["probability"] = "true"

            """ 带参数调用通用文字识别, 图片参数为本地图片 """
            try:
                resp = client.basicGeneral(image, options)
                list = []
                for i in resp['words_result']:
                    word = i['words']
                    list.append(word)
                with open('./test.txt', 'w') as f:
                    for i in list:
                        f.writelines(i + "\n")
                with open('./test.txt', 'r') as f:
                    # print('识别到的内容是：%s' % f.read())
                    content = f.read()
                    new_content = content.replace('\n', '')
                    # print(new_content)
                    data = {
                        "content": new_content
                    }
                return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})
            except Exception as e:
                return HttpResponse('请提交带文字的图片')
        else:
            return HttpResponse('请先提交文字图片')


class Animal_recognition(View):
    def get(self, request):
        # 调用动物识别api
        # 返回识别结果供前端页面显示

        return render(request, 'search/animal_search.html')

    def post(self, request):
        from aip import AipImageClassify
        pic = request.FILES.get("pic")

        # 将前端提交来的图片保存本地
        # fs = FileSystemStorage()
        # fs.save(pic.name, pic)
        # print(os.path.join(BASE_DIR, "frontend/dist/static/media/test"))
        if pic:
            with open(os.path.join(BASE_DIR, "frontend/dist/static/media/animal/%s") % pic.name, 'wb') as f:
                for chunk in pic.chunks():
                    f.write(chunk)
            """ 你的 APPID AK SK """

            client = AipImageClassify(APP_ID_BAIDU, API_KEY_BAIDU, SECRET_KEY_BAIDU)

            """ 读取图片 """

            def get_file_content(filePath):
                with open(filePath, 'rb') as fp:
                    return fp.read()

            filePath = os.path.join(BASE_DIR, "frontend/dist/static/media/animal" + '/' + pic.name)
            # print(filePath)
            image = get_file_content(os.path.join(BASE_DIR, "frontend/dist/static/media/animal" + '/' + pic.name))
            #
            # """ 调用通用物体识别 """
            # resp = client.animalDetect(image)
            # print(resp)

            """ 如果有可选参数 """
            options = {}
            options["top_num"] = 3
            options["baike_num"] = 5
            """ 带参数调用通用动物识别 """
            try:
                resp = client.animalDetect(image, options)
                # print(resp)
                name = resp['result'][0]['name']
                desc = resp['result'][0]['baike_info']['description']
                # print(resp['result'][0]['name'])
                # save_path = image_biaozhu(filePath, name)
                # print(save_path)
                data = {
                    "name": name,
                    "description": desc
                }

                # 返回图片给前端显示

                return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})
            except Exception as e:
                # print(e)
                return HttpResponse('请提交动物图片')
        else:
            return HttpResponse('请先提交动物图片')


class Plant_recognition(View):
    def get(self, request):
        # 调用植物识别api
        # 返回识别结果供前端页面显示

        return render(request, 'search/plant_search.html')

    def post(self, request):
        from aip import AipImageClassify
        pic = request.FILES.get("pic")
        # 将前端提交来的图片保存本地
        # fs = FileSystemStorage()
        # fs.save(pic.name, pic)
        # print(os.path.join(BASE_DIR, "frontend/dist/static/media/test"))
        if pic:
            with open(os.path.join(BASE_DIR, "frontend/dist/static/media/plant/%s") % pic.name, 'wb') as f:
                for chunk in pic.chunks():
                    f.write(chunk)
            """ 你的 APPID AK SK """

            client = AipImageClassify(APP_ID_BAIDU, API_KEY_BAIDU, SECRET_KEY_BAIDU)

            """ 读取图片 """

            def get_file_content(filePath):
                with open(filePath, 'rb') as fp:
                    return fp.read()

            image = get_file_content(os.path.join(BASE_DIR, "frontend/dist/static/media/plant" + '/' + pic.name))
            #
            # """ 调用通用物体识别 """
            # resp = client.animalDetect(image)
            # print(resp)

            """ 如果有可选参数 """
            options = {}
            options["top_num"] = 3
            options["baike_num"] = 5
            """ 带参数调用通用植物识别 """
            try:
                resp = client.plantDetect(image, options)
                data = {
                    "name": resp['result'][0]['name'],
                    "description": resp['result'][0]['baike_info']['description']
                }
                return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})
            except Exception as e:
                return HttpResponse('请提交植物图片')
        else:
            return HttpResponse('请先选择植物图片')


class Vagetable_View(View):
    def get(self, request):
        return render(request, 'search/vagetable_search.html')

    def post(self, request):
        import base64
        import requests

        get_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=AyuLyqu4FNB4klZvGAHSjVaQ&client_secret=MI53Tuf71Xt4KoQiqT7G3lUH96DC3mZ8&'
        url = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/dish'
        resp = requests.post(get_token_url)
        # print(resp.json()['access_token'])
        access_token = resp.json()['access_token']
        request_url = url + "?access_token=" + access_token
        headers = {
            'Content-Type': 'application/x-www-form-urlencode'

        }
        pic = request.FILES.get("pic")
        if pic:
            # 将前端提交来的图片保存本地
            # fs = FileSystemStorage()
            # fs.save(pic.name, pic)
            # print(os.path.join(BASE_DIR, "frontend/dist/static/media/test"))
            with open(os.path.join(BASE_DIR, "frontend/dist/static/media/vagetables/%s") % pic.name, 'wb') as f:
                for chunk in pic.chunks():
                    f.write(chunk)
            file_path = os.path.join(BASE_DIR, "frontend/dist/static/media/vagetables/%s") % pic.name
            # print(file_path)
            f = open(file_path, 'rb')
            content = f.read()

            img = base64.b64encode(content)

            params = {
                'image': img,
                # 'top_num': 5,
                # 'baike_num': 0
            }
            try:
                response = requests.post(request_url, headers=headers, data=params)
                data = response.json()
                return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})
            except Exception as e:
                return HttpResponse('请提交蔬菜图片')
        else:
            return HttpResponse('请提交蔬菜图片')


class Landview(View):
    def get(self, request):
        return render(request, 'search/land_search.html')

    def post(self, request):
        from aip import AipImageClassify

        pic = request.FILES.get("pic")
        if pic:
            with open(os.path.join(BASE_DIR, "frontend/dist/static/media/land/%s") % pic.name, 'wb') as f:
                for chunk in pic.chunks():
                    f.write(chunk)
            file_path1 = os.path.join(BASE_DIR, "frontend/dist/static/media/land/%s") % pic.name
            # print(file_path1)
            """ 你的 APPID AK SK """

            client = AipImageClassify(APP_ID_BAIDU, API_KEY_BAIDU, SECRET_KEY_BAIDU)

            """ 读取图片 """

            def get_file_content(filePath):
                with open(filePath, 'rb') as fp:
                    return fp.read()

            image = get_file_content(file_path1)

            """ 调用地标识别 """
            try:
                resp = client.landmark(image)
                # print(resp['result']['landmark'])
                # print(resp)
                data = {
                    "landmark": resp['result']['landmark']
                }
                return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})
            except Exception as e:
                return HttpResponse('请提交地标图片')
        else:
            return HttpResponse('请提交地标图片')


class FaceView(View):
    def get(self, request):
        return render(request, 'search/face_recognize.html')

    def post(self, request):
        import base64

        import requests

        get_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=EQ1xbon78DH5drso7Gulmepp&client_secret=h6gr3EL1hWgNLseA31xdEhxGl5t7QSe9&'
        url = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'
        resp = requests.post(get_token_url)
        # print(resp.json()['access_token'])
        access_token = resp.json()['access_token']
        face_url = url + '?access_token=' + access_token
        headers = {
            'Content-Type': 'application/x-www-form-urlencode'

        }
        pic = request.FILES.get("pic")
        if pic:
            # 将前端提交来的图片保存本地
            # fs = FileSystemStorage()
            # fs.save(pic.name, pic)
            # print(os.path.join(BASE_DIR, "frontend/dist/static/media/test"))
            with open(os.path.join(BASE_DIR, "frontend/dist/static/media/face/%s") % pic.name, 'wb') as f:
                for chunk in pic.chunks():
                    f.write(chunk)
            file_path = os.path.join(BASE_DIR, "frontend/dist/static/media/face/%s") % pic.name
            # print(file_path)
            f = open(file_path, 'rb')
            content = f.read()
            img = base64.b64encode(content)
            params = {
                'image': img,
                'image_type': 'BASE64',
                "face_field": "age,beauty,expression,faceshape,gender,glasses,race,quality,emotion",
                'max_face_num': 5
            }
            try:
                response = requests.post(face_url, headers=headers, data=params)
                # print(response.json())
                result = response.json()['result']
                timeStamp = response.json()['timestamp']
                # print(timeStamp)
                timeArray = time.localtime(timeStamp)
                otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                data = {
                    '肤色': result['face_list'][0]['race']['type'],
                    '年龄': result['face_list'][0]['age'],
                    '有无配戴眼镜': result['face_list'][0]['glasses']['type'],
                    '性别': result['face_list'][0]['gender']['type'],
                    '脸型': result['face_list'][0]['face_shape']['type'],
                    # square: 正方形 triangle:三角形 oval: 椭圆 heart: 心形 round: 圆形
                    '识别状态': response.json()['error_msg'],
                    '当前识别时间': otherStyleTime
                }
                return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})
            except Exception as e:
                return HttpResponse('请提交人脸图片')

        else:
            return HttpResponse('请提交人脸图片')


class IC_card_View(View):
    def get(self, request):
        '''ic卡识别'''
        return render(request, 'search/ic_search.html')

    def post(self, request):
        from aip import AipOcr
        pic = request.FILES.get("pic")
        filePath = os.path.join(BASE_DIR, "frontend/dist/static/media/ic_card" + '/' + pic.name)
        if pic:
            with open(os.path.join(BASE_DIR, "frontend/dist/static/media/ic_card/%s") % pic.name, 'wb') as f:
                for chunk in pic.chunks():
                    f.write(chunk)

            """ 你的 APPID AK SK """

            client = AipOcr(APP_ID_BAIDU, API_KEY_BAIDU, SECRET_KEY_BAIDU)
            """ 读取图片 """

            def get_file_content(filePath):
                with open(filePath, 'rb') as fp:
                    return fp.read()

            image = get_file_content(filePath)
            try:
                resp = client.bankcard(image)
                number = resp['result']['bank_card_number']
                bankname = resp['result']['bank_name']
                # print('识别到的卡号是:%s' % resp['result']['bank_card_number'])
                # print('识别卡所属银行是:%s' % resp['result']['bank_name'])
                data = {
                    "识别卡号": number,
                    "所属银行": bankname
                }
                return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})
            except Exception as e:
                return HttpResponse('请提交银行卡照片')
