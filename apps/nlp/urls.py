from django.urls import path
# import lxml.html
# etree = lxml.html.etree
from . import views

app_name = 'nlp'

urlpatterns = [
    path('emotion/', views.nlp_View.as_view(), name='emotion'),  # 通用文字识别
    ]
