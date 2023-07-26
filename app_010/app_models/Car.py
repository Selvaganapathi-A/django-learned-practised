from django.db import models

from . import CarBrand, CarFuel


class CarModel(models.Model):
    brand = models.ForeignKey(
        to=CarBrand.CarBrandModel, on_delete=models.PROTECT
    )
    name = models.CharField(max_length=100)
    fuel_type = models.ManyToManyField(to=CarFuel.CarFuelTypeModel)

    def __str__(self) -> str:
        return f"{self.brand.name} - {self.name}"
