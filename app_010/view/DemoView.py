
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import F, Q
from django.views import View
from django.views.generic import DetailView, ListView, RedirectView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.views.generic.edit import UpdateView

from typing import Any, Dict

from app_010.model import Demo


# *** Create View *** #
class DemoCreateView(CreateView):
    model = Demo.DemoModel
    fields = "__all__"
    template_name = r"app_010/Demo/Demo-create.html"
    success_url = reverse_lazy("app10:demo-read-list")


# *** Read List *** #
class DemoListView(ListView):
    model = Demo.DemoModel
    queryset = Demo.DemoModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/Demo/Demo-read-all.html"
    queryset = Demo.DemoModel.objects.all()


# *** Read View *** #
class DemoDetailView(DetailView):
    model = Demo.DemoModel
    template_name = r"app_010/Demo/Demo-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class DemoUpdateView(UpdateView):
    model = Demo.DemoModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/Demo/Demo_update"
    template_name = r"app_010/Demo/Demo-update.html"


# *** Delete View *** #


class DemoDeleteView(DeleteView):
    model = Demo.DemoModel
    fields = "__all__"
    template_name = r"app_010/Demo/Demo-delete.html"
    success_url = reverse_lazy("app10:demo-read-list")

