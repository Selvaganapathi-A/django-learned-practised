from django.db import models
from django.urls import reverse_lazy


class TeacherModel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:teacher-read", kwargs={"pk": self.pk})
