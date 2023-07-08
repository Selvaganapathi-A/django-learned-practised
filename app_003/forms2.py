from django import forms

from . import models

"""

for details refer:-
    1) https://stackoverflow.com/questions/15348007/djangos-modelform-where-is-the-list-of-meta-options
    2) https://ordinarycoders.com/blog/article/using-django-form-fields-and-widgets

"""


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
                "Author Name Should not include Iniitials, Father name and Family Names.\nblah"
                " blah...."
            ),
            "email": "valid email id.",
        }


class Person(forms.Form):
    first_name = forms.CharField(max_length=64, min_length=2, initial="Your Name.")
    last_name = forms.CharField(
        max_length=64,
        initial="Family Name, Father name or Initial.",
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
        error_messages={
            "invalid": "Enter a valid value",
            "required": "You have to have this.",
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

    birth_day = forms.DateField(
        error_messages={
            "required": "",
        }
    )

    birth_year = forms.DateField(
        widget=forms.widgets.SelectDateWidget(
            years=(
                1980,
                1990,
                2000,
                2010,
            )
        )
    )

    school_joined = forms.DateField(
        widget=forms.widgets.NumberInput(
            attrs={"type": "date"},
        ),
    )

    income_per_year = forms.DecimalField(
        min_value=0,
        max_value=1_000_000_000,
        widget=forms.widgets.NumberInput(
            attrs={
                "value": 90_000,
                "step": 100,
            }
        ),
        initial=5_999,
    )

    def __init__(self, *args, **kwargs) -> None:
        self.label_suffix = ""
        super().__init__(**kwargs)
        # super(Person, self).__init__(*args, **kwargs)

    #     print("args", args)
    #     print("kwargs", kwargs)

    #     for k, v in self.fields.items():
    #         print(k, ":", v.error_messages)
    pass
