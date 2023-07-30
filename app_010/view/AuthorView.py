
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

from app_010.model import Author


# *** Create View *** #
class AuthorCreateView(CreateView):
    model = Author.AuthorModel
    fields = "__all__"
    template_name = r"app_010/Author/Author-create.html"
    success_url = reverse_lazy("app10:author-read-list")


# *** Read List *** #
class AuthorListView(ListView):
    model = Author.AuthorModel
    queryset = Author.AuthorModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/Author/Author-read-all.html"
    queryset = Author.AuthorModel.objects.all()


# *** Read View *** #
class AuthorDetailView(DetailView):
    model = Author.AuthorModel
    template_name = r"app_010/Author/Author-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class AuthorUpdateView(UpdateView):
    model = Author.AuthorModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/Author/Author_update"
    template_name = r"app_010/Author/Author-update.html"


# *** Delete View *** #


class AuthorDeleteView(DeleteView):
    model = Author.AuthorModel
    fields = "__all__"
    template_name = r"app_010/Author/Author-delete.html"
    success_url = reverse_lazy("app10:author-read-list")

