from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     model = User
#     list_display = ["email", "phone", "country", "is_staff"]
#     fieldsets  = (
#         ("Основная информация", {"fields": ("email", "phone", "country")},),
#         ("Права доступа", {"fields": ("is_staff", "is_active", "is_superuser")},),
#     )
#     add_fieldsets = (
#         ("Создать пользователя", {"fields": ("email", "password1", "password2")},)
#     )
#     search_fields = ["email", "phone"]
#     ordering = ('email',)
