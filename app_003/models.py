from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone

import datetime
import functools
import os
import re
import uuid

import pytz

# Create your models here.

"""
one to one relationship example.
"""


def current_month_start():
    current_date = datetime.date.today()
    india = pytz.timezone("Asia/Calcutta")
    return datetime.datetime(
        current_date.year, current_date.month, 1, 0, 0, 0, tzinfo=india
    )


def custom_upload_dir(instance, filename, path_to_save: str):
    filename = instance.isbn + os.path.splitext(filename)[-1]
    return os.path.join(path_to_save, filename)


def mobile_number_validator(value: str):
    if not re.match(r"^\+91\-[9876]\d{2}\-\d{3}\-\d{4}$", value):
        raise ValidationError(
            "provide '+91-000-000-0000' in this format.",
            params={"value": value},
        )


class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)
    mobile = models.CharField(
        max_length=16,
        validators=[mobile_number_validator],
        help_text='Mobile Number in "+91-000-000-0000".',
    )
    email = models.EmailField()

    def get_absolute_url(self):
        return reverse_lazy("app03:author-detail", kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return f"{self.name}"


class Book(models.Model):
    class Meta:
        db_table = "app_03_book"
        get_latest_by = ["date_published", "_date_created"]
        # *** order_with_respect_to = "author"
        ordering = (
            models.F("author__name").asc(nulls_last=True),
            models.F("title").asc(nulls_last=True),
        )
        indexes = [
            models.Index(
                fields=["title", "isbn", "edition"],
                name="custom_index",
            ),
        ]
        unique_together = ["title", "edition", "author"]
        constraints = [
            models.CheckConstraint(
                check=models.Q(pages__gte=10),
                name="must contain atleast 10 pages.",
            ),
            models.CheckConstraint(
                check=models.Q(date_published__lte=current_month_start()),
                name="must be published before a month.",
            ),
        ]
        verbose_name = "Book"
        verbose_name_plural = "Books"
        unique_together = [
            ("title", "edition", "author"),
        ]

    isbn = models.UUIDField(
        default=uuid.uuid4, primary_key=True, auto_created=True, editable=False
    )
    title = models.CharField(max_length=128)
    edition = models.IntegerField(default=1)
    pages = models.IntegerField(default=0)
    language = models.CharField(max_length=64)
    date_published = models.DateTimeField(default=timezone.now, validators=[])
    cover_image = models.ImageField(
        upload_to=functools.partial(
            custom_upload_dir,
            path_to_save="app_003/book-cover/",
        ),
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        related_name="books",
    )
    _date_created = models.DateTimeField(
        auto_now_add=True
    )  # Added when object is created
    _date_modified = models.DateTimeField(auto_now=True)  # Everytime updated


if __name__ == "__main__":
    # ~bash:  Book.objects.all()
    # <QuerySet [<Book: Book object (d5d2417c-f561-41d3-81b9-d1590a507313)>, <Book: Book object (52ca1431-4e65-498f-beae-7279bfc82ec3)>, <Book: Book object (54231e6e-59a8-4d96-b2d9-2a845faf8d1e)>, <Book: Book object (f567d5c1-126c-4315-ac21-ed4ca6eb8b9b)>, <Book: Book object (17d60cd7-51cf-475a-b6b2-0682bd541829)>, <Book: Book object (42dd7e21-62ba-46e1-9ddf-c52e330323e4)>, <Book: Book object (2a6fbd46-f778-469b-8043-59d6926a934e)>]>  # noqa: E501

    # ~bash:  Author.objects.all()
    # <QuerySet [<Author: <Author> : Ramya>, <Author: <Author> : Michel>, <Author: <Author> : Ramsey>, <Author: <Author> : Cassandra>, <Author: <Author> : Paul>]># noqa: E501

    # ~bash:  Author.objects.filter(name='Ramya')
    # <QuerySet [<Author: <Author> : Ramya>]>

    # ~bash:  for author in Author.objects.filter(name='Ramya'):
    #             print(author.name)
    #
    # Ramya

    # ~bash:  Author.objects.get(name='Ramya')
    # <Author: <Author> : Ramya>

    # ~bash:  ramya = Author.objects.get(name='Ramya')

    # ~bash:  ramya.book_set
    # <django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x0000019F033D8ED0> # noqa: E501

    # ~bash:  ramya.book_set.all()
    # <QuerySet [<Book: Book object (d5d2417c-f561-41d3-81b9-d1590a507313)>, <Book: Book object (42dd7e21-62ba-46e1-9ddf-c52e330323e4)>, <Book: Book object (2a6fbd46-f778-469b-8043-59d6926a934e)>]> # noqa: E501

    # ~bash:  for book in ramya.book_set.all():
    # ~bash:  for book in ramya.books.all():
    #             print(book.title)
    #             print(book.isbn)
    #             print(book.language)
    #             print()
    #
    # Eye sight
    # d5d2417c-f561-41d3-81b9-d1590a507313
    # Hindi

    # Quantum of Solace
    # 42dd7e21-62ba-46e1-9ddf-c52e330323e4
    # English

    # Maxim's Primer
    # 2a6fbd46-f778-469b-8043-59d6926a934e
    # English

    # ~bash:  ramya.book_set.filter(language="English")
    # <QuerySet [<Book: Book object (42dd7e21-62ba-46e1-9ddf-c52e330323e4)>, <Book: Book object (2a6fbd46-f778-469b-8043-59d6926a934e)>]> # noqa: E501

    # ~bash:  for book in ramya.book_set.all():
    #             print(book.title)
    #             print(book.isbn)
    #             print(book.language)
    #             print()
    #
    # Eye sight
    # d5d2417c-f561-41d3-81b9-d1590a507313
    # Hindi

    # Quantum of Solace
    # 42dd7e21-62ba-46e1-9ddf-c52e330323e4
    # English

    # Maxim's Primer
    # 2a6fbd46-f778-469b-8043-59d6926a934e
    # English

    # ~bash:  for book in ramya.book_set.filter(language='English'):
    #             print(book.title)
    #             print(book.isbn)
    #             print(book.language)
    #             print()
    #
    # Quantum of Solace
    # 42dd7e21-62ba-46e1-9ddf-c52e330323e4
    # English

    # Maxim's Primer
    # 2a6fbd46-f778-469b-8043-59d6926a934e
    # English
    pass
