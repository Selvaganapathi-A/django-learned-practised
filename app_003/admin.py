from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["email", "name"]


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["isbn", "edition", "pages", "title", "author"]
