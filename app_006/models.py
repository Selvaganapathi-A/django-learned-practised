from django.db import models
from django.utils import timesince


# Create your models here.


class Teacher(models.Model):
    firstname = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"Teacher : {self.firstname} {self.surname}"


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    dateofbirth = models.DateField()
    classroom = models.IntegerField(
        choices=(
            (1, "1"),
            (2, "2"),
            (3, "3"),
            (4, "4"),
            (5, "5"),
            (6, "6"),
            (7, "7"),
            (8, "8"),
        )
    )
    teacher = models.CharField(max_length=100)

    def __str__(self):
        # print(vars(self))
        return f"Student : {self.firstname} {self.surname}"

    def age(self):
        return timesince.timesince(self.dateofbirth)
