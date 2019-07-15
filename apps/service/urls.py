from django.urls import path

from . import views

app_name = 'service'

urlpatterns = [
    # 此处的name，用作加载模板文件---{% url 'service:Voice' %}
    path('Voice/', views.Voice_View.as_view(), name='Voice'),  # 语音技术
    path('Vision/', views.Vision_View.as_view(), name='Vision'),  # 视觉技术
    path('NLP/', views.NLP_View.as_view(), name='NLP'),  # 自然语言处理

]
