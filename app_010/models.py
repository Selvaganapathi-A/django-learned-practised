import datetime
import uuid

from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone

# Create your models here.


class Author(models.Model):
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid.uuid4,
        editable=False,
        auto_created=True,
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(validators=[])

    def get_absolute_url(self):
        return reverse_lazy("app10:author-detail", kwargs={"pk": self.pk})
