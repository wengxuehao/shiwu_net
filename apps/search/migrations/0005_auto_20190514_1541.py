# Generated by Django 2.1.8 on 2019-05-14 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20190514_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recognize_model',
            name='name',
            field=models.CharField(choices=[('文字识别', 'character'), ('动物识别', 'animail'), ('植物识别', 'plant')], max_length=20, verbose_name='识别种类名称'),
        ),
    ]
