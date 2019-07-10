import numpy
from PIL import Image, ImageFont, ImageDraw
from cv2 import cv2
import os

from shiwu.settings import BASE_DIR


def image_biaozhu(filePath,name):

    img_OpenCV = cv2.imread(filePath)
    # 图像从OpenCV格式转换成PIL格式
    img_PIL = Image.fromarray(cv2.cvtColor(img_OpenCV, cv2.COLOR_BGR2RGB))

    font = ImageFont.truetype(os.path.join(BASE_DIR, "frontend/dist/static/simhei.ttf"), 40)
    # 文字输出位置
    position = (0, 100)
    # 输出内容
    str = name

    # 需要先把输出的中文字符转换成Unicode编码形式
    # str = str.encode('utf8')

    draw = ImageDraw.Draw(img_PIL)
    draw.text(position, str, font=font, fill=(255, 0, 0))
    # 使用PIL中的save方法保存图片到本地
    # img_PIL.save('02.jpg', 'jpeg')

    # 转换回OpenCV格式
    img_OpenCV = cv2.cvtColor(numpy.asarray(img_PIL), cv2.COLOR_RGB2BGR)
    # cv2.imshow("window_name", img_OpenCV)
    save_path =os.path.join(BASE_DIR, "frontend/dist/static/media/biaozhu"+'/' +name + '.' + 'png')
    # print(save_path)
    cv2.imwrite(save_path, img_OpenCV)
    cv2.waitKey()
    return save_path
# image_biaozhu('jumao.png','lisi')