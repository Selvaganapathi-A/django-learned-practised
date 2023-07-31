from django.urls import path

from app_010 import view, views


# Put app name here
app_name: str = "app10"


# add your routes here.
urlpatterns = [
    path("", views.index, name="index"),
    path("humanize", views.humanized_view, name="humanize"),
]


ARTICLE_urlpatterns = [
    # Create
    path(
        "Article/add/",
        view.ArticleView.ArticleCreateView.as_view(),
        name="article-create",
    ),
    # Read
    path(
        "Article/",
        view.ArticleView.ArticleListView.as_view(),
        name="article-read-list",
    ),
    path(
        "Article/<int:pk>/",
        view.ArticleView.ArticleDetailView.as_view(),
        name="article-read",
    ),
    # Update
    path(
        "Article/<int:pk>/change/",
        view.ArticleView.ArticleUpdateView.as_view(),
        name="article-change",
    ),
    # Delete
    path(
        "Article/<int:pk>/delete/",
        view.ArticleView.ArticleDeleteView.as_view(),
        name="article-delete",
    ),
]

AUTHOR_urlpatterns = [
    # Create
    path(
        "Author/add/",
        view.AuthorView.AuthorCreateView.as_view(),
        name="author-create",
    ),
    # Read
    path(
        "Author/",
        view.AuthorView.AuthorListView.as_view(),
        name="author-read-list",
    ),
    path(
        "Author/<uuid:pk>/",
        view.AuthorView.AuthorDetailView.as_view(),
        name="author-read",
    ),
    # Update
    path(
        "Author/<uuid:pk>/change/",
        view.AuthorView.AuthorUpdateView.as_view(),
        name="author-change",
    ),
    # Delete
    path(
        "Author/<uuid:pk>/delete/",
        view.AuthorView.AuthorDeleteView.as_view(),
        name="author-delete",
    ),
]

BOOK_urlpatterns = [
    # Create
    path(
        "Book/add/", view.BookView.BookCreateView.as_view(), name="book-create"
    ),
    # Read
    path("Book/", view.BookView.BookListView.as_view(), name="book-read-list"),
    path(
        "Book/<int:pk>/",
        view.BookView.BookDetailView.as_view(),
        name="book-read",
    ),
    # Update
    path(
        "Book/<int:pk>/change/",
        view.BookView.BookUpdateView.as_view(),
        name="book-change",
    ),
    # Delete
    path(
        "Book/<int:pk>/delete/",
        view.BookView.BookDeleteView.as_view(),
        name="book-delete",
    ),
]

CAR_urlpatterns = [
    # Create
    path("Car/add/", view.CarView.CarCreateView.as_view(), name="car-create"),
    # Read
    path("Car/", view.CarView.CarListView.as_view(), name="car-read-list"),
    path(
        "Car/<int:pk>/",
        view.CarView.CarDetailView.as_view(),
        name="car-read",
    ),
    # Update
    path(
        "Car/<int:pk>/change/",
        view.CarView.CarUpdateView.as_view(),
        name="car-change",
    ),
    # Delete
    path(
        "Car/<int:pk>/delete/",
        view.CarView.CarDeleteView.as_view(),
        name="car-delete",
    ),
]

CARBRAND_urlpatterns = [
    # Create
    path(
        "CarBrand/add/",
        view.CarBrandView.CarBrandCreateView.as_view(),
        name="carbrand-create",
    ),
    # Read
    path(
        "CarBrand/",
        view.CarBrandView.CarBrandListView.as_view(),
        name="carbrand-read-list",
    ),
    path(
        "CarBrand/<int:pk>/",
        view.CarBrandView.CarBrandDetailView.as_view(),
        name="carbrand-read",
    ),
    # Update
    path(
        "CarBrand/<int:pk>/change/",
        view.CarBrandView.CarBrandUpdateView.as_view(),
        name="carbrand-change",
    ),
    # Delete
    path(
        "CarBrand/<int:pk>/delete/",
        view.CarBrandView.CarBrandDeleteView.as_view(),
        name="carbrand-delete",
    ),
]

