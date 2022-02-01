from django.contrib import admin
from .models import UserRole,User,Category,Course,Session
# Register your models here.

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('Title','Id')

# @admin.register(UserRole)
# class UserRoleAdmin(admin.ModelAdmin):
#     list_display = ('Title','Id')