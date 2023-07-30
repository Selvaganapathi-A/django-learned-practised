from django.db import models
from django.urls import reverse_lazy


class TagModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:tag-read", kwargs={"pk": self.pk})
