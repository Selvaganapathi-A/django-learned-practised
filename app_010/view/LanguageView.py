
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

from app_010.model import Language


# *** Create View *** #
class LanguageCreateView(CreateView):
    model = Language.LanguageModel
    fields = "__all__"
    template_name = r"app_010/Language/Language-create.html"
    success_url = reverse_lazy("app10:language-read-list")


# *** Read List *** #
class LanguageListView(ListView):
    model = Language.LanguageModel
    queryset = Language.LanguageModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/Language/Language-read-all.html"
    queryset = Language.LanguageModel.objects.all()


# *** Read View *** #
class LanguageDetailView(DetailView):
    model = Language.LanguageModel
    template_name = r"app_010/Language/Language-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class LanguageUpdateView(UpdateView):
    model = Language.LanguageModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/Language/Language_update"
    template_name = r"app_010/Language/Language-update.html"


# *** Delete View *** #


class LanguageDeleteView(DeleteView):
    model = Language.LanguageModel
    fields = "__all__"
    template_name = r"app_010/Language/Language-delete.html"
    success_url = reverse_lazy("app10:language-read-list")

