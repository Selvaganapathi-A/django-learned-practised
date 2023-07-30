from django.db import models
from django.urls import reverse_lazy
from django.utils import timesince


class PersonModel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    dateofbirth = models.DateField(max_length=100)
    social_security_number = models.CharField(max_length=19)
    placeofbirth = models.CharField(max_length=200)
    gender = models.CharField(
        max_length=1,
        choices=(
            ("m", "Male"),
            ("f", "Female"),
            ("o", "Others"),
        ),
    )
    email = models.EmailField()
    occupation = models.CharField(max_length=50)
    income_per_year = models.PositiveIntegerField()
    bio = models.TextField(max_length=1000)
    image = models.ImageField(
        upload_to="app_010/person_image/", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname} {self.age} old"

    @property
    def age(self) -> str:
        return timesince.timesince(self.dateofbirth)

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:person-read", kwargs={"pk": self.pk})
