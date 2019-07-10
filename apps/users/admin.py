from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserProfileAdmin(UserAdmin):
    list_display = ['username', 'password',  'first_name', 'last_name', 'email', 'is_staff', 'is_active',
                    'date_joined']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active',
                     'date_joined']
    list_filter = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined']


admin.site.register(User, UserProfileAdmin)
