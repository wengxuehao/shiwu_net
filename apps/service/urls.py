from django.urls import path

from . import views

app_name = 'service'

urlpatterns = [
    path('voice/', views.Voice_View.as_view(), name='voice'),  # 语音技术
    path('Vision/', views.Vision_View.as_view(), name='Vision'),  # 视觉技术
    path('NLP/', views.NLP_View.as_view(), name='NLP'),  # 自然语言处理

]
