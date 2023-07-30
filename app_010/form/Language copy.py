from django.db import models


class LanguageModel(models.Model):
    name = models.CharField(
        max_length=100,
        help_text=(
            "Enter books natural language (e.g. Tamil, Greek, Latin, etc.)"
        ),
    )

    def __str__(self) -> str:
        return self.name
