from django.contrib import admin
from .models import Autor,Tutorial


# Register your models here.
@admin.register(Autor)
class ProfessorDisplay(admin.ModelAdmin):
    list_display = ('FirstName','LastName','Status')
    list_filter = ('Status',)
    search_fields = ('FirstName','LastName')
    ordering = ['AutorId']

class TutorialDisplay(admin.ModelAdmin):
    list_display = ('TutorialTitle','Autor','Status')
    list_filter = ('Status','Autor')
    search_fields = ('TutorialTitle','Autor')
    ordering = ['TutorialId']
    prepopulated_fields = {'Slug': ('TutorialTitle',)}
admin.site.register(Tutorial,TutorialDisplay)

