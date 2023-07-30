
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

from app_010.model import Person


# *** Create View *** #
class PersonCreateView(CreateView):
    model = Person.PersonModel
    fields = "__all__"
    template_name = r"app_010/Person/Person-create.html"
    success_url = reverse_lazy("app10:person-read-list")


# *** Read List *** #
class PersonListView(ListView):
    model = Person.PersonModel
    queryset = Person.PersonModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/Person/Person-read-all.html"
    queryset = Person.PersonModel.objects.all()


# *** Read View *** #
class PersonDetailView(DetailView):
    model = Person.PersonModel
    template_name = r"app_010/Person/Person-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class PersonUpdateView(UpdateView):
    model = Person.PersonModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/Person/Person_update"
    template_name = r"app_010/Person/Person-update.html"


# *** Delete View *** #


class PersonDeleteView(DeleteView):
    model = Person.PersonModel
    fields = "__all__"
    template_name = r"app_010/Person/Person-delete.html"
    success_url = reverse_lazy("app10:person-read-list")

