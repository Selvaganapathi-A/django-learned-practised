from django.urls import path

from . import views

# Put app name here
app_name: str = "app10"

# add your routes here.
urlpatterns = [
    path("", views.index, name="index"),
    path("authors/author-detail/<uuid:pk>", views.author_detail, name="author-detail"),
    path("authors/author-list", views.author_list, name="author-list"),
]
