#
from django import forms
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils import timesince, timezone
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView

from typing import Any

from . import models

# Create your views here.

"""
1) https://docs.djangoproject.com/en/4.2/ref/class-based-views/flattened-index/#archiveindexview
2)
"""

#


class AuthorDetailView(DetailView):
    model = models.Author


class AuthorListView(ListView):
    model = models.Author
    paginate_by = 5


#


class AuthorCreateView(CreateView):
    model = models.Author
    fields = ["name"]


class AuthorUpdateView(UpdateView):
    model = models.Author
    fields = ["name"]
    template_name_suffix = "_update_form"


class AuthorDeleteView(DeleteView):
    model = models.Author
    fields = ["name"]
    success_url = reverse_lazy("app02:authorlistview")


#


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary

        print()
        print()
        print()
        print(f"{self.cleaned_data['name']}")
        print()
        print(f"{self.cleaned_data['message']}")
        print()
        print()
        print()
        pass


class ContactFormView(FormView):
    template_name = "app_002/contact_form.html"
    form_class = ContactForm
    success_url = reverse_lazy("app02:index")

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
