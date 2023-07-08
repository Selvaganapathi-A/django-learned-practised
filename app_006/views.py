from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.


def index(req: HttpRequest):
    return render(
        request=req,
        template_name="app_006/index.html",
        context={
            "web_page_title": "App 006",
        },
    )
