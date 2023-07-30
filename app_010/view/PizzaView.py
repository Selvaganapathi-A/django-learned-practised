
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

from app_010.model import Pizza


# *** Create View *** #
class PizzaCreateView(CreateView):
    model = Pizza.PizzaModel
    fields = "__all__"
    template_name = r"app_010/Pizza/Pizza-create.html"
    success_url = reverse_lazy("app10:pizza-read-list")


# *** Read List *** #
class PizzaListView(ListView):
    model = Pizza.PizzaModel
    queryset = Pizza.PizzaModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/Pizza/Pizza-read-all.html"
    queryset = Pizza.PizzaModel.objects.all()


# *** Read View *** #
class PizzaDetailView(DetailView):
    model = Pizza.PizzaModel
    template_name = r"app_010/Pizza/Pizza-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class PizzaUpdateView(UpdateView):
    model = Pizza.PizzaModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/Pizza/Pizza_update"
    template_name = r"app_010/Pizza/Pizza-update.html"


# *** Delete View *** #


class PizzaDeleteView(DeleteView):
    model = Pizza.PizzaModel
    fields = "__all__"
    template_name = r"app_010/Pizza/Pizza-delete.html"
    success_url = reverse_lazy("app10:pizza-read-list")

