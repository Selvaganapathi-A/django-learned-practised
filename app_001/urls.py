from django.urls import path

from . import views

# Put app name here
app_name: str = "app01"

# add your routes here.
urlpatterns = [
    path("", views.index, name="index"),
]
