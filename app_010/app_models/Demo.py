from django.db import models
from django.utils import timezone

from datetime import date, time, timedelta

import decimal
import json
import uuid

import pytz


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


class DemoModelFK(models.Model):
    fkfield = models.CharField(max_length=100)


class DemoModelM2M(models.Model):
    m2mfield = models.CharField(max_length=100)


class DemoModelO2O(models.Model):
    o2ofield = models.CharField(max_length=100)


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
    email_field = models.EmailField(default="system@admin.bin")
    # * -----------------------------------------------------------------* #
    # * - Single line text
    # ? widget = TextInput
    char_field = models.CharField(max_length=100)

    json_field = models.JSONField(default=jsonify)
    slug_field = models.SlugField(default="slug_field")
    # ? widget = 'UrlInput'
    url_field = models.URLField(default="https://www.example.com/?q=tree")
    uuid_field = models.UUIDField(default=uuid.uuid4)
    # ? widget = 'TextInput'
    generic_ipaddress_field = models.GenericIPAddressField(
        default="192.168.43.1:8000"
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
    big_integer_field = models.BigIntegerField()
    positive_big_integer_field = models.PositiveBigIntegerField()
    integer_field = models.IntegerField()
    positive_integer_field = models.PositiveIntegerField()
    small_integer_field = models.SmallIntegerField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    float_field = models.FloatField()
    # * -----------------------------------------------------------------* #
    # * Decimal
    # ? widget = 'NumberInput' when localize is False or 'TextInput' otherwise.
    decimal_field = models.DecimalField(
        decimal_places=9, max_digits=30, default=decimal.Decimal(65.776)
    )
    # * -----------------------------------------------------------------* #
    #
    file_field = models.FileField(upload_to="app10/demo_file/")
    filepath_field = models.FilePathField(path="D:/Common/Pictures/Cook Ware/")
    # ? ClearableFileInput.
    image_field = models.ImageField(upload_to="app10/demo_image/")
    # * -----------------------------------------------------------------* #
    # Relationship Fields
    m2m_field = models.ManyToManyField(
        to=DemoModelM2M,
    )
    fk_field = models.ForeignKey(
        to=DemoModelFK, on_delete=models.SET_NULL, null=True
    )
    o2o_field = models.OneToOneField(
        to=DemoModelO2O,
        on_delete=models.SET_NULL,
        null=True,
    )
    # * ---------------------------------------------------------------- * #
