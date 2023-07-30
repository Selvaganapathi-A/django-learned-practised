from django.db import models
from django.urls import reverse_lazy


class ToppingModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:topping-read", kwargs={"pk": self.pk})
