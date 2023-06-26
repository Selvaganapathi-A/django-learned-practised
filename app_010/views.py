from django.http import HttpRequest, request
from django.shortcuts import render

# Create your views here.


def index(req: HttpRequest):
    return render(
        request=req,
        template_name="app_010/index.html",
        context={
            "web_page_title": "App 010",
        },
    )
