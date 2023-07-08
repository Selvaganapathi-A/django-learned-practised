from django import forms


class WidgetExample(forms.Form):
    # *** Widgets
    # Handling Text Inputs
    TextInput = forms.CharField(
        required=False,
        widget=forms.widgets.TextInput(attrs={"class": "form-field"}),
    )
    NumberInput = forms.CharField(
        required=False,
        widget=forms.widgets.NumberInput(attrs={"class": "form-field"}),
    )
    EmailInput = forms.CharField(
        required=False,
        widget=forms.widgets.EmailInput(attrs={"class": "form-field"}),
    )
    URLInput = forms.CharField(
        required=False,
        widget=forms.widgets.URLInput(attrs={"class": "form-field"}),
    )
    PasswordInput = forms.CharField(
        required=False,
        widget=forms.widgets.PasswordInput(attrs={"class": "form-field"}),
    )
    HiddenInput = forms.CharField(
        required=False,
        widget=forms.widgets.HiddenInput(attrs={"class": "form-field"}),
    )
    DateInput = forms.CharField(
        required=False,
        widget=forms.widgets.DateInput(attrs={"class": "form-field"}),
    )
    DateTimeInput = forms.CharField(
        required=False,
        widget=forms.widgets.DateTimeInput(attrs={"class": "form-field"}),
    )
    TimeInput = forms.CharField(
        required=False,
        widget=forms.widgets.TimeInput(attrs={"class": "form-field"}),
    )
    Textarea = forms.CharField(
        required=False,
        widget=forms.widgets.Textarea(attrs={"class": "form-field"}),
    )
    # ! -------------------------------------------------------------------- ! #
    CheckboxInput = forms.CharField(
        required=False,
        widget=forms.widgets.CheckboxInput(attrs={"class": "form-field"}),
    )

    Select = forms.CharField(
        widget=forms.widgets.Select(
            attrs={
                "class": "form-field",
            },
            choices=(
                ("paul", "Paul"),
                ("bethany", "Bethany"),
            ),
        )
    )
    # Select = forms.CharField(
    #     required=False,
    #     widget=forms.widgets.Select(attrs={"class": "form-field"}),
    # )
    NullBooleanSelect = forms.NullBooleanField(
        required=False,
        widget=forms.widgets.NullBooleanSelect(
            attrs={"class": "form-field"},
        ),
    )

    RadioSelect = forms.CharField(
        required=False,
        widget=forms.widgets.RadioSelect(
            attrs={"class": "form-field"},
            choices=(
                ("paul", "Paul"),
                ("bethany", "Bethany"),
            ),
        ),
    )
    SelectMultiple = forms.CharField(
        required=False,
        widget=forms.widgets.SelectMultiple(
            attrs={"class": "form-field"},
            choices=(
                ("paul", "Paul"),
                ("bethany", "Bethany"),
            ),
        ),
    )
    CheckboxSelectMultiple = forms.CharField(
        required=False,
        widget=forms.widgets.CheckboxSelectMultiple(
            attrs={"class": "form-field"},
            choices=(
                ("paul", "Paul"),
                ("bethany", "Bethany"),
            ),
        ),
    )
    # ! -------------------------------------------------------------------- ! #
    ClearableFileInput = forms.CharField(
        required=False,
        widget=forms.widgets.ClearableFileInput(attrs={"class": "form-field"}),
    )

    FileInput = forms.CharField(
        required=False,
        widget=forms.widgets.FileInput(attrs={"class": "form-field"}),
    )

    # ! -------------------------------------------------------------------- ! #

    MultipleHiddenInput = forms.CharField(
        required=False,
        widget=forms.widgets.MultipleHiddenInput(attrs={"class": "form-field"}),
    )
    SplitDateTimeWidget = forms.CharField(
        required=False,
        widget=forms.widgets.SplitDateTimeWidget(attrs={"class": "form-field"}),
    )
    SplitHiddenDateTimeWidget = forms.CharField(
        required=False,
        widget=forms.widgets.SplitHiddenDateTimeWidget(
            attrs={"class": "form-field"}
        ),
    )
    SelectDateWidget = forms.CharField(
        required=False,
        widget=forms.widgets.SelectDateWidget(
            attrs={"class": "form-field"},
            years=(1990, 1991, 1993, 1994, 1996, 1997, 1999, 2000),
            months={1: "9", 2: "10", 3: "11", 5: "12", 6: "13", 12: "15"},
        ),
    )
    # # ! ------------------------------------------------------------------ ! #

    # MultiWidget = forms.CharField(
    #     required=False,
    #     widget=forms.widgets.MultiWidget(
    #         widgets=(forms.widgets.TextInput(), forms.widgets.TextInput())
    #     ),
    # )


