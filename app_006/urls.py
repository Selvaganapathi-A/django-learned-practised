from django.urls import path

from . import views


# Put app name here
app_name: str = "app06"
# add your routes here.
urlpatterns = [
    path("", views.index, name="index"),
    path("student-list/", views.student_list, name="student_list"),
]
