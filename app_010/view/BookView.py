
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

from app_010.model import Book


# *** Create View *** #
class BookCreateView(CreateView):
    model = Book.BookModel
    fields = "__all__"
    template_name = r"app_010/Book/Book-create.html"
    success_url = reverse_lazy("app10:book-read-list")


# *** Read List *** #
class BookListView(ListView):
    model = Book.BookModel
    queryset = Book.BookModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/Book/Book-read-all.html"
    queryset = Book.BookModel.objects.all()


# *** Read View *** #
class BookDetailView(DetailView):
    model = Book.BookModel
    template_name = r"app_010/Book/Book-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class BookUpdateView(UpdateView):
    model = Book.BookModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/Book/Book_update"
    template_name = r"app_010/Book/Book-update.html"


# *** Delete View *** #


class BookDeleteView(DeleteView):
    model = Book.BookModel
    fields = "__all__"
    template_name = r"app_010/Book/Book-delete.html"
    success_url = reverse_lazy("app10:book-read-list")

