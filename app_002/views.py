from django.http import HttpRequest
from django.shortcuts import render

from . import models

# Create your views here.


def index(req: HttpRequest):
    # from lorem_text import lorem

    # for _ in range(108):
    #     article = models.Article(
    #         **{
    #             "headline": lorem.words(2).title(),
    #             "content": lorem.paragraphs(5),
    #             "author": lorem.words(1).capitalize(),
    #         }
    #     )

    #     article.save()

    return render(
        request=req,
        template_name="app_002/index.html",
        context={
            "web_page_title": "Class Views",
        },
    )
