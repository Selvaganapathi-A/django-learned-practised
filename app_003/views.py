from django.contrib import messages
from django.http import HttpRequest, HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View

import pprint

from . import forms
from .app_forms import forms_01, forms_02

# Create your views here.


def index(req: HttpRequest):
    return render(
        request=req,
        template_name="app_003/index.html",
        context={
            "web_page_title": "App 003",
        },
    )


def form_example(req: HttpRequest):
    if req.method == "POST":
        form = forms_01.FormExample(data=req.POST, files=req.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            for k, v in form.cleaned_data.items():
                print(f"{k} : {v}")
            return redirect(reverse_lazy("app03:form-example"))
    else:
        form = forms_01.FormExample()
    return render(
        request=req,
        template_name="app_003/field_form.html",
        context={
            "web_page_title": "Form Fields",
            "form": form,
        },
    )


def widget_example(req: HttpRequest):
    if req.method == "POST":
        form = forms_02.WidgetExample(data=req.POST, files=req.FILES)

        if form.is_valid():
            # print(form.cleaned_data)
            for k, v in form.cleaned_data.items():
                print(f"{k} ", v)
            return redirect(reverse_lazy("app03:field-widget"))
    else:
        form = forms_02.WidgetExample()
    return render(
        request=req,
        template_name="app_003/widget_form.html",
        context={
            "web_page_title": "Field Widgets",
            "form": form,
        },
    )


def html_widget_example(req: HttpRequest):
    if req.method == "POST":
        form = forms_02.HTMLWidgetExample(data=req.POST, files=req.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            for k, v in form.cleaned_data.items():
                print(f"{k} ", v)
            return redirect(reverse_lazy("app03:html-widget"))
    else:
        form = forms_02.HTMLWidgetExample()
    return render(
        request=req,
        template_name="app_003/field-widgets-html.html",
        context={
            "web_page_title": "Field Widgets",
            "form": form,
        },
    )


# Class Based Views Here


class IndexView(View):
    def get(self, req: HttpRequest):
        author_form = forms.AuthorForm()
        return render(
            request=req,
            template_name="app_003/index.html",
            context={
                "web_page_title": "Op 003",
                "author": author_form,
            },
        )

    def post(self, req: HttpRequest):
        author_form = forms.AuthorForm(data=req.POST, files=req.FILES)
        if author_form.is_valid():
            author_form.save()
            messages.success(req, message="Form successfully Saved.")
            return HttpResponseRedirect(redirect_to=reverse("app03:cbv01"))

        return render(
            request=req,
            template_name="app_003/index.html",
            context={
                "web_page_title": "Op 003",
                "author": author_form,
            },
        )

    pass


class PersonVew(View):
    def get(self, req: HttpRequest):
        person = forms.PersonForm()
        return render(
            request=req,
            template_name="app_003/person.html",
            context={
                "web_page_title": "Op 003",
                "person": person,
            },
        )

    def post(self, req: HttpRequest):
        person: forms.PersonForm = forms.PersonForm(data=req.POST)
        print(
            person.is_bound,
            "valid person" if person.is_valid() else "invalid person",
        )
        if person.is_valid():
            return HttpResponsePermanentRedirect(
                redirect_to=reverse("app03:person")
            )
        else:
            pprint.pprint(person.errors)
        return render(
            request=req,
            template_name="app_003/person.html",
            context={
                "web_page_title": "Op 003",
                "person": person,
            },
        )