CARFUELTYPE_urlpatterns = [
    # Create
    path(
        "CarFuelType/add/",
        view.CarFuelTypeView.CarFuelTypeCreateView.as_view(),
        name="carfueltype-create",
    ),
    # Read
    path(
        "CarFuelType/",
        view.CarFuelTypeView.CarFuelTypeListView.as_view(),
        name="carfueltype-read-list",
    ),
    path(
        "CarFuelType/<int:pk>/",
        view.CarFuelTypeView.CarFuelTypeDetailView.as_view(),
        name="carfueltype-read",
    ),
    # Update
    path(
        "CarFuelType/<int:pk>/change/",
        view.CarFuelTypeView.CarFuelTypeUpdateView.as_view(),
        name="carfueltype-change",
    ),
    # Delete
    path(
        "CarFuelType/<int:pk>/delete/",
        view.CarFuelTypeView.CarFuelTypeDeleteView.as_view(),
        name="carfueltype-delete",
    ),
]

CATEGORY_urlpatterns = [
    # Create
    path(
        "Category/add/",
        view.CategoryView.CategoryCreateView.as_view(),
        name="category-create",
    ),
    # Read
    path(
        "Category/",
        view.CategoryView.CategoryListView.as_view(),
        name="category-read-list",
    ),
    path(
        "Category/<int:pk>/",
        view.CategoryView.CategoryDetailView.as_view(),
        name="category-read",
    ),
    # Update
    path(
        "Category/<int:pk>/change/",
        view.CategoryView.CategoryUpdateView.as_view(),
        name="category-change",
    ),
    # Delete
    path(
        "Category/<int:pk>/delete/",
        view.CategoryView.CategoryDeleteView.as_view(),
        name="category-delete",
    ),
]

DEMO_urlpatterns = [
    # Create
    path(
        "Demo/add/", view.DemoView.DemoCreateView.as_view(), name="demo-create"
    ),
    # Read
    path("Demo/", view.DemoView.DemoListView.as_view(), name="demo-read-list"),
    path(
        "Demo/<int:pk>/",
        view.DemoView.DemoDetailView.as_view(),
        name="demo-read",
    ),
    # Update
    path(
        "Demo/<int:pk>/change/",
        view.DemoView.DemoUpdateView.as_view(),
        name="demo-change",
    ),
    # Delete
    path(
        "Demo/<int:pk>/delete/",
        view.DemoView.DemoDeleteView.as_view(),
        name="demo-delete",
    ),
]

DEMOFK_urlpatterns = [
    # Create
    path(
        "DemoFK/add/",
        view.DemoFKView.DemoFKCreateView.as_view(),
        name="demofk-create",
    ),
    # Read
    path(
        "DemoFK/",
        view.DemoFKView.DemoFKListView.as_view(),
        name="demofk-read-list",
    ),
    path(
        "DemoFK/<int:pk>/",
        view.DemoFKView.DemoFKDetailView.as_view(),
        name="demofk-read",
    ),
    # Update
    path(
        "DemoFK/<int:pk>/change/",
        view.DemoFKView.DemoFKUpdateView.as_view(),
        name="demofk-change",
    ),
    # Delete
    path(
        "DemoFK/<int:pk>/delete/",
        view.DemoFKView.DemoFKDeleteView.as_view(),
        name="demofk-delete",
    ),
]

DEMOM2M_urlpatterns = [
    # Create
    path(
        "DemoM2M/add/",
        view.DemoM2MView.DemoM2MCreateView.as_view(),
        name="demom2m-create",
    ),
    # Read
    path(
        "DemoM2M/",
        view.DemoM2MView.DemoM2MListView.as_view(),
        name="demom2m-read-list",
    ),
    path(
        "DemoM2M/<int:pk>/",
        view.DemoM2MView.DemoM2MDetailView.as_view(),
        name="demom2m-read",
    ),
    # Update
    path(
        "DemoM2M/<int:pk>/change/",
        view.DemoM2MView.DemoM2MUpdateView.as_view(),
        name="demom2m-change",
    ),
    # Delete
    path(
        "DemoM2M/<int:pk>/delete/",
        view.DemoM2MView.DemoM2MDeleteView.as_view(),
        name="demom2m-delete",
    ),
]

