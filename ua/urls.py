from django.contrib.auth.decorators import login_required
from django.urls import path, reverse_lazy

from . import views

app_name = "ua"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", view=views.LoginUserView.as_view(), name="login"),
    path("signup/", view=views.CreateUserView.as_view(), name="signup"),
    path(
        "dashboard/",
        view=login_required(
            views.DashboardView.as_view(), login_url=reverse_lazy("ua:login")
        ),
        name="dashboard",
    ),
    path("logout/",views.logout_user, name="logout"),
]
