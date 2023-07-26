from django.contrib import admin

from . import models

# Register your models here.


# @admin.register(models.Article)
# class ArticleAdmin(admin.ModelAdmin):
#     search_fields = ("headline",)
#     list_display = ["headline", "author", "date_posted"]
#     list_filter = ("author",)
#     list_per_page = 11
#     pass


# @admin.register(models.Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ["name", "contact"]
#     list_per_page = 11
