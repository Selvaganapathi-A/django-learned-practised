
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

from app_010.model import Student


# *** Create View *** #
class StudentCreateView(CreateView):
    model = Student.StudentModel
    fields = "__all__"
    template_name = r"app_010/Student/Student-create.html"
    success_url = reverse_lazy("app10:student-read-list")


# *** Read List *** #
class StudentListView(ListView):
    model = Student.StudentModel
    queryset = Student.StudentModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/Student/Student-read-all.html"
    queryset = Student.StudentModel.objects.all()


# *** Read View *** #
class StudentDetailView(DetailView):
    model = Student.StudentModel
    template_name = r"app_010/Student/Student-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class StudentUpdateView(UpdateView):
    model = Student.StudentModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/Student/Student_update"
    template_name = r"app_010/Student/Student-update.html"


# *** Delete View *** #


class StudentDeleteView(DeleteView):
    model = Student.StudentModel
    fields = "__all__"
    template_name = r"app_010/Student/Student-delete.html"
    success_url = reverse_lazy("app10:student-read-list")

