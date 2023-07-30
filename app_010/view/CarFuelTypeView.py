
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

from app_010.model import CarFuelType


# *** Create View *** #
class CarFuelTypeCreateView(CreateView):
    model = CarFuelType.CarFuelTypeModel
    fields = "__all__"
    template_name = r"app_010/CarFuelType/CarFuelType-create.html"
    success_url = reverse_lazy("app10:carfueltype-read-list")


# *** Read List *** #
class CarFuelTypeListView(ListView):
    model = CarFuelType.CarFuelTypeModel
    queryset = CarFuelType.CarFuelTypeModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/CarFuelType/CarFuelType-read-all.html"
    queryset = CarFuelType.CarFuelTypeModel.objects.all()


# *** Read View *** #
class CarFuelTypeDetailView(DetailView):
    model = CarFuelType.CarFuelTypeModel
    template_name = r"app_010/CarFuelType/CarFuelType-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class CarFuelTypeUpdateView(UpdateView):
    model = CarFuelType.CarFuelTypeModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/CarFuelType/CarFuelType_update"
    template_name = r"app_010/CarFuelType/CarFuelType-update.html"


# *** Delete View *** #


class CarFuelTypeDeleteView(DeleteView):
    model = CarFuelType.CarFuelTypeModel
    fields = "__all__"
    template_name = r"app_010/CarFuelType/CarFuelType-delete.html"
    success_url = reverse_lazy("app10:carfueltype-read-list")

