from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from apps.service.models import Service_model
from .models import User


class Index_view(View):
    def get(self, request):
        services = Service_model.objects.all()
        # print(services)
        print('首页')
        return render(request, 'user/index.html')


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
            user = User.objects.get(username=username)
            password = user.password
            if password1 == password:
                # print('密码正确')
                if password1 == password2:
                    # print('两次密码一致')
                    # 登陆成功，并跳转到主页，且主页显示用户名
                    return HttpResponse('登陆成功')
                else:
                    # print('两次密码不一致')
                    return HttpResponse('两次密码不一致')
            else:
                print('密码不正确')
            return HttpResponse('密码不正确')
        except Exception as e:
            # print('没有这个用户%s' % e)
            return HttpResponse('没有这个用户名，请先注册用户')


class Register_View(View):
    def get(self, request):
        print('用户注册页面')
        return render(request, 'user/register.html')

    def post(self, request):
        ps = request.POST.get('password')
        name = request.POST.get('name')
        email = request.POST.get('email')
        user = User()
        user.username = name
        user.email = email
        user.password = ps
        user.save()
        print('用户注册成功，并登录到主页')
        # 把用户信息返回给前端，来渲染主页的用户信息
        data = {
            "username": user.username,
        }
        return render(request, 'user/index.html',{"data":data})


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
        name = request.POST.get('name', '')
        telephone = request.POST.get('telephone', '')
        user = User.objects.filter(id=id)
        user.telephone = telephone
        user.name = name
        user.save()
        return HttpResponse('ok')
