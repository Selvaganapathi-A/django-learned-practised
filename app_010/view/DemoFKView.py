
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

from app_010.model import DemoFK


# *** Create View *** #
class DemoFKCreateView(CreateView):
    model = DemoFK.DemoFKModel
    fields = "__all__"
    template_name = r"app_010/DemoFK/DemoFK-create.html"
    success_url = reverse_lazy("app10:demofk-read-list")


# *** Read List *** #
class DemoFKListView(ListView):
    model = DemoFK.DemoFKModel
    queryset = DemoFK.DemoFKModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/DemoFK/DemoFK-read-all.html"
    queryset = DemoFK.DemoFKModel.objects.all()


# *** Read View *** #
class DemoFKDetailView(DetailView):
    model = DemoFK.DemoFKModel
    template_name = r"app_010/DemoFK/DemoFK-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class DemoFKUpdateView(UpdateView):
    model = DemoFK.DemoFKModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/DemoFK/DemoFK_update"
    template_name = r"app_010/DemoFK/DemoFK-update.html"


# *** Delete View *** #


class DemoFKDeleteView(DeleteView):
    model = DemoFK.DemoFKModel
    fields = "__all__"
    template_name = r"app_010/DemoFK/DemoFK-delete.html"
    success_url = reverse_lazy("app10:demofk-read-list")

