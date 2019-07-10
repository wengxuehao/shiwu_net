from aip import AipNlp
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from shiwu.settings import APP_ID_BAIDU, API_KEY_BAIDU, SECRET_KEY_BAIDU


class nlp_View(View):
    def get(self, request):
        return render(request, 'nlp/emotion.html')

    def post(self, request):
        '''拿到前端提交来的数据'''
        content = request.POST.get('content')

        self.client = AipNlp(APP_ID_BAIDU, API_KEY_BAIDU, SECRET_KEY_BAIDU)
        text = content
        resp = self.client.sentimentClassify(text)
        positive = resp['items'][0]['positive_prob']
        negative = resp['items'][0]['negative_prob']
        data = {
            "情绪积极概率": positive,
            "情绪消极概率": negative
        }
        return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})
