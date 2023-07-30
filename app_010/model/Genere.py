from django.db import models
from django.urls import reverse_lazy


class GenereModel(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Enter book genere (e.g. SciFi, Fiction, Anime etc.)",
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:genere-read", kwargs={"pk": self.pk})
