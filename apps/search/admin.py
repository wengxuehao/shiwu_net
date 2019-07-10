from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Recognize_model


class Recognize_model_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


admin.site.register(Recognize_model, Recognize_model_Admin)
