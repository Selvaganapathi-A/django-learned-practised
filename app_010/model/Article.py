from django.db import models
from django.urls import reverse_lazy

from .Author import AuthorModel


class ArticleModel(models.Model):
    headline = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(
        to=AuthorModel,
        on_delete=models.RESTRICT,
        to_field="social_security_number",
        related_name="ssn",
    )
    date_posted = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:article-read", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.headline
