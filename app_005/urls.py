from django.urls import path

from . import views

# Put app name here
app_name: str = "app05"

# add your routes here.
urlpatterns = [
    path("", views.index, name="index"),
    path(
        "reset-password",
        views.PasswordResetView.as_view(),
        name="reset-password",
    ),
]
