from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http.request import HttpHeaders, HttpRequest
from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from . import forms

# Create your views here.


def index(request: HttpRequest):
    print(settings.DATABASES)
    print(settings.TIME_ZONE)
    return render(
        request=request,
        template_name="ua/index.html",
        context={
            "web_page_title": "User Authendication",
            "user": request.user,
        },
    )


"""
`
class DashboardView(generic.View):
`
and in urls.py
`
    path(
        "dashboard/",
        view=login_required(
            views.DashboardView.as_view(), login_url=reverse_lazy("ua:login")
        ),
        name="dashboard",
    ),
`
------------------------------------------------------------------------------
(or)
------------------------------------------------------------------------------
`
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(LoginRequiredMixin, generic.View):
`
and in urls.py
`
    path("dashboard/", view=views.DashboardView.as_view(), name="dashboard")
`
"""


class CreateUserView(generic.View):
    """
    User Create User.....
    -> Get method to provide form.
    -> post method to get data and validate and save new user.
    """

    template_name: str = "ua/user-create.html"

    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            messages.error(
                request,
                message=(
                    "User already signed in. Signout before create another"
                    " user."
                ),
            )
            return redirect(to=reverse_lazy("ua:dashboard"))
        return render(
            request=request,
            template_name=self.template_name,
            context={
                "web_page_title": "Create User",
                "form": forms.SignupUserForm(),
                "user": request.user,
            },
        )

    def post(self, request: HttpRequest):
        if request.user.is_authenticated:
            print("access failed. as user is signed in.")
            messages.error(
                request,
                message=(
                    "User already signed in. Signout before create another"
                    " user."
                ),
            )
            return redirect(to=reverse_lazy("ua:dashboard"))
        data = request.POST.items()
        for key, value in data:
            print(key)
            print("\t", value)
        form = forms.SignupUserForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user: User = form.save(commit=True)
            login(request, user)
            messages.success(request, message="User Registered Successfully.")
            return redirect(to=reverse_lazy("ua:dashboard"))
        return render(
            request=request,
            template_name=self.template_name,
            context={
                "web_page_title": "Create User",
                "form": form,
                "user": request.user,
            },
        )


class LoginUserView(generic.View):
    template_name: str = "ua/user-signin.html"

    def get(self, request: HttpRequest):
        if request.user.is_authenticated:
            return redirect(to=reverse_lazy("ua:dashboard"))
        form: forms.LoginForm = forms.LoginForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                "web_page_title": "Login User",
                "form": form,
                "user": request.user,
            },
        )

    def post(self, request: HttpRequest):
        """
        Redirect to User Dashboard page if user is already authendicated.
        """

        if request.user.is_authenticated:
            return redirect(to=reverse_lazy("ua:dashboard"))

        form: forms.LoginForm = forms.LoginForm(
            request=request, data=request.POST, files=request.FILES
        )
        if not form.is_valid():
            return redirect(to=reverse_lazy("ua:login"))
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        user = authenticate(request, username=username, password=password)

        if user is None:
            return redirect(to=reverse_lazy("ua:login"))

        login(request=request, user=user)
        return redirect(
            to=reverse_lazy("ua:dashboard"),
        )


@login_required(
    redirect_field_name="bagasoore",
    login_url=reverse_lazy("ua:login"),
)
def logout_user(request: HttpRequest):
    logout(request)
    return redirect(to=reverse_lazy("ua:index"))


class DashboardView(generic.View):
    template_name: str = "ua/user-dashboard.html"

    def get(self, request: HttpRequest):
        if request.content_type == "application/json":
            return JsonResponse(
                data={
                    "aqi": "82",
                    "wind": "5kms nw",
                }
            )
        all_users = []
        if request.user.is_authenticated and request.user.is_superuser:  # type: ignore
            all_users = User.objects.all().order_by("first_name")

        return render(
            request=request,
            template_name=self.template_name,
            context={
                "web_page_title": "Dashboard",
                "all_users": all_users,
                "user": request.user,
            },
        )
