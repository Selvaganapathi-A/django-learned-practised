from django.http import HttpRequest, JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import RedirectView, TemplateView

from typing import Any

# Create your views here.


class MyView(View):
    template_name = "app_002/myview.html"

    def get(self, request, *args, **kwargs):
        if request.content_type == "application/json":
            return JsonResponse(
                {
                    "title": "MyView",
                    "method": "get",
                },
            )
        else:
            return render(
                request=request,
                template_name=self.template_name,
                context={
                    "web_page_title": "MyView - GET",
                },
            )

    def post(self, request: HttpRequest, *args, **kwargs):
        if request.content_type == "application/json":
            return JsonResponse(
                {
                    "title": "MyView",
                    "method": "post",
                },
            )

        return render(
            request=request,
            template_name=self.template_name,
            context={
                "web_page_title": "MyView - POST",
            },
        )

    def head(self, request, *args, **kwargs):
        if request.content_type == "application/json":
            return JsonResponse(
                {
                    "title": "MyView",
                    "method": "head",
                },
            )
        return render(
            request=request,
            template_name=self.template_name,
            context={
                "web_page_title": "MyView - HEAD",
            },
        )


class MyTemplateView(TemplateView):
    template_name = "app_002/mytemplateview.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        context = self.get_context_data()
        context["college"] = "University of Titan/Jupiter"
        return self.render_to_response(context=context)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(MyTemplateView, self).get_context_data()
        context["name"] = "My Template View"
        context["web_page_title"] = "My Template View - GET"
        return context


"""
https://docs.djangoproject.com/en/4.2/ref/class-based-views/base
https://ccbv.co.uk/projects/Django/4.2/django.views.generic.base/RedirectView/
"""


class myRedirectView(RedirectView):
    permanent = False
    query_string = False
    pattern_name = "app02:index"


class MyPermenantRedirectView(RedirectView):
    permanent = True
    query_string = False
    url = reverse_lazy("index:index")
