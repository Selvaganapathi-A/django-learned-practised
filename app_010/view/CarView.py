
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

from app_010.model import Car


# *** Create View *** #
class CarCreateView(CreateView):
    model = Car.CarModel
    fields = "__all__"
    template_name = r"app_010/Car/Car-create.html"
    success_url = reverse_lazy("app10:car-read-list")


# *** Read List *** #
class CarListView(ListView):
    model = Car.CarModel
    queryset = Car.CarModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/Car/Car-read-all.html"
    queryset = Car.CarModel.objects.all()


# *** Read View *** #
class CarDetailView(DetailView):
    model = Car.CarModel
    template_name = r"app_010/Car/Car-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class CarUpdateView(UpdateView):
    model = Car.CarModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/Car/Car_update"
    template_name = r"app_010/Car/Car-update.html"


# *** Delete View *** #


class CarDeleteView(DeleteView):
    model = Car.CarModel
    fields = "__all__"
    template_name = r"app_010/Car/Car-delete.html"
    success_url = reverse_lazy("app10:car-read-list")

