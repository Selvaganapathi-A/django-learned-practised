from django.db import models
from django.utils import timesince

from . import validators

# Create your models here.


class MobileNumber(models.Model):
    mobile_number = models.CharField(
        max_length=12,
        validators=(validators.mobile_number_validator,),
        help_text="`000 000 0000`. Enter like this!",
    )

    def __str__(self) -> str:
        return f"{self.mobile_number}"


class Email(models.Model):
    email_address = models.EmailField(max_length=100)

    def __str__(self) -> str:
        return f"{self.email_address}"


class Address(models.Model):
    AddressLine1 = models.CharField(max_length=100)
    AddressLine2 = models.CharField(max_length=100, blank=True, null=True)
    Street = models.CharField(max_length=100)
    Village = models.CharField(max_length=100, blank=True, null=True)
    Taluk = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    PostalCode = models.CharField(
        max_length=7, validators=(validators.postal_code_validator,)
    )


class GenderChoices(models.Choices):
    Male = "Male--"
    Female = "Female"
    Other = "Other-"


class Person(models.Model):
    person_id = models.BigAutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    phone_number = models.OneToOneField(
        to=MobileNumber, on_delete=models.CASCADE
    )
    email = models.ManyToManyField(to=Email, blank=True)
    address = models.ForeignKey(to=Address, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=25)
    occupation = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    profile_image = models.ImageField(
        upload_to="app_010/profile_images/", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        return timesince.timesince(self.date_of_birth)
