from django.db import models
from django.urls import reverse_lazy

from typing import Self


class DemoFKModel(models.Model):
    fkfield = models.CharField(max_length=100)

    def __str__(self: Self) -> str:
        return str(self.fkfield)

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:demofk-read", kwargs={"pk": self.pk})
