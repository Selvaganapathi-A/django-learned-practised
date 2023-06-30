from django.urls import path

from . import views, views_001, views_002, views_003

# Put app name here
app_name: str = "app02"

# add your routes here.
urlpatterns = [
    path("", views.index, name="index"),
    #
    path("myview/", views_001.MyView.as_view(), name="myview"),
    path("mytemplateview/", views_001.MyTemplateView.as_view(), name="mytemplateview"),
    path("myredirectview", views_001.myRedirectView.as_view(), name="myredirectview"),
    path(
        "mypermenantredirectview",
        views_001.MyPermenantRedirectView.as_view(),
        name="mypermenantredirectview",
    ),
    #
    path("contactformview/", views_003.ContactFormView.as_view(), name="contactformview"),
    path("mydetailview/<int:pk>/", views_002.MyDetailView.as_view(), name="mydetailview"),
    path("mylistview/", views_002.MyListView.as_view(), name="mylistview"),
    #
    path("authorcreateview/", views_003.AuthorCreateView.as_view(), name="authorcreateview"),
    path(
        "authorupdateview/<int:pk>/", views_003.AuthorUpdateView.as_view(), name="authorupdateview"
    ),
    path(
        "authordeleteview/<int:pk>/", views_003.AuthorDeleteView.as_view(), name="authordeleteview"
    ),
    #
    path("authordetail/<int:pk>/", views_003.AuthorDetailView.as_view(), name="authordetailview"),
    path("authorlist/", views_003.AuthorListView.as_view(), name="authorlistview"),
]
