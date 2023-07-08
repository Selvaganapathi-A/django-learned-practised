from django.db import models
from django.urls import reverse

from . import validators

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)
    contact = models.CharField(
        max_length=16,
        validators=(validators.mobile_number_validator,),
        help_text='Mobile Number in "+91-000-000-0000".',
    )

    def get_absolute_url(self):
        return reverse("app02:author-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.name}"


class Article(models.Model):
    headline = models.CharField(max_length=128)
    content = models.TextField(max_length=3072)
    author = models.ForeignKey(
        to=Author, on_delete=models.CASCADE, to_field="name"
    )
    date_posted = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("app02:article-detail", kwargs={"pk": self.pk})
