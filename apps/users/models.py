import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    """
    用户模型
    """
    # telephone = models.CharField(max_length=11, verbose_name='手机号',default='')
    # password = models.CharField(max_length=100,verbose_name='密码',default='')
    # 用户id为uuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,verbose_name="用户编号")
    icon = models.ImageField(upload_to='img', default='', verbose_name='用户头像')
    user_num = models.CharField(max_length=128,default="")

    class Meta:
        verbose_name = '用户模型'
        db_table = 'user'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
