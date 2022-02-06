from django.contrib import admin
from .models import AdminPanelItem
# Register your models here.

@admin.register(AdminPanelItem)
class AdminPanelItemAdmin(admin.ModelAdmin):
    list_display = ('Title',)
    prepopulated_fields = {'Slug':('Title',)}
