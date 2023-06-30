from django.contrib import messages
from django.http import HttpRequest, HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ArchiveIndexView, CreateView, DeleteView, DetailView
from django.views.generic import FormView, ListView, RedirectView, TemplateView
from django.views.generic import UpdateView

import pprint

from . import forms

# Create your views here.


def index(req: HttpRequest):
    return render(
        request=req,
        template_name="app_003/index.html",
        context={
            "web_page_title": "App 003",
        },
    )


# Class Based Views Here


class IndexView(View):
    # def get(self):
    def get(self, req: HttpRequest):
        # print(self.request.method)
        # print(req.method)
        # author_form = forms.AuthorForm()
        # print(author_form)
        person = forms.PersonForm()
        return render(
            request=req,
            template_name="app_003/index.html",
            context={
                "web_page_title": "Op 003",
                # "author": author_form,
                "person": person,
            },
        )

    def post(self, req: HttpRequest, *args, **kwargs):
        # print()
        # print("*", args)
        # print("*", kwargs)
        # print("*", req)
        # print("*", req.method)
        # print()
        # print("*", self)
        # print("*", self.__dict__)
        # print()
        # print("*", tuple(req.POST.items()))
        # # print()
        author_form = forms.AuthorForm(data=req.POST, files=req.FILES)
        print(author_form.is_valid())
        if author_form.is_valid():
            print(author_form)
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


class ContactView(View):
    def get(self, req: HttpRequest):
        contact = forms.ContactForm()
        return render(
            request=req,
            template_name="app_003/contact.html",
            context={
                "web_page_title": "Op 003",
                "contact": contact,
            },
        )

    def post(self, req: HttpRequest, *args, **kwargs):
        contact: forms.ContactForm = forms.ContactForm(data=req.POST)
        if contact.is_valid():
            print(contact.is_bound, "valid contact" if contact.is_valid() else "invalid contact")
            return HttpResponseRedirect(redirect_to=reverse("app03:contact"))

        return render(
            request=req,
            template_name="app_003/contact.html",
            context={
                "web_page_title": "Op 003",
                "contact": contact,
            },
        )


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
        # data = tuple(req.POST.items())
        # print(data)
        person: forms.PersonForm = forms.PersonForm(data=req.POST)
        print(person.is_bound, "valid person" if person.is_valid() else "invalid person")
        if person.is_valid():
            return HttpResponsePermanentRedirect(redirect_to=reverse("app03:person"))
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
