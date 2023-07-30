
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

from app_010.model import DemoM2M


# *** Create View *** #
class DemoM2MCreateView(CreateView):
    model = DemoM2M.DemoM2MModel
    fields = "__all__"
    template_name = r"app_010/DemoM2M/DemoM2M-create.html"
    success_url = reverse_lazy("app10:demom2m-read-list")


# *** Read List *** #
class DemoM2MListView(ListView):
    model = DemoM2M.DemoM2MModel
    queryset = DemoM2M.DemoM2MModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/DemoM2M/DemoM2M-read-all.html"
    queryset = DemoM2M.DemoM2MModel.objects.all()


# *** Read View *** #
class DemoM2MDetailView(DetailView):
    model = DemoM2M.DemoM2MModel
    template_name = r"app_010/DemoM2M/DemoM2M-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class DemoM2MUpdateView(UpdateView):
    model = DemoM2M.DemoM2MModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/DemoM2M/DemoM2M_update"
    template_name = r"app_010/DemoM2M/DemoM2M-update.html"


# *** Delete View *** #


class DemoM2MDeleteView(DeleteView):
    model = DemoM2M.DemoM2MModel
    fields = "__all__"
    template_name = r"app_010/DemoM2M/DemoM2M-delete.html"
    success_url = reverse_lazy("app10:demom2m-read-list")

