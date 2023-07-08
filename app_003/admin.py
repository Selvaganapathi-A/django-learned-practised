from django.contrib import admin

from . import models
from .app_forms import forms_01
from .app_models import models_02

# Register your models here.


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["email", "name"]


class BookAdmin(admin.ModelAdmin):
    exclude = ("isbn",)
    ordering = ("title", "author")
    list_display = ["title", "author", "edition", "pages"]

    list_filter = ("author", "language")


admin.site.register(models.Book, BookAdmin)
