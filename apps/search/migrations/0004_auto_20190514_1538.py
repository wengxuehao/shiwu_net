# Generated by Django 2.1.8 on 2019-05-14 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20190514_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recognize_model',
            name='description',
            field=models.CharField(max_length=50, verbose_name='识别种类描述'),
        ),
    ]
