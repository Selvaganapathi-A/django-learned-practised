from django.db import models
from django.db.models.functions import Lower
from django.urls import reverse_lazy

from datetime import date, datetime

import functools
import os

from .Author import AuthorModel
from .Genere import GenereModel
from .Language import LanguageModel


def custom_upload_dir(instance, filename, path_to_save: str):
    filename = instance.isbn + os.path.splitext(filename)[-1]
    return os.path.join(path_to_save, filename)


class BookModel(models.Model):
    # Metadata
    class Meta:
        db_table = "app10_book"
        get_latest_by = ["date_pulished", "date_added"]
        # order_with_respect_to = "author"
        ordering = (
            models.F("author__name").asc(nulls_last=True),
            models.F("title").asc(nulls_last=True),
        )
        indexes = (
            models.Index(Lower("title").asc(), name="index_title"),
            models.Index(
                fields=("author", "-date_published"),
                name="index_author_pub_date",
            ),
            models.Index(fields=("-date_added",), name="index_date_added"),
        )
        unique_together = ("title", "edition", "author")
        constraints = (
            models.CheckConstraint(
                check=models.Q(date_published__lte=date.today()),
                name="pub_date_validator",
                violation_error_message=(
                    "You're not Time Traveller to publish book in future and"
                    " add it in the past. you Cannot Create PARADOX. Violation"
                    " of Time"
                ),
            ),
            models.CheckConstraint(
                check=models.Q(pages__gte=25),
                name="min_page_validator",
                violation_error_message="Book contain atleast 25 pages.",
            ),
        )
        verbose_name = "BoOk"
        verbose_name_plural = "bOoKs"

    # Fields
    isbn = models.CharField(
        max_length=13, help_text="ISBN Number.", unique=True
    )
    title = models.CharField(max_length=256)
    edition = models.PositiveSmallIntegerField()
    author = models.ForeignKey(
        to=AuthorModel, on_delete=models.SET_NULL, null=True
    )
    language = models.ForeignKey(to=LanguageModel, on_delete=models.RESTRICT)
    genere = models.ManyToManyField(
        to=GenereModel, help_text="Select Genere for this Book."
    )
    pages = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    date_published = models.DateField()
    cover_image = models.ImageField(
        upload_to=functools.partial(
            custom_upload_dir, path_to_save="app10/book/cover_image/"
        ),
        blank=True,
        null=True,
    )

    def get_absolute_url(self) -> str:
        return reverse_lazy("app10:book-read", kwargs={"pk": self.pk})


    def __str__(self) -> str:
        return f"{self.title} added {self.date_added:%Y-%m-%d}."
