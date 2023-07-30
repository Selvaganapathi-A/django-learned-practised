
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

from app_010.model import Topping


# *** Create View *** #
class ToppingCreateView(CreateView):
    model = Topping.ToppingModel
    fields = "__all__"
    template_name = r"app_010/Topping/Topping-create.html"
    success_url = reverse_lazy("app10:topping-read-list")


# *** Read List *** #
class ToppingListView(ListView):
    model = Topping.ToppingModel
    queryset = Topping.ToppingModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/Topping/Topping-read-all.html"
    queryset = Topping.ToppingModel.objects.all()


# *** Read View *** #
class ToppingDetailView(DetailView):
    model = Topping.ToppingModel
    template_name = r"app_010/Topping/Topping-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class ToppingUpdateView(UpdateView):
    model = Topping.ToppingModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/Topping/Topping_update"
    template_name = r"app_010/Topping/Topping-update.html"


# *** Delete View *** #


class ToppingDeleteView(DeleteView):
    model = Topping.ToppingModel
    fields = "__all__"
    template_name = r"app_010/Topping/Topping-delete.html"
    success_url = reverse_lazy("app10:topping-read-list")

