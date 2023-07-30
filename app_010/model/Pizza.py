from django.db import models
from django.urls import reverse_lazy

from . import Topping


class PizzaModel(models.Model):
    name = models.CharField(max_length=100)
    toppings = models.ManyToManyField(
        to=Topping.ToppingModel, related_name="pizza"
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:pizza-read", kwargs={"pk": self.pk})
