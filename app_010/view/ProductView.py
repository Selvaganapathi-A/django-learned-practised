
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

from app_010.model import Product


# *** Create View *** #
class ProductCreateView(CreateView):
    model = Product.ProductModel
    fields = "__all__"
    template_name = r"app_010/Product/Product-create.html"
    success_url = reverse_lazy("app10:product-read-list")


# *** Read List *** #
class ProductListView(ListView):
    model = Product.ProductModel
    queryset = Product.ProductModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/Product/Product-read-all.html"
    queryset = Product.ProductModel.objects.all()


# *** Read View *** #
class ProductDetailView(DetailView):
    model = Product.ProductModel
    template_name = r"app_010/Product/Product-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class ProductUpdateView(UpdateView):
    model = Product.ProductModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/Product/Product_update"
    template_name = r"app_010/Product/Product-update.html"


# *** Delete View *** #


class ProductDeleteView(DeleteView):
    model = Product.ProductModel
    fields = "__all__"
    template_name = r"app_010/Product/Product-delete.html"
    success_url = reverse_lazy("app10:product-read-list")

