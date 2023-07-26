from django.core import paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.views import generic

from typing import Iterable

import uuid


# from . import models

# Create your views here.


def index(req: HttpRequest):
    return render(
        request=req,
        template_name="app_004/index.html",
        context={
            "web_page_title": "App 004",
        },
    )


# def person_detail(req: HttpRequest, pk: uuid.UUID):
#     person: models.Person = models.Person.objects.get(pk=pk)
#     return render(
#         request=req,
#         template_name="app_004/person/detail.html",
#         context={
#             "web_page_title": "App 004",
#             "person": person,
#         },
#     )


# def person_list(req: HttpRequest):
#     people: Iterable[models.Person] = models.Person.objects.all()
#     pages: paginator.Paginator = paginator.Paginator(people, 3)
#     current_page = 4
#     go = pages.get_elided_page_range(current_page, on_each_side=2, on_ends=1)
#     print(go)

#     return render(
#         request=req,
#         template_name="app_004/person/list.html",
#         context={
#             "web_page_title": "App 004",
#             "persons": people,
#         },
#     )


# class StudentDetail(generic.DetailView):
#     model = models.Student
#     queryset = models.Student.objects.all()


# class StudentList(generic.ListView):
#     model = models.Student
#     queryset = models.Student.objects.all()
#     paginate_by = 5
#     paginate_by = 5
