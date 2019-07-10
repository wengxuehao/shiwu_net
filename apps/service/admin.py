from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Service_model


class Service_model_Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']


admin.site.register(Service_model, Service_model_Admin)
