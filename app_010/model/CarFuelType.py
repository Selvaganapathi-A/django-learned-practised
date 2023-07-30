from django.db import models
from django.urls import reverse_lazy


class CarFuelTypeModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:carfueltype-read", kwargs={"pk": self.pk})
