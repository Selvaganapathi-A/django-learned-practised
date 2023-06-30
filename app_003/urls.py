from django.urls import path

from . import views

# Put app name here
app_name: str = "app03"

# add your routes here.
urlpatterns = [
    path("", views.index, name="index"),
    path("cbv_1/", views.IndexView.as_view(), name="cbv01"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("person/", views.PersonVew.as_view(), name="person"),
]
