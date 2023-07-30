from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import render
from django.template import loader, Template


# Create your views here.


def index(req: HttpRequest):
    """
    Simple Way to Render via HTML File.
    """
    return render(
        request=req,
        template_name="app_001/index.html",
        context={
            "web_page_title": "Function Views...",
        },
    )


# Simple HttpResponse
def method_01(request: HttpRequest) -> HttpResponse:
    """
    Simple HTTP Response
    """
    return HttpResponse("<h1> Example 1 </h1>")


# Render from HTML File
def method_02(request: HttpRequest) -> HttpResponse:
    """
    Render From HTML File.
    1. Load Template
    2. Render with Custom Data
    3. Send as Simple Http Response
    """
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
    """
    As Normal.
    """
    page_title: str = "Example 3"
    return render(
        request=request,
        template_name=r"app_001\template_003.html",
        context={"web_page_title": page_title, "founder": "Django Admin"},
    )
