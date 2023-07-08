from django.urls import path

from . import views

# Put app name here
app_name: str = "app03"

# add your routes here.
urlpatterns = [
    path("", views.index, name="index"),
    path("form-example/", views.form_example, name="form-example"),
    path("field-widget/", views.widget_example, name="field-widget"),
    path("html-widget/", views.html_widget_example, name="html-widget"),
    path("author/", views.IndexView.as_view(), name="author"),
    path("person/", views.PersonVew.as_view(), name="person"),
]
