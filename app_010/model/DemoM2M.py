from django.db import models
from django.urls import reverse_lazy

from typing import Self


class DemoM2MModel(models.Model):
    m2mfield = models.CharField(max_length=100)

    def __str__(self: Self) -> str:
        return str(self.m2mfield)

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:demom2m-read", kwargs={"pk": self.pk})
