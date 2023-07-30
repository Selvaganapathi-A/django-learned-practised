
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

from app_010.model import Category


# *** Create View *** #
class CategoryCreateView(CreateView):
    model = Category.CategoryModel
    fields = "__all__"
    template_name = r"app_010/Category/Category-create.html"
    success_url = reverse_lazy("app10:category-read-list")


# *** Read List *** #
class CategoryListView(ListView):
    model = Category.CategoryModel
    queryset = Category.CategoryModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/Category/Category-read-all.html"
    queryset = Category.CategoryModel.objects.all()


# *** Read View *** #
class CategoryDetailView(DetailView):
    model = Category.CategoryModel
    template_name = r"app_010/Category/Category-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class CategoryUpdateView(UpdateView):
    model = Category.CategoryModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/Category/Category_update"
    template_name = r"app_010/Category/Category-update.html"


# *** Delete View *** #


class CategoryDeleteView(DeleteView):
    model = Category.CategoryModel
    fields = "__all__"
    template_name = r"app_010/Category/Category-delete.html"
    success_url = reverse_lazy("app10:category-read-list")

