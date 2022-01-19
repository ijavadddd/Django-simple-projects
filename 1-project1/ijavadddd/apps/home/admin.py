from django.contrib import admin
from .models import Author,Tutorial


# Register your models here.
@admin.register(Author)
class ProfessorDisplay(admin.ModelAdmin):
    list_display = ('FirstName','LastName','Status')
    list_filter = ('Status',)
    search_fields = ('FirstName','LastName')
    ordering = ['AuthorId']

class TutorialDisplay(admin.ModelAdmin):
    list_display = ('TutorialTitle','Author','Status')
    list_filter = ('Status','Author')
    search_fields = ('TutorialTitle','Author')
    ordering = ['TutorialId']
    prepopulated_fields = {'Slug': ('TutorialTitle',)}
admin.site.register(Tutorial,TutorialDisplay)

