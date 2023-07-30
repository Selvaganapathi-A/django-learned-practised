from django.db import models
from django.urls import reverse_lazy

from . import CarBrand, CarFuelType


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(
        to=CarBrand.CarBrandModel, on_delete=models.PROTECT
    )
    fuel_type = models.ManyToManyField(to=CarFuelType.CarFuelTypeModel)

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:car-read", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.brand.name} - {self.name}"
