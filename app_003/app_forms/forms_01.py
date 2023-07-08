from django import forms

import datetime
import decimal
import json
import uuid

# from django.forms import widgets

# from django.conf import settings


class FormExample(forms.Form):
    jsonfield = forms.JSONField(
        initial=json.dumps({1: 7, 2: 8, 3: 9, 4: {"a": 1, "b": "c"}})
    )

    genericipaddressfield = forms.GenericIPAddressField(initial="192.168.2.1")
    regexfield = forms.RegexField(
        r"^\d+$",
        error_messages={
            "invalid": (
                "Enter natural numbers only. like, '1234567' not floats or any"
                " other numbers."
            ),
            "required": "You Cannont leave me alone",
        },
    )
    charfield = forms.CharField(initial="enter some character")
    slugfield = forms.SlugField(initial="initial_slug")
    emailfield = forms.EmailField(initial="yourname@serviceprovider.domain")
    urlfield = forms.URLField(initial="https://yourdomain.type")

    datefield = forms.DateField(initial=datetime.date(1999, 12, 31))
    datetimefield = forms.DateTimeField(
        initial=datetime.datetime(
            1999,
            12,
            31,
            23,
            59,
            59,
            0,
            datetime.timezone(
                datetime.timedelta(hours=5, minutes=30), "Asia/Calcutta"
            ),
        )
    )
    timefield = forms.TimeField(initial=datetime.time(23, 59, 59))
    durationfield = forms.DurationField(
        initial=datetime.timedelta(
            weeks=53,
            days=7,
            hours=23,
            minutes=59,
            seconds=59,
            milliseconds=999,
            microseconds=999,
        )
    )

    filefield = forms.FileField(required=False)
    filepathfield = forms.FilePathField(
        path="index",
        required=False,
        recursive=True,
        allow_folders=True,
        # match="*.py",
    )
    imagefield = forms.ImageField(required=False)

    floatfield = forms.FloatField(initial=34.567)
    decimalfield = forms.DecimalField(
        initial=decimal.Decimal(9999.50),
        max_digits=10,
        decimal_places=2,
        min_value=1,
    )
    integerfield = forms.IntegerField(
        initial=3423,
    )

    nullbooleanfield = forms.NullBooleanField(
        initial=None,
    )
    choicefield = forms.ChoiceField(
        choices=(
            ("mars", "Mars-Probably had life in past"),
            ("earth", "Earth-Planet"),
            ("titan", "Titan-Moon of Jupiter"),
        ),
    )
    typedchoicefield = forms.TypedChoiceField(
        initial="arctorus",
        choices=(
            ("polaris", "Polaris"),
            ("anubis", "Aubis"),
            ("sirius", "Sirius"),
            ("sun", "Sun"),
            ("jupiter", "Jupiter"),
        ),
    )
    multiplechoicefield = forms.MultipleChoiceField(
        initial=("polaris", "sun", "sirius"),
        choices=(
            ("polaris", "Polaris"),
            ("anubis", "Aubis"),
            ("sirius", "Sirius"),
            ("sun", "Sun"),
            ("jupiter", "Jupiter"),
        ),
    )
    typedmultiplechoicefield = forms.TypedMultipleChoiceField(
        initial=("jupiter", "anubis"),
        choices=(
            ("polaris", "Polaris"),
            ("anubis", "Aubis"),
            ("sirius", "Sirius"),
            ("sun", "Sun"),
            ("jupiter", "Jupiter"),
        ),
    )
    uuidfield = forms.UUIDField(
        initial=uuid.uuid4,
    )

    booleanfield = forms.BooleanField(
        initial=True,
    )

    # * Complex field
    # combofield =  forms.ComboField(,)
    # multivaluefield =  forms.MultiValueField(,)
    # splitdatetimefield =  forms.SplitDateTimeField(,)

    # * Model Relationship
    # modelchoicefield =  forms.ModelChoiceField(,)
    # modelmultiplechoicefield =  forms.ModelMultipleChoiceField(,)


# # -
# print("# -")

# for i, field in enumerate(sorted(vars(forms))):
#     if field.endswith("Field"):
#         print(f" {(field.lower() + '_').ljust(32, 'a')} =  forms.{field}()")

# print("# -")
# # -

# -
# print("# -")


# for i, field in enumerate(sorted(vars(widgets))):
#     if field.startswith("_"):
#         continue
#     print(
#         f" {field} = forms.CharField(required=False,"
#         f" widget=forms.widgets.{field}())"
#     )

# print("# -")
