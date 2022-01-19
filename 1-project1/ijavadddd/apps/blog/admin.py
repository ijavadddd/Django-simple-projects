from re import A
from django.contrib import admin
from .models import Author,Article
# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('FirstName','LastName','Education','Email','Status')
    search_fields = ('Status',)
    prepopulated_fields ={'Slug':('FirstName','LastName')}

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('Title','Tags','Status')
    search_fields = ('Status','Tags')
    prepopulated_fields = {'Slug':('Title',)}
