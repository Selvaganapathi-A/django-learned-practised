from django.urls import reverse_lazy
from django.db import models


class CarBrandModel(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:carbrand-read", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.name
