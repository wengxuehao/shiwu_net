"""shiwu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.views.generic.base import TemplateView
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path(r'', TemplateView.as_view(template_name="user/index.html")),    ## 这里将url的根路径指向vue中的index页面
#     # url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('user/', include('apps.users.urls')),
#     path('search/', include('apps.search.urls')),
#     path('service/', include('apps.service.urls')),
#     path('nlp/',include('apps.nlp.urls'))
# ]
from rest_framework import routers

from apps.users import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'^', include(router.urls)),
    # path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/', include('apps.users.urls')),
    path('search/', include('apps.search.urls')),
    path('service/', include('apps.service.urls')),
    path('nlp/', include('apps.nlp.urls'))
]
