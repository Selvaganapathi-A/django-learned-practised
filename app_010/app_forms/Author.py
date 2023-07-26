from django import forms

from app_010.app_models import Author


class AuthorForm(forms.ModelForm):
    # Create Metadata
    class Meta:
        model = Author.AuthorModel
        # fields = ("firstName", "lastName", "contact")
        fields = "__all__"
        # exclude = ("name", )
        widgets = {
            "firstName": forms.widgets.TextInput(
                attrs={
                    "class": "form-field firstName",
                    "id": "a-fn",
                    "required": True,
                }
            ),
            "lastName": forms.widgets.TextInput(
                attrs={
                    "class": "form-field lastName",
                    "id": "a-ln",
                    "required": False,
                }
            ),
        }
        labels = {
            "firstName": "First Name",
            "lastName": "Last Name",
            "contact": "Mobile Number",
        }
        help_texts = {
            "firstName": "Actual or fictional Name ",
            "lastName": "if Any.",
        }
