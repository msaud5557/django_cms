from django.contrib import admin
from content.models import Articles, Category


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']



@admin.register(Articles)
class Articlesadmin(admin.ModelAdmin):
    list_display=['title','publication_date']


