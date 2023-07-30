from django.db import models


class GenereModel(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Enter book genere (e.g. SciFi, Fiction, Anime etc.)",
    )

    def __str__(self) -> str:
        return self.name
