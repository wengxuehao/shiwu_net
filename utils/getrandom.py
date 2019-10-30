# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 16:22
# @Author  : wy
# @File    : getrandom.py
# @Software: PyCharm
import random


def ranstr(num):
    # 猜猜变量名为啥叫 H
    # ranstr(随机个数)
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    salt = ''
    for i in range(num):
        salt += random.choice(H)

    return salt
