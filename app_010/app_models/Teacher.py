from django.db import models


class TeacherModel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
