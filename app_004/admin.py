from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "date_of_birth", "name", "father_name")


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "date_of_birth", "uuid", "age")
    pass