DEMOO2O_urlpatterns = [
    # Create
    path(
        "DemoO2O/add/",
        view.DemoO2OView.DemoO2OCreateView.as_view(),
        name="demoo2o-create",
    ),
    # Read
    path(
        "DemoO2O/",
        view.DemoO2OView.DemoO2OListView.as_view(),
        name="demoo2o-read-list",
    ),
    path(
        "DemoO2O/<int:pk>/",
        view.DemoO2OView.DemoO2ODetailView.as_view(),
        name="demoo2o-read",
    ),
    # Update
    path(
        "DemoO2O/<int:pk>/change/",
        view.DemoO2OView.DemoO2OUpdateView.as_view(),
        name="demoo2o-change",
    ),
    # Delete
    path(
        "DemoO2O/<int:pk>/delete/",
        view.DemoO2OView.DemoO2ODeleteView.as_view(),
        name="demoo2o-delete",
    ),
]

GENERE_urlpatterns = [
    # Create
    path(
        "Genere/add/",
        view.GenereView.GenereCreateView.as_view(),
        name="genere-create",
    ),
    # Read
    path(
        "Genere/",
        view.GenereView.GenereListView.as_view(),
        name="genere-read-list",
    ),
    path(
        "Genere/<int:pk>/",
        view.GenereView.GenereDetailView.as_view(),
        name="genere-read",
    ),
    # Update
    path(
        "Genere/<int:pk>/change/",
        view.GenereView.GenereUpdateView.as_view(),
        name="genere-change",
    ),
    # Delete
    path(
        "Genere/<int:pk>/delete/",
        view.GenereView.GenereDeleteView.as_view(),
        name="genere-delete",
    ),
]

LANGUAGE_urlpatterns = [
    # Create
    path(
        "Language/add/",
        view.LanguageView.LanguageCreateView.as_view(),
        name="language-create",
    ),
    # Read
    path(
        "Language/",
        view.LanguageView.LanguageListView.as_view(),
        name="language-read-list",
    ),
    path(
        "Language/<int:pk>/",
        view.LanguageView.LanguageDetailView.as_view(),
        name="language-read",
    ),
    # Update
    path(
        "Language/<int:pk>/change/",
        view.LanguageView.LanguageUpdateView.as_view(),
        name="language-change",
    ),
    # Delete
    path(
        "Language/<int:pk>/delete/",
        view.LanguageView.LanguageDeleteView.as_view(),
        name="language-delete",
    ),
]

PERSON_urlpatterns = [
    # Create
    path(
        "Person/add/",
        view.PersonView.PersonCreateView.as_view(),
        name="person-create",
    ),
    # Read
    path(
        "Person/",
        view.PersonView.PersonListView.as_view(),
        name="person-read-list",
    ),
    path(
        "Person/<int:pk>/",
        view.PersonView.PersonDetailView.as_view(),
        name="person-read",
    ),
    # Update
    path(
        "Person/<int:pk>/change/",
        view.PersonView.PersonUpdateView.as_view(),
        name="person-change",
    ),
    # Delete
    path(
        "Person/<int:pk>/delete/",
        view.PersonView.PersonDeleteView.as_view(),
        name="person-delete",
    ),
]

PIZZA_urlpatterns = [
    # Create
    path(
        "Pizza/add/",
        view.PizzaView.PizzaCreateView.as_view(),
        name="pizza-create",
    ),
    # Read
    path(
        "Pizza/", view.PizzaView.PizzaListView.as_view(), name="pizza-read-list"
    ),
    path(
        "Pizza/<int:pk>/",
        view.PizzaView.PizzaDetailView.as_view(),
        name="pizza-read",
    ),
    # Update
    path(
        "Pizza/<int:pk>/change/",
        view.PizzaView.PizzaUpdateView.as_view(),
        name="pizza-change",
    ),
    # Delete
    path(
        "Pizza/<int:pk>/delete/",
        view.PizzaView.PizzaDeleteView.as_view(),
        name="pizza-delete",
    ),
]

PRODUCT_urlpatterns = [
    # Create
    path(
        "Product/add/",
        view.ProductView.ProductCreateView.as_view(),
        name="product-create",
    ),
    # Read
    path(
        "Product/",
        view.ProductView.ProductListView.as_view(),
        name="product-read-list",
    ),
    path(
        "Product/<int:pk>/",
        view.ProductView.ProductDetailView.as_view(),
        name="product-read",
    ),
    # Update
    path(
        "Product/<int:pk>/change/",
        view.ProductView.ProductUpdateView.as_view(),
        name="product-change",
    ),
    # Delete
    path(
        "Product/<int:pk>/delete/",
        view.ProductView.ProductDeleteView.as_view(),
        name="product-delete",
    ),
]

