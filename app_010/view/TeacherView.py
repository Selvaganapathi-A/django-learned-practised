from django.db.models import F
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from typing import Any, Dict

from app_010.model import Teacher


# *** Create View *** #
class TeacherCreateView(CreateView):
    model = Teacher.TeacherModel
    fields = "__all__"
    template_name = r"app_010/Teacher/Teacher-create.html"
    success_url = reverse_lazy("app10:teacher-read-list")


# *** Read List *** #
class TeacherListView(ListView):
    model = Teacher.TeacherModel
    queryset = Teacher.TeacherModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/Teacher/Teacher-read-all.html"
    queryset = Teacher.TeacherModel.objects.all()


# *** Read View *** #
class TeacherDetailView(DetailView):
    model = Teacher.TeacherModel
    template_name = r"app_010/Teacher/Teacher-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class TeacherUpdateView(UpdateView):
    model = Teacher.TeacherModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/Teacher/Teacher_update"
    template_name = r"app_010/Teacher/Teacher-update.html"


# *** Delete View *** #


class TeacherDeleteView(DeleteView):
    model = Teacher.TeacherModel
    fields = "__all__"
    template_name = r"app_010/Teacher/Teacher-delete.html"
    success_url = reverse_lazy("app10:teacher-read-list")
