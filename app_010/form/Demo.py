from django import forms

from datetime import date
from pprint import pprint
from typing import Self

import json

from app_010.model.Demo import DemoModel


def printer(*args, **kwargs):
    pprint(args)
    pprint(kwargs)


class DemoForm(forms.ModelForm):
    """
    Demonstrate Form Fields in Django
    """

    delna = forms.CharField(
        max_length=10,
        min_length=8,
        empty_value="empty pussy,",
        widget=forms.widgets.TextInput(
            attrs={
                "type": "date",
                "class": "form-field",
            }
        ),
    )

    class Meta:
        model = DemoModel
        fields = "__all__"

    # date_field = forms.DateField(
    #     required=True,
    #     label="Enter Date of Last Week:(This is Label)",
    #     initial=date(1999, 12, 31),
    #     help_text="this is help text.",
    # )
    # char_field = forms.CharField(
    #     required=True,
    #     label="Enter Date of Last Week:(This is Label)",
    #     initial="hello Frenmy! :-(=)",
    #     help_text="this is help text.",
    # )

    def __init__(self: Self, *args, **options):
        super(DemoForm, self).__init__(*args, **options)
        # printer(args)
        # printer(options)

        # printer(model=getattr(options, "model", None))
        # printer(fields=getattr(options, "fields", None))
        # printer(exclude=getattr(options, "exclude", None))
        # printer(widgets=getattr(options, "widgets", None))
        # printer(localized_fields=getattr(options, "localized_fields", None))
        # printer(labels=getattr(options, "labels", None))
        # printer(help_texts=getattr(options, "help_texts", None))
        # printer(error_messages=getattr(options, "error_messages", None))
        # printer(field_classes=getattr(options, "field_classes", None))

        # visible_field: forms.Field
        # for visible_field in self.visible_fields():
        #     print(type(visible_field), visible_field)
