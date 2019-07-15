from django.db import models


# Create your models here.
class Recognize_model(models.Model):
    '''可识别的类型'''
    CATEHORY_CHOICES = (('文字识别', 'character'), ('动物识别', 'animail'), ('植物识别', "plant"))
    id = models.IntegerField(primary_key=True, verbose_name='识别种类id')
    name = models.CharField(choices=CATEHORY_CHOICES, max_length=20, verbose_name='识别种类名称')
    description = models.CharField(max_length=50, verbose_name='识别种类描述')

    class Meta:
        verbose_name = '识别种类模型'
        db_table = 'Recognize_Model'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