class HTMLWidgetExample(forms.Form):
    search_input = forms.CharField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "search",
            }
        ),
        required=False,
    )
    # ! -------------------------------------------------------------------- ! #
    checkbox_input = forms.CharField(
        widget=forms.widgets.CheckboxInput(
            attrs={
                "class": "form-field",
                "type": "checkbox",
            }
        ),
        required=False,
    )
    checkbox_input_select_multiple = forms.CharField(
        widget=forms.widgets.CheckboxSelectMultiple(
            attrs={
                "class": "form-field",
                "type": "checkbox",
            },
            choices=(
                ("thor", "Thor Odinson"),
                ("tony", "Tony Stink"),
                ("strange", "I ain't Stange."),
            ),
        ),
        required=False,
    )
    radio_input = forms.CharField(
        widget=forms.widgets.RadioSelect(
            attrs={
                "class": "form-field",
                "type": "radio",
            },
            choices=(
                ("jarvis", "AI-1 Jarvis"),
                ("ultron", "AI-2 Ultron"),
                ("vision", "AI-3 Vision"),
            ),
        ),
        required=False,
    )
    range_input = forms.IntegerField(
        min_value=-50,
        max_value=150,
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "range",
                "step": "4",
            }
        ),
        required=False,
    )
    # ! -------------------------------------------------------------------- ! #
    file_input = forms.FileField(
        widget=forms.widgets.FileInput(
            attrs={
                "class": "form-field",
                "type": "file",
            }
        ),
        required=False,
    )
    # ! -------------------------------------------------------------------- ! #
    color_input = forms.CharField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "color",
            }
        ),
        required=False,
    )
    hidden_input = forms.CharField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "hidden",
                "value": "hidde-text-xyz-abc",
            }
        ),
        required=False,
    )
    password_input = forms.CharField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "password",
            }
        ),
        required=False,
    )
    # ! -------------------------------------------------------------------- ! #
    number_input = forms.IntegerField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "number",
            }
        ),
        required=False,
    )
    tel_input = forms.CharField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "tel",
            }
        ),
        required=False,
    )
    # ! -------------------------------------------------------------------- ! #
    text_input = forms.CharField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "text",
            }
        ),
        required=False,
    )
    email_input = forms.EmailField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "email",
            }
        ),
        required=False,
    )
    url_input = forms.URLField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "url",
            }
        ),
        required=False,
    )
    # ! -------------------------------------------------------------------- ! #
    date_input = forms.DateField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "date",
            }
        ),
        required=False,
    )
    time_input = forms.TimeField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "time",
            }
        ),
        required=False,
    )
    week_input = forms.CharField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "week",
            }
        ),
        required=False,
    )
    month_input = forms.CharField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "month",
            }
        ),
        required=False,
    )
    # ! -------------------------------------------------------------------- ! #
    reset_input = forms.CharField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "reset",
            }
        ),
        required=False,
    )
    submit_input = forms.CharField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "submit",
            }
        ),
        required=False,
    )
    button_input = forms.CharField(
        widget=forms.widgets.Input(
            attrs={"class": "form-field", "type": "button", "value": "GPT-27"}
        ),
        required=False,
    )
    image_submit = forms.ImageField(
        widget=forms.widgets.Input(
            attrs={
                "class": "form-field",
                "type": "image",
            }
        ),
        required=False,
    )
    # ! -------------------------------------------------------------------- ! #
    pass
