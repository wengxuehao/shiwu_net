# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 12:59
# @Author  : wy
# @File    : wusundemo.py
# @Software: PyCharm
# encoding:utf-8
import base64
import requests
import base64
import requests

get_token_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=AyuLyqu4FNB4klZvGAHSjVaQ&client_secret=MI53Tuf71Xt4KoQiqT7G3lUH96DC3mZ8&'
# url = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/dish'
f = open('D:\wxh\shiwu\微信图片_20190823130358.jpg', 'rb')
img = base64.b64encode(f.read())
url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/image_quality_enhance"
resp = requests.post(get_token_url)
# print(resp.json()['access_token'])
access_token = resp.json()['access_token']
print(access_token)
request_url = url + "?access_token=" + access_token
headers = {
    'Content-Type': 'application/x-www-form-urlencode'

}
data = {"image": img}
response = requests.post(url=request_url,data=data,headers=headers)
content = response.json()
print(content)
'''
图像无损放大
'''
# encoding:utf-8
import base64

# '''
# 图像无损放大
# '''

# 二进制方式打开图片文件


# params = {"image": img}
# # params = urllib.urlencode(params)
#
# access_token = '[调用鉴权接口获取的token]'
# request_url = request_url + "?access_token=" + access_token
# request = urllib2.Request(url=request_url, data=params)
# request.add_header('Content-Type', 'application/x-www-form-urlencoded')
# response = urllib2.urlopen(request)
# content = response.read()
# if content:
#     print content
