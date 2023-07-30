
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

from app_010.model import DemoO2O


# *** Create View *** #
class DemoO2OCreateView(CreateView):
    model = DemoO2O.DemoO2OModel
    fields = "__all__"
    template_name = r"app_010/DemoO2O/DemoO2O-create.html"
    success_url = reverse_lazy("app10:demoo2o-read-list")


# *** Read List *** #
class DemoO2OListView(ListView):
    model = DemoO2O.DemoO2OModel
    queryset = DemoO2O.DemoO2OModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/DemoO2O/DemoO2O-read-all.html"
    queryset = DemoO2O.DemoO2OModel.objects.all()


# *** Read View *** #
class DemoO2ODetailView(DetailView):
    model = DemoO2O.DemoO2OModel
    template_name = r"app_010/DemoO2O/DemoO2O-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class DemoO2OUpdateView(UpdateView):
    model = DemoO2O.DemoO2OModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/DemoO2O/DemoO2O_update"
    template_name = r"app_010/DemoO2O/DemoO2O-update.html"


# *** Delete View *** #


class DemoO2ODeleteView(DeleteView):
    model = DemoO2O.DemoO2OModel
    fields = "__all__"
    template_name = r"app_010/DemoO2O/DemoO2O-delete.html"
    success_url = reverse_lazy("app10:demoo2o-read-list")

