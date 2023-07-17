from django.http import HttpRequest, HttpResponse
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


def student_list(request: HttpRequest):
    
    return render(
        request=request,
        template_name="app_006/student_list.html",
        context={
            "web_page_title": "App 006",
        },
    )
