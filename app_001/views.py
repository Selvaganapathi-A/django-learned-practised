from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render
from django.template import loader, Template

# Create your views here.


def index(req: HttpRequest):
    return render(
        request=req,
        template_name="app_001/index.html",
        context={
            "web_page_title": "Function Views...",
        },
    )


# Simple HttpResponse
def method_01(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1> Example 1 </h1>")


# Render from HTML File
def method_02(request: HttpRequest) -> HttpResponse:
    template_: Template = loader.get_template(r"app_001\template_002.html")
    page_title: str = "Example 2"
    return HttpResponse(
        template_.render(
            request=request,
            context={
                "web_page_title": page_title,
                "founder": "Django Software Foundation.",
            },
        )
    )


# Render from HTML File version - 2
def method_03(request: HttpRequest) -> HttpResponse:
    page_title: str = "Example 3"
    return render(
        request=request,
        template_name=r"app_001\template_003.html",
        context={"web_page_title": page_title, "founder": "Django Admin"},
    )
