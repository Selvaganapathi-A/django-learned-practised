from django.db import models
from django.urls import reverse_lazy

import uuid

from app_010.app_validators import model_validators


class AuthorModel(models.Model):
    social_security_number = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False
    )
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200, null=True, blank=True)
    contact = models.CharField(
        max_length=16,
        validators=(model_validators.mobile_number_validator,),
        help_text='Mobile Number in "+91-000-000-0000".',
    )

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:author-read", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
