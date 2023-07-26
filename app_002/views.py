from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, RedirectView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.views.generic.edit import UpdateView

from typing import Any, Dict

from . import forms, models

# Create your views here.


def index(req: HttpRequest) -> HttpResponse:
    return render(
        request=req,
        template_name="app_002/index.html",
        context={
            "web_page_title": "Class Views",
        },
    )


# *** Basic Class based View ***


class BasicView(View):
    """Base View Example"""

    template_name = r"app_002/base-view.html"

    def get(self, request, *args, **kwargs):
        if request.content_type == "application/json":
            return JsonResponse(
                {
                    "title": "MyView",
                    "method": "get",
                },
            )
        else:
            return render(
                request=request,
                template_name=self.template_name,
                context={
                    "web_page_title": "Base View - GET http method",
                },
            )

    def post(self, request: HttpRequest, *args, **kwargs):
        if request.content_type == "application/json":
            return JsonResponse(
                {
                    "title": "MyView",
                    "method": "post",
                },
            )

        return render(
            request=request,
            template_name=self.template_name,
            context={
                "web_page_title": "Base View - POST http method",
            },
        )

    def head(self, request, *args, **kwargs):
        headers = {
            "Last Updated": "2 min ago.",
            "Updated By": "Amelia",
        }
        response: HttpResponse = HttpResponse(headers=headers)
        return response


# *** Template View ***


class ArticleAuthorList(TemplateView):
    """
    example for Template View
    """

    template_name = "app_002/articles-and-authors.html"

    extra_context = {
        "web_page_title": "Article & Author",
    }

    def get(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse:
        context = self.get_context_data()
        context["origin"] = "Madras University"
        # context["articles"] = models.Article.objects.count()
        # context["authors"] = models.Article.objects.count()
        return self.render_to_response(context=context)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(ArticleAuthorList, self).get_context_data()
        context["about"] = "Template View Example"
        return context


# *** Redirect Views ***


class TemporaryRedirect(RedirectView):
    """Temporary Redirect"""

    permanent = False
    query_string = False
    url = "https://www.google.co.in/search?q=%(term)s"
    # pattern_name = "app02:trc"


class PermenantRedirect(RedirectView):
    """Permenant Redirect"""

    permanent = True
    query_string = False
    url = reverse_lazy("index:index")


# *** Django Edit Views
# ? FormView, Create, Update, Delete Views ? #


class CustomerComplaints(FormView):
    template_name = "app_002/complaint/customer-complaint-form.html"
    form_class = forms.ComplaintForm
    success_url = reverse_lazy("app02:index")

    def form_valid(self, form: forms.ComplaintForm) -> HttpResponse:
        form.send_mail()
        return super().form_valid(form)


# *** List View ***


"""

Paginator
https://ccbv.co.uk/projects/Django/4.2/django.views.generic.base/RedirectView/

https://docs.djangoproject.com/en/4.2/ref/class-based-views/base
https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/
https://docs.djangoproject.com/en/4.2/ref/class-based-views/flattened-index/#archiveindexview

https://docs.djangoproject.com/en/4.2/topics/pagination/#paginating-a-list-view

"""


# class ArticleList(ListView):
#     """List View Example"""

#     model = models.Article
#     paginate_by = 10
#     template_name = r"app_002\article\article_list.html"
#     queryset = models.Article.objects.order_by("headline")


# class AuthorList(ListView):
#     """List View Example"""

#     model = models.Author
#     paginate_by = 10
#     template_name = r"app_002\author\author_list.html"
#     queryset = models.Author.objects.order_by("name")


# # *** Detail View ***
# class ArticleDetail(DetailView):
#     """Detail View Example"""

#     model = models.Article
#     template_name = r"app_002\article\article_detail.html"

#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         context = super(ArticleDetail, self).get_context_data()
#         context["contents"] = self.object.content.split("\n")  # type:ignore
#         context.update(kwargs)
#         return context


# class AuthorDetail(DetailView):
#     """Detail View Example"""

#     model = models.Author
#     template_name = r"app_002\author\author_detail.html"

#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         context = super(AuthorDetail, self).get_context_data()
#         context.update(kwargs)
#         return context


# # *** Create View *** #
# class AuthorCreate(CreateView):
#     model = models.Author
#     fields = ("name", "contact")
#     template_name = "app_002/author/author_create.html"


# # *** Update View *** #
# class AuthorUpdate(UpdateView):
#     model = models.Author
#     fields = ("name", "contact")
#     # template_name_suffix = "_update"
#     # template_name_field = "app_002/author/author"
#     template_name = "app_002/author/author_update.html"


# # *** Delete View *** #
# class AuthorDelete(DeleteView):
#     model = models.Author
#     fields = ("name", "contact")
#     template_name = "app_002/author/author_delete.html"
#     success_url = reverse_lazy("app02:author-list")
