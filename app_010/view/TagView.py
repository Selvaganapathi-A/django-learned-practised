
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

from app_010.model import Tag


# *** Create View *** #
class TagCreateView(CreateView):
    model = Tag.TagModel
    fields = "__all__"
    template_name = r"app_010/Tag/Tag-create.html"
    success_url = reverse_lazy("app10:tag-read-list")


# *** Read List *** #
class TagListView(ListView):
    model = Tag.TagModel
    queryset = Tag.TagModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/Tag/Tag-read-all.html"
    queryset = Tag.TagModel.objects.all()


# *** Read View *** #
class TagDetailView(DetailView):
    model = Tag.TagModel
    template_name = r"app_010/Tag/Tag-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class TagUpdateView(UpdateView):
    model = Tag.TagModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/Tag/Tag_update"
    template_name = r"app_010/Tag/Tag-update.html"


# *** Delete View *** #


class TagDeleteView(DeleteView):
    model = Tag.TagModel
    fields = "__all__"
    template_name = r"app_010/Tag/Tag-delete.html"
    success_url = reverse_lazy("app10:tag-read-list")

