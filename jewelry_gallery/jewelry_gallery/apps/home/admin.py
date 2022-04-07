from django.contrib import admin
from . import models 
# Register your models here.

@admin.register(models.Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('Title','Status')
    search_fields = ('Title',)

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('FirstName','LastName','Role','Status')
    search_fields = ('Role','FirstName','LastName','PhoneNumber')


