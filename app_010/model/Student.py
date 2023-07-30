from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse_lazy
from django.utils import timesince

import uuid


def student_standard_validator(value: int):
    if 0 < value < 13:
        return

    raise ValidationError(
        message="class room must between 1-12 only.",
        code="classroom error",
        params={"classroom": value},
    )


class StudentModel(models.Model):
    studentid = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4,
    )
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    standard = models.IntegerField(validators=(student_standard_validator,))
    section = models.CharField(max_length=1, default="A")
    dateofbirth = models.DateField()
    image = models.ImageField(null=True, blank=True)

    def age(self):
        return timesince.timesince(self.dateofbirth)

    def __str__(self) -> str:
        return (
            f"{self.firstname} {self.lastname}"
            f" [{self.standard}-{self.section.upper()}]"
        )

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:student-read", kwargs={"pk": self.pk})
