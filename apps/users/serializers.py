# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 16:58
# @Author  : wy
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
