from django.db import models

from . import Topping


class PizzaModel(models.Model):
    name = models.CharField(max_length=100)
    toppings = models.ManyToManyField(
        to=Topping.ToppingModel,
    )

    def __str__(self) -> str:
        return self.name
