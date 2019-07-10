from django.urls import path

from . import views
# from apps.search import views

app_name = 'search'

urlpatterns = [
    path('char/', views.Character_recognition.as_view(), name='char'),  # 通用文字识别
    path('animal/', views.Animal_recognition.as_view(), name='annimal'),  # 动物识别
    path('plant/', views.Plant_recognition.as_view(), name='plant'),  # 植物识别,
    path('vagetable/', views.Vagetable_View.as_view(), name='vagetable'),  # 蔬菜识别
    path('land/', views.Landview.as_view(), name='land'),  # 地标识别
    path('face/', views.FaceView.as_view(), name='face'),  # 人脸识别
    path('ic_card/',views.IC_card_View.as_view(),name='ic_card')  # 银行卡识别
]
