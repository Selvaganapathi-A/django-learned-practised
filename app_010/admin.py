from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MobileNumber)
class MobileNumberAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Email)
class EmailAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "age",
        "created_at",
        "updated_at",
    )
    list_per_page = 10
    list_display_links = ("first_name", "last_name", "age")

    pass
