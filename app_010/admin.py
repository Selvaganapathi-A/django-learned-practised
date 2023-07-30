from django.contrib import admin

from app_010.model import ArticleModel, AuthorModel, BookModel, CarBrandModel
from app_010.model import CarFuelTypeModel, CarModel, CategoryModel
from app_010.model import DemoFKModel, DemoM2MModel, DemoModel, DemoO2OModel
from app_010.model import GenereModel, LanguageModel, PersonModel, PizzaModel
from app_010.model import ProductModel, StudentModel, TagModel, TeacherModel
from app_010.model import ToppingModel


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


admin.site.register(ArticleModel)
admin.site.register(AuthorModel)
admin.site.register(BookModel)
admin.site.register(CarModel)
admin.site.register(CarBrandModel)
admin.site.register(CarFuelTypeModel)
admin.site.register(CategoryModel)
admin.site.register(DemoModel)
admin.site.register(DemoFKModel)
admin.site.register(DemoM2MModel)
admin.site.register(DemoO2OModel)
admin.site.register(GenereModel)
admin.site.register(LanguageModel)
admin.site.register(PizzaModel)
admin.site.register(ProductModel)
admin.site.register(StudentModel)
admin.site.register(TagModel)
admin.site.register(TeacherModel)
admin.site.register(ToppingModel)
