from django.shortcuts import render

# Create your views here.
from django.views import View

from utils import result


class Voice_View(View):
    def get(self, request):
        # print('调取语音服务')
        return render(request, 'service/voice_recognition.html')


class Vision_View(View):
    def get(self, request):
        # print('调取视觉技术服务')
        # return render(request, 'service/Vision_technology.html')\
        data = {
            "list":["返回注册信息列表"]
        }
        return result.result(message="success",data=data)



class NLP_View(View):
    def get(self, request):
        # print('调取nlp服务')
        return render(request, 'service/NLP.html')
