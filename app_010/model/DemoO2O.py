from django.db import models
from django.urls import reverse_lazy

from typing import Self


class DemoO2OModel(models.Model):
    o2ofield = models.CharField(max_length=100)

    def __str__(self: Self) -> str:
        return str(self.o2ofield)

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:demoo2o-read", kwargs={"pk": self.pk})
