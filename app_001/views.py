from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect, StreamingHttpResponse
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
    return HttpResponse("<h1> Hello </h1>")


# Render from HTML File
def method_02(request: HttpRequest) -> HttpResponse:
    template_: Template = loader.get_template("app_001/view_001.html")
    page_title: str = "Method 2"
    return HttpResponse(
        template_.render(
            request=request,
            context={
                "web_page_title": page_title,
            },
        )
    )


# Render from HTML File v2
def method_03(request: HttpRequest) -> HttpResponse:
    page_title: str = "Method 3"
    return render(
        request=request,
        template_name="app_001/view_002.html",
        context={
            "web_page_title": page_title,
        },
    )
