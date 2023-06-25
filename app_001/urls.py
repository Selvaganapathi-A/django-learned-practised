from django.urls import path

from . import views

# Put app name here
app_name: str = "app01"

# add your routes here.
urlpatterns = [
    path("", views.index, name="index"),
    path("method_01", views.method_01, name="method1"),
    path("method_02", views.method_02, name="method2"),
    path("method_03", views.method_03, name="method3"),
]
