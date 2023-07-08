from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.


def index(req: HttpRequest):
    return render(
        request=req,
        template_name="index/index.html",
        context={
            "web_page_title": "Homepage",
        },
    )


# Error Views Defined Below.


# # Page not found
# handler404 = "index.views.my_custom_page_not_found_view"
def my_custom_page_not_found_view(
    request: HttpRequest, exception: Exception | None = None
):
    return render(
        request=request,
        template_name="404.html",
        context={
            "web_page_title": "Not Found!",
            "pol": "lop pol lop",
        },
    )


# # Server Error
# handler500 = "index.views.my_custom_error_view"
def my_custom_error_view(request: HttpRequest, exception: Exception | None = None):
    return render(
        request=request,
        template_name="500.html",
        context={
            "web_page_title": "Server Error.",
        },
    )


# # Permission Denied
# handler403 = "index.views.my_custom_permission_denied_view"
def my_custom_permission_denied_view(
    request: HttpRequest, exception: Exception | None = None
):
    return render(
        request=request,
        template_name="403.html",
        context={
            "web_page_title": "Access Denied.",
        },
    )


# # Bad Request
# handler400 = "index.views.my_custom_bad_request_view"
def my_custom_bad_request_view(
    request: HttpRequest, exception: Exception | None = None
):
    return render(
        request=request,
        template_name="400.html",
        context={
            "web_page_title": "Bad Request.",
        },
    )
