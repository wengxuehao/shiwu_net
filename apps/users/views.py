import random

from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework import viewsets

# from getrandom import ranstr
from utils import result, getrandom
from apps.service.models import Service_model
from apps.users.serializers import UserSerializer
# from .models import User
from django.contrib import auth

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password

User = get_user_model()
import logging

logger = logging.getLogger("django")


class Index_view(View):
    def get(self, request):
        services = Service_model.objects.all()
        # print(services)
        print('首页')
        return render(request, 'user/index.html')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserView(View):
    def get(self, request):
        #  跳转登录界面最好
        # return HttpResponse('HELLO WORLD 这是登录页面')
        print('用户登录界面')
        return render(request, 'user/login.html')

    def post(self, request):
        '''需要校验数据库用户和密码的对应关系'''
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        try:
            # user = User.objects.get(username=username)

            from django.contrib.auth import authenticate
            user = authenticate(username=username, password=password1)
            # django 内置的登录验证，如果获取到user对象则代表验证通过
            if user:
                if password1 == password2:
                    # 登录成功，并跳转到主页，且主页显示用户名
                    return result.result(message="两次密码一致，且密码验证成功，登录成功")
                else:
                    # print('两次密码不一致')
                    return result.params_error(message="两次密码不一致，登录失败")
            else:
                return result.params_error(message="密码错误，登录失败")

        except Exception as e:
            logger.error("用户登录失败：", e)
            # print('没有这个用户%s' % e)
            logger.error("没有这个用户")
            return result.params_error(message=e)


class Register_View(View):
    def get(self, request):
        return render(request, 'user/register.html')

    def post(self, request):
        password = request.POST.get('password')
        name = request.POST.get('name')
        email = request.POST.get('email')
        # 用户名唯一；需要校验数据库
        name_database = User.objects.filter(username=name).first()
        if name_database:
            logger.error("注册用户失败")
            return result.params_error(message="用户名已经存在")
        else:
            # 新建用户
            try:

                query_result = User(username=name, is_staff=0, email=email)
                query_result.set_password(password)

                query_result.save()

                # user = User()
                # user.username = name
                # user.email = email
                # user.password = password
                #
                # user.save()
            except Exception as e:
                logger.error("注册用户失败：", e)
                return result.params_error(message=e)
            # 把用户信息返回给前端，来渲染主页的用户信息

            data = {
                "username": name,
                "email": email,
                "userid": query_result.id
            }
            return result.result(message='注册成功', data=data)


class User_manage(View):
    '''
    用户管理页面
    支持用户更换头像
    用户修改密码
    '''

    def get(self, request):
        print('用户管理页面')
        return render(request, 'user/user_manage.html')

    def post(self, request):
        '''
        用户修改个人信息
        修改手机号码和用户名
        '''
        username = request.POST.get('username', '')
        telephone = request.POST.get('telephone', '')
        password = request.POST.get('password', '')
        userid = request.POST.get('userid', '')
        # 根据用户id来校验用户，修改用户信息id
        try:
            # query_result = User(id=userid)
            # query_result.set_password(password)
            #
            # query_result.save()
            # user = User.objects.filter(id=userid).first()
            query_result = User(id=userid)
            if query_result:
                query_result.telephone = telephone
                query_result.username = username
                query_result.set_password(password)
                query_result.save()
                return result.result(message="用户信息修改成功")
            else:
                return result.params_error(message="用户编号不存在")
        except Exception as e:
            return result.params_error(message=e)
