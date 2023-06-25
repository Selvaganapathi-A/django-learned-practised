from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.


def index(req: HttpRequest):
    return render(
        request=req,
        template_name="app_002/index.html",
        context={
            "web_page_title": "App __2",
        },
    )


def register(req: HttpRequest):
    if req.method == "POST":
        items = req.POST.items()
        print(tuple(items))
    return render(
        request=req,
        template_name="app_002/user register.html",
        context={
            "web_page_title": "User Registration",
        },
    )
