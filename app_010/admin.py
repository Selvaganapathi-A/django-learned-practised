from django.contrib import admin

from app_010.app_models import ArticleModel, AuthorModel, BookModel
from app_010.app_models import CarBrandModel, CarFuelTypeModel, CarModel
from app_010.app_models import CategoryModel, DemoModel, DummyModel
from app_010.app_models import GenereModel, LanguageModel, PersonModel
from app_010.app_models import PizzaModel, ProductModel, StudentModel
from app_010.app_models import TagModel, TeacherModel, ToppingModel
from app_010.app_models.Demo import DemoModelFK, DemoModelM2M, DemoModelO2O
from app_010.app_models.Dummy import DummyModelFK, DummyModelM2M, DummyModelO2O

from . import models


# Register your models here.


@admin.register(PersonModel)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "firstname",
        "lastname",
        "age",
        "created_at",
        "updated_at",
    )
    list_per_page = 10
    list_display_links = ("firstname", "lastname", "age")

    pass


admin.site.register(ArticleModel)
admin.site.register(AuthorModel)
admin.site.register(BookModel)
admin.site.register(CarModel)
admin.site.register(CarBrandModel)
admin.site.register(CarFuelTypeModel)
admin.site.register(CategoryModel)
admin.site.register(DemoModel)
admin.site.register(DemoModelFK)
admin.site.register(DemoModelM2M)
admin.site.register(DemoModelO2O)
admin.site.register(DummyModel)
admin.site.register(DummyModelFK)
admin.site.register(DummyModelM2M)
admin.site.register(DummyModelO2O)
admin.site.register(GenereModel)
admin.site.register(LanguageModel)
admin.site.register(PizzaModel)
admin.site.register(ProductModel)
admin.site.register(StudentModel)
admin.site.register(TagModel)
admin.site.register(TeacherModel)
admin.site.register(ToppingModel)
