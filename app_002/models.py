from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    headline = models.CharField(max_length=128)
    content = models.TextField(max_length=3072)
    author = models.CharField(max_length=64)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.headline} - {self.author}"


class Author(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("app02:authordetailview", kwargs={"pk": self.pk})
