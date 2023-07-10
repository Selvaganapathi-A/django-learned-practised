from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")
        widgets = {
            "username": forms.widgets.TextInput(
                attrs={
                    "class": "form-field",
                }
            ),
            "password": forms.widgets.PasswordInput(
                attrs={
                    "class": "form-field",
                    # "type": "password",
                }
            ),
        }
        help_texts = {
            "username": ("Username",),
            "password": ("it is case sensitive. insert correctly.",),
        }

    def __init__(self, *args, **kwargs) -> None:
        super(LoginForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["password"].widget.attrs["placeholder"] = "Password"


class SignupUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

    pass
