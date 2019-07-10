# Generated by Django 2.1.8 on 2019-05-14 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recognize_model',
            name='name',
            field=models.CharField(choices=[('C', '文字识别'), ('A', '动物识别'), ('P', '植物识别')], max_length=20, verbose_name='识别种类名称'),
        ),
    ]
