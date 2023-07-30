from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone

from datetime import date, time, timedelta
from typing import Self

import decimal
import json
import re
import uuid

import pytz

from .DemoFK import DemoFKModel
from .DemoM2M import DemoM2MModel
from .DemoO2O import DemoO2OModel


"""
https://docs.djangoproject.com/en/4.2/ref/models/fields/
"""

INDIA = pytz.timezone("Asia/Calcutta")


def jsonify():
    return json.dumps(
        {
            "people": {
                "name": "rhino",
                "age": 20,
            }
        }
    )


def validator(value: str):
    if re.match(r"\d+", value):
        return
    raise ValidationError(
        "must be valid integer." " should'nt contain any other letter",
        code="regex error",
        params={
            "param": value,
        },
    )


class DemoModel(models.Model):
    # * -----------------------------------------------------------------* #
    # * - Auto Field
    # field_001 = models.AutoField()
    # field_005 = models.BigAutoField()
    small_auto_field = models.SmallAutoField(primary_key=True, editable=False)
    # * -----------------------------------------------------------------* #
    # * - BooleanField
    # ? widget = CheckboxInput
    boolean_field = models.BooleanField(default=True)
    # * -----------------------------------------------------------------* #
    # ? widget = 'UrlInput'
    url_field = models.URLField(default="https://www.example.com/?q=tree")
    # * -----------------------------------------------------------------* #
    # * - Single line text
    # ? widget = TextInput
    char_field_1 = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        name="DJango Academy",
        default="default dv1",
        help_text="helping you decide char field 1.😬😬😬",
        validators=(validator,),
        error_messages={
            "required": "should'nt be empty",
            "invalid": "invalid data",
        }
        # # ? Set as Primary key for this model
        # primary_key=True,
        # # ? Hides from rendering
        # # editable=False,
    )

    char_field_2 = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        choices=(
            ("robo", "vision"),
            ("software", "jarvis"),
            ("hardware", "ultron"),
        ),
    )
    char_field = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        choices=(
            (
                "audio",
                (
                    ("comprehensive", "Humans Can hear"),
                    ("incomprehensive", "Humans Cannot hear"),
                ),
            ),
            (
                "video",
                (
                    ("visible", "Humans Can See"),
                    ("invisible", "Humans Cannot See"),
                ),
            ),
            (
                "taste",
                (
                    ("bitter", "Unpleasent"),
                    ("sweet", "🍫🍫🍫"),
                ),
            ),
        ),
    )
    json_field = models.JSONField(default=jsonify)
    slug_field = models.SlugField(default="slug_field")
    email_field = models.EmailField(default="system@admin.bin")
    uuid_field = models.UUIDField(default=uuid.uuid4)
    # * -----------------------------------------------------------------* #
    # ? widget = 'TextInput'
    generic_ipaddress_field = models.GenericIPAddressField(
        default="192.168.43.1"
    )
    # * -----------------------------------------------------------------* #
    # * - Text Field
    # ? widget = 'TextArea'
    text_field = models.TextField(default="text field")
    # * -----------------------------------------------------------------* #
    # * - BinaryField
    binary_field = models.BinaryField(default=b"12186.co.in")
    # * -----------------------------------------------------------------* #
    #  * Date and Datetime
    # ? widget = DateInput
    # ! default = `datetime.date.today`
    # ! auto_now_add = updated when instace is created
    # ! auto_now = updated every time instace is saved
    date_field = models.DateField(default=date.today)
    # ? widget = DateTimeInput
    # ! default = `django.utils.timezone.now`
    datetime_field = models.DateTimeField(default=timezone.now)
    # ? widget = 'TimeInput'
    time_field = models.TimeField(default=time(23, 59, 58, 987654))
    # ! periods of time - modeled in Python by `timedelta`.
    duration_field = models.DurationField(
        default=timedelta(
            weeks=51,
            days=5,
            hours=23,
            minutes=57,
            seconds=46,
            milliseconds=454,
            microseconds=989,
        )
    )
    # * -----------------------------------------------------------------* #
    # * - Integer Field
    # ? widget = NumberInput
    big_integer_field = models.BigIntegerField(blank=True, null=True)
    positive_big_integer_field = models.PositiveBigIntegerField(
        blank=True, null=True
    )
    integer_field = models.IntegerField(blank=True, null=True)
    positive_integer_field = models.PositiveIntegerField(blank=True, null=True)
    small_integer_field = models.SmallIntegerField(blank=True, null=True)
    positive_small_integer_field = models.PositiveSmallIntegerField(
        blank=True, null=True
    )
    float_field = models.FloatField(blank=True, null=True)
    # * -----------------------------------------------------------------* #
    # * Decimal
    # ? widget = 'NumberInput' when localize is False or 'TextInput' otherwise.
    decimal_field = models.DecimalField(
        decimal_places=10,
        max_digits=15,
        default=decimal.Decimal(13),
        blank=True,
        null=True,
    )
    # * -----------------------------------------------------------------* #
    #
    file_field = models.FileField(
        upload_to="app10/demo_file/", blank=True, null=True
    )
    filepath_field = models.FilePathField(
        path=r"E:/App/Organisation/files/media/app10/",
        recursive=True,
        blank=True,
        null=True,
    )
    # ? ClearableFileInput.
    image_field = models.ImageField(
        upload_to="app10/images/", blank=True, null=True
    )
    # * -----------------------------------------------------------------* #
    # Relationship Fields
    m2m_field = models.ManyToManyField(
        to=DemoM2MModel,
    )
    fk_field = models.ForeignKey(
        to=DemoFKModel, on_delete=models.SET_NULL, null=True
    )
    o2o_field = models.OneToOneField(
        to=DemoO2OModel, on_delete=models.SET_NULL, null=True
    )
    # * ---------------------------------------------------------------- * #

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:demo-read", kwargs={"pk": self.pk})

    def __str__(self: Self) -> str:
        return str(self.pk)
