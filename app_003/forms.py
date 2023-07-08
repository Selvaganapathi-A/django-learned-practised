from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import datetime

from . import models

"""

for details refer:-
    1) https://stackoverflow.com/questions/15348007/djangos-modelform-where-is-the-list-of-meta-options
        -- form meta options

    2) https://ordinarycoders.com/blog/article/using-django-form-fields-and-widgets
        -- info text

    3) https://docs.djangoproject.com/en/4.2/topics/forms/
        -- for rendering form in html

"""


def email_validator(value: str):
    print("email-validator function", value)
    if not value.endswith("@gmail.com"):
        raise ValidationError(
            _(
                "email provider must be gmail only.",
            ),
            code="gmail",
            params={
                "mail": value,
            },
        )
    else:
        print("value ok", f"{value} provider is from google.")


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ["name", "email"]  # fields to include
        # exclude = ['email'] # fields to exclude from form
        widgets = {
            "name": forms.widgets.TextInput(
                attrs={
                    "class": "form-field author-name",
                    "id": "author-name",
                    "required": True,
                }
            ),
        }
        labels = {
            "name": "Author Name",
            "email": "Author Contact Mail ID",
        }

        help_texts = {
            "name": (
                "Author Name Should not include Iniitials, Father name & Family Names."
                " blah...."
            ),
            "email": "valid email id.",
        }


class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=64, min_length=2)
    last_name = forms.CharField(
        max_length=64,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Last Name",
                "rows": 10,
                "cols": 30,
                "class": "form-field",
            }
        ),
    )
    mobile = forms.CharField(
        label="Mobile Number",
        label_suffix="(:-:)",
        widget=forms.TextInput(
            attrs={
                "pattern": r"[9876]\d{9}",
            }
        ),
        error_messages={
            "invalid": "Enter Valid mobile number.",
            "required": "10 digit valid indian mobile number only accepted currently.",
        },
        max_length=10,
        min_length=10,
    )

    comment = forms.CharField(
        widget=forms.Textarea(
            {
                "rows": 4,
                "cols": 60,
            }
        ),
        label="Biography",
    )

    mail = forms.EmailField(
        help_text="gmail, yahoo, outlook, live, ",
        widget=forms.widgets.EmailInput(
            attrs={
                "class": "email",
            },
        ),
        label="Email",
        validators=[
            email_validator,
        ],
        error_messages={
            # "invalid": "provide valid email address",
            "required": "recommended gmail, yahoo, live or outlook",
        },
    )

    contact_via_call = forms.BooleanField(
        widget=forms.widgets.CheckboxInput(
            attrs={
                "class": "accept google jnh",
                "checked": True,
            }
        )
    )

    birth_day = forms.DateField()

    birth_year = forms.DateField(
        widget=forms.widgets.SelectDateWidget(
            years=(
                1980,
                1990,
                2000,
                2010,
            ),
        )
    )

    school_joined = forms.DateField(
        widget=forms.widgets.NumberInput(
            attrs={"type": "date"},
        ),
    )

    marriage_day = forms.DateField(
        widget=forms.widgets.NumberInput(
            attrs={
                "type": "date",
                "step": 15,
                "value": "1994-01-01",
            }
        ),
        initial="1994-08-05",
    )

    def __init__(self, *args, **kwargs) -> None:
        super(PersonForm, self).__init__(*args, **kwargs)
        self.label_suffix = ""
        for field in self.visible_fields():
            # field.field.widget.attrs["class"] = "form-field"
            css_class = field.field.widget.attrs.get("class", "")
            css_class += " form-field"
            field.field.widget.attrs["class"] = css_class
            # print((field.field.widget.attrs))
            # print(field)
            # print(field.__dict__)
            # print(dir(field))

    def clean(self):
        super(PersonForm, self).clean()

        username = self.cleaned_data.get("last_name")

        if len(username) < 10:
            self.errors["last_name"] = self.error_class(
                [
                    "Minimum 10 characters required",
                    "am i joke to you",
                    "oh la la la..",
                ],
            )
        if self.cleaned_data.get(
            "marriage_day", datetime.date(2003, 12, 31)
        ) > datetime.date(2003, 12, 31):
            self.errors["marriage_day"] = self.error_class(
                [
                    "minor marriage not allowed.",
                    "marry before you.",
                ]
            )
            raise ValidationError("marriage minor men.")
        print(
            self.cleaned_data.get("marriage_day", datetime.date(2003, 12, 31)),
            datetime.date(2003, 12, 31),
            self.cleaned_data.get("marriage_day", datetime.date(2003, 12, 31))
            > datetime.date(2003, 12, 31),
        )
        return self.cleaned_data


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
