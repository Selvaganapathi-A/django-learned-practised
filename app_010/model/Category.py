from django.db import models
from django.urls import reverse_lazy


class CategoryModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:category-read", kwargs={"pk": self.pk})
