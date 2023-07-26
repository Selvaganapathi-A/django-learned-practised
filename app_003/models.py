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
