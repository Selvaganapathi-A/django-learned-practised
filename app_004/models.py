from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timesince

from typing import Self

import datetime
import os
import uuid

from dateutil import relativedelta

# Create your models here.


def min_age_validator(date_of_birth: datetime.date):
    if (
        relativedelta.relativedelta(date_of_birth, datetime.date.today()).years
        < 18
    ):
        raise ValidationError("You are not Child Anymore.")


def date_of_birth_validator(date_of_birth: datetime.date):
    print(relativedelta.relativedelta(date_of_birth, datetime.date.today()))
    if (
        relativedelta.relativedelta(date_of_birth, datetime.date.today()).years
        > 0
    ):
        raise ValidationError(
            "Cannot add Children born in Future .",
            params={
                "Birhday": date_of_birth,
            },
        )


class CalculateAge:
    @property
    def age(self):
        _age = relativedelta.relativedelta(
            datetime.date.today(),
            self.date_of_birth,  # type: ignore
        )
        return f"{_age.years} Years, {_age.months} Months."


class Student(models.Model):
    name = models.CharField(max_length=64)
    father_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(
        validators=[
            min_age_validator,
        ],
    )
    image = models.ImageField(upload_to="app_004/student/")
    student_id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )

    def __str__(self) -> str:
        return f"{self.date_of_birth:%Y-%m-%d} - {self.name} {self.father_name}"

    def age(self):
        return timesince.timesince(self.date_of_birth)



class Person(models.Model, CalculateAge):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, primary_key=True, unique=True
    )
    name = models.CharField(max_length=128)
    date_of_birth = models.DateField(
        validators=[
            date_of_birth_validator,
        ]
    )
