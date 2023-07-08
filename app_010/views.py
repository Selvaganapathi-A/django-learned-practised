from django.core.paginator import Page, Paginator
from django.db.models import F, Q
from django.http import HttpRequest
from django.shortcuts import render

from typing import Iterable

import uuid

from . import models

# Create your views here.


def index(req: HttpRequest):
    return render(
        request=req,
        template_name="app_010/index.html",
        context={
            "web_page_title": "App 010",
        },
    )


def author_list(req: HttpRequest):
    authors: Iterable[models.Author] = models.Author.objects.all().order_by(
        "first_name",
        "last_name",
    )
    paginator = Paginator(authors, per_page=10)
    return render(
        request=req,
        template_name="app_010/authors/author-list.html",
        context={
            "web_page_title": "Authors",
            "objects": authors,
        },
    )


def author_detail(req: HttpRequest, pk: uuid.UUID):
    author: models.Author = models.Author.objects.get(id=pk)

    return render(
        request=req,
        template_name="app_010/authors/author-detail.html",
        context={
            "web_page_title": "Author - " + author.first_name,
            "object": author,
        },
    )
