from django.urls import path

from . import views


# Put app name here
app_name: str = "app04"

# add your routes here.
urlpatterns = [
    path("", views.index, name="index"),
    # path("studentlist/", views.StudentList.as_view(), name="studentlist"),
    # path(
    #     "studentdetail/<uuid:pk>/", views.StudentDetail.as_view(), name="studentdetail"
    # ),
    # path("person/list/", views.person_list, name="person-list"),
]
