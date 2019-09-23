from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'user'
urlpatterns = [
    path('login/', views.UserView.as_view(), name='login'),
    path('manage/',views.User_manage.as_view(),name='manage'),
    path('index/',views.Index_view.as_view(),name='index'),
    path('register/',views.Register_View.as_view(),name='register')

]
# router = DefaultRouter()  # 可以处理视图的路由器
# router.register(r'books', views.UserView.as_view())  # 向路由器中注册视图集
# urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中