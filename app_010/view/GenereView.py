
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

from app_010.model import Genere


# *** Create View *** #
class GenereCreateView(CreateView):
    model = Genere.GenereModel
    fields = "__all__"
    template_name = r"app_010/Genere/Genere-create.html"
    success_url = reverse_lazy("app10:genere-read-list")


# *** Read List *** #
class GenereListView(ListView):
    model = Genere.GenereModel
    queryset = Genere.GenereModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/Genere/Genere-read-all.html"
    queryset = Genere.GenereModel.objects.all()


# *** Read View *** #
class GenereDetailView(DetailView):
    model = Genere.GenereModel
    template_name = r"app_010/Genere/Genere-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class GenereUpdateView(UpdateView):
    model = Genere.GenereModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/Genere/Genere_update"
    template_name = r"app_010/Genere/Genere-update.html"


# *** Delete View *** #


class GenereDeleteView(DeleteView):
    model = Genere.GenereModel
    fields = "__all__"
    template_name = r"app_010/Genere/Genere-delete.html"
    success_url = reverse_lazy("app10:genere-read-list")

