from django.db import models
from django.urls import reverse_lazy


class LanguageModel(models.Model):
    name = models.CharField(
        max_length=100,
        help_text=(
            "Enter books natural language (e.g. Tamil, Greek, Latin, etc.)"
        ),
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:language-read", kwargs={"pk": self.pk})
