from django.db import models


# Create your models here.
class Service_model(models.Model):
    CATEHORY_CHOICES = (('语言技术', 'voice'), ('视觉技术', 'vision'), ('自然语言处理', 'nlp'))
    id = models.IntegerField(primary_key=True, verbose_name='服务名称编号')
    name = models.CharField(choices=CATEHORY_CHOICES, max_length=20, verbose_name='服务名称')
    description = models.CharField(max_length=50, verbose_name='服务名称描述')

    class Meta:
        verbose_name = '服务名称'
        db_table = 'Service_Model'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
