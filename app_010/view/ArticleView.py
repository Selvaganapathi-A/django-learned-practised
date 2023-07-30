
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

from app_010.model import Article


# *** Create View *** #
class ArticleCreateView(CreateView):
    model = Article.ArticleModel
    fields = "__all__"
    template_name = r"app_010/Article/Article-create.html"
    success_url = reverse_lazy("app10:article-read-list")


# *** Read List *** #
class ArticleListView(ListView):
    model = Article.ArticleModel
    queryset = Article.ArticleModel.objects.all().order_by(F("1"))
    paginate_by = 10
    template_name = r"app_010/Article/Article-read-all.html"
    queryset = Article.ArticleModel.objects.all()


# *** Read View *** #
class ArticleDetailView(DetailView):
    model = Article.ArticleModel
    template_name = r"app_010/Article/Article-read.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data()
        context.update(kwargs)
        return context


# *** Update View *** #
class ArticleUpdateView(UpdateView):
    model = Article.ArticleModel
    fields = "__all__"
    # template_name_suffix = "_update"
    # template_name_field = "app_010/Article/Article_update"
    template_name = r"app_010/Article/Article-update.html"


# *** Delete View *** #


class ArticleDeleteView(DeleteView):
    model = Article.ArticleModel
    fields = "__all__"
    template_name = r"app_010/Article/Article-delete.html"
    success_url = reverse_lazy("app10:article-read-list")