STUDENT_urlpatterns = [
    # Create
    path(
        "Student/add/",
        view.StudentView.StudentCreateView.as_view(),
        name="student-create",
    ),
    # Read
    path(
        "Student/",
        view.StudentView.StudentListView.as_view(),
        name="student-read-list",
    ),
    path(
        "Student/<uuid:pk>/",
        view.StudentView.StudentDetailView.as_view(),
        name="student-read",
    ),
    # Update
    path(
        "Student/<uuid:pk>/change/",
        view.StudentView.StudentUpdateView.as_view(),
        name="student-change",
    ),
    # Delete
    path(
        "Student/<uuid:pk>/delete/",
        view.StudentView.StudentDeleteView.as_view(),
        name="student-delete",
    ),
]

TAG_urlpatterns = [
    # Create
    path("Tag/add/", view.TagView.TagCreateView.as_view(), name="tag-create"),
    # Read
    path("Tag/", view.TagView.TagListView.as_view(), name="tag-read-list"),
    path(
        "Tag/<int:pk>/",
        view.TagView.TagDetailView.as_view(),
        name="tag-read",
    ),
    # Update
    path(
        "Tag/<int:pk>/change/",
        view.TagView.TagUpdateView.as_view(),
        name="tag-change",
    ),
    # Delete
    path(
        "Tag/<int:pk>/delete/",
        view.TagView.TagDeleteView.as_view(),
        name="tag-delete",
    ),
]

TEACHER_urlpatterns = [
    # Create
    path(
        "Teacher/add/",
        view.TeacherView.TeacherCreateView.as_view(),
        name="teacher-create",
    ),
    # Read
    path(
        "Teacher/",
        view.TeacherView.TeacherListView.as_view(),
        name="teacher-read-list",
    ),
    path(
        "Teacher/<int:pk>/",
        view.TeacherView.TeacherDetailView.as_view(),
        name="teacher-read",
    ),
    # Update
    path(
        "Teacher/<int:pk>/change/",
        view.TeacherView.TeacherUpdateView.as_view(),
        name="teacher-change",
    ),
    # Delete
    path(
        "Teacher/<int:pk>/delete/",
        view.TeacherView.TeacherDeleteView.as_view(),
        name="teacher-delete",
    ),
]

TOPPING_urlpatterns = [
    # Create
    path(
        "Topping/add/",
        view.ToppingView.ToppingCreateView.as_view(),
        name="topping-create",
    ),
    # Read
    path(
        "Topping/",
        view.ToppingView.ToppingListView.as_view(),
        name="topping-read-list",
    ),
    path(
        "Topping/<int:pk>/",
        view.ToppingView.ToppingDetailView.as_view(),
        name="topping-read",
    ),
    # Update
    path(
        "Topping/<int:pk>/change/",
        view.ToppingView.ToppingUpdateView.as_view(),
        name="topping-change",
    ),
    # Delete
    path(
        "Topping/<int:pk>/delete/",
        view.ToppingView.ToppingDeleteView.as_view(),
        name="topping-delete",
    ),
]

urlpatterns += (
    ARTICLE_urlpatterns
    + AUTHOR_urlpatterns
    + BOOK_urlpatterns
    + CAR_urlpatterns
    + CARBRAND_urlpatterns
    + CARFUELTYPE_urlpatterns
    + CATEGORY_urlpatterns
    + DEMO_urlpatterns
    + DEMOFK_urlpatterns
    + DEMOM2M_urlpatterns
    + DEMOO2O_urlpatterns
    + GENERE_urlpatterns
    + LANGUAGE_urlpatterns
    + PERSON_urlpatterns
    + PIZZA_urlpatterns
    + PRODUCT_urlpatterns
    + STUDENT_urlpatterns
    + TAG_urlpatterns
    + TEACHER_urlpatterns
    + TOPPING_urlpatterns
) + [
    path("fs/", view.Formset.Formset_Pizza.formset_view, name="fs"),
]
