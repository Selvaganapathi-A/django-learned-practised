from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils import timesince, timezone
from django.views.generic import DetailView, ListView

from typing import Any

from . import models

# Create your views here.

"""
Paginator
https://docs.djangoproject.com/en/4.2/topics/pagination/#paginating-a-list-view
https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/
"""


class MyDetailView(DetailView):
    model = models.Article

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data()
        context["now"] = timezone.now()
        context["contents"] = self.object.content.split("\n")  # type: ignore
        return context


class MyListView(ListView):
    model = models.Article
    paginate_by = 25
