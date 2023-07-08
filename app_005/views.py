from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import View

# Create your views here.


def index(req: HttpRequest):
    return render(
        request=req,
        template_name="app_005/index.html",
        context={
            "web_page_title": "App 005",
        },
    )


class PasswordResetView(View):
    template_name: str = "app_005/password-reset.html"

    def get(self, req: HttpRequest):
        pwrst = PasswordResetForm()
        af = AuthenticationForm()
        ucf = UserCreationForm()

        return render(
            req,
            self.template_name,
            context={
                "web_page_title": "Reset Password",
                "form": pwrst,
                "af": af,
                "ucf": ucf,
            },
        )

    def post(self, req: HttpRequest):
        form = PasswordResetForm(data=req.POST, files=req.FILES)
        data = req.POST.items()
        for k, v in data:
            print(k, "<~~~>", v)
        if form.is_valid():
            print(tuple(form.cleaned_data.items()))
        return render(
            req,
            self.template_name,
            context={
                "web_page_title": "Reset Password",
                "form": form,
            },
        )


print(dir(PasswordResetView))


if __name__ == "__main__":
    print(
        User,
        UserCreationForm,
        UserChangeForm,
        PasswordResetForm,
        PasswordResetForm,
        SetPasswordForm,
        AuthenticationForm,
        AdminPasswordChangeForm,
        PasswordChangeForm,
    )
    pass
