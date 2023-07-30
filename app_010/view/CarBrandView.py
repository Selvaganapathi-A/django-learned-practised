
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

from app_010.model import CarBrand


# *** Create View *** #
class CarBrandCreateView(CreateView):
    model = CarBrand.CarBrandModel
    fields = "__all__"
    template_name = r"app_010/CarBrand/CarBrand-create.html"
    success_url = reverse_lazy("app10:carbrand-read-list")


# *** Read List *** #
class CarBrandListView(ListView):
    model = CarBrand.CarBrandModel
    queryset = CarBrand.CarBrandModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/CarBrand/CarBrand-read-all.html"
    queryset = CarBrand.CarBrandModel.objects.all()


# *** Read View *** #
class CarBrandDetailView(DetailView):
    model = CarBrand.CarBrandModel
    template_name = r"app_010/CarBrand/CarBrand-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class CarBrandUpdateView(UpdateView):
    model = CarBrand.CarBrandModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/CarBrand/CarBrand_update"
    template_name = r"app_010/CarBrand/CarBrand-update.html"


# *** Delete View *** #


class CarBrandDeleteView(DeleteView):
    model = CarBrand.CarBrandModel
    fields = "__all__"
    template_name = r"app_010/CarBrand/CarBrand-delete.html"
    success_url = reverse_lazy("app10:carbrand-read-list")

