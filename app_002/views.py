from django.http import HttpRequest, HttpResponse, HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect, StreamingHttpResponse
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
