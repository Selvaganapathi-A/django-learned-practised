from django.http import HttpRequest, request
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ArchiveIndexView, CreateView, DateDetailView
from django.views.generic import DayArchiveView, DeleteView, DetailView, FormView
from django.views.generic import ListView, MonthArchiveView, RedirectView, TemplateView
from django.views.generic import TodayArchiveView, UpdateView, View, WeekArchiveView
from django.views.generic import YearArchiveView

from typing import Any

# Create your views here.


def index(req: HttpRequest):
    return render(
        request=req,
        template_name="app_004/index.html",
        context={
            "web_page_title": "App 004",
        },
    )


class MyTemplateView(TemplateView):
    template_name = "app_004/experimental/index.html"
    template_engine = None

    ### Here or urlconf
    # extra_context = {
    #     "web_page_title": "Template View",
    # }

    http_method_names = ["get", "post"]

    content_type = "text/html"

    # def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     return super().get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        context = super(MyTemplateView, self).get_context_data(*args, **kwargs)
        # context["web_page_title"] = "Another Title"
        context["sequence"] = (0, 8, 6, 4, 2, 9, 7, 5, 3, 1)
        return context


# print(dir(MyTemplateView))
# print()
# print(dir(Homeview.as_view()))
# print()
# help(Homeview)
# print()


class MyCreateView(CreateView):
    pass
