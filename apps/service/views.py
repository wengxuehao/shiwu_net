from django.shortcuts import render

# Create your views here.
from django.views import View


class Voice_View(View):
    def get(self, request):
        # print('调取语音服务')
        return render(request, 'service/voice_recognition.html')


class Vision_View(View):
    def get(self, request):
        # print('调取视觉技术服务')
        return render(request, 'service/Vision_technology.html')


class NLP_View(View):
    def get(self, request):
        # print('调取nlp服务')
        return render(request, 'service/NLP.html')
