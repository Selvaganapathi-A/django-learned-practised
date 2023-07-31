from django import forms
from django.forms import formset_factory
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

from app_010.model.Pizza import PizzaModel
from app_010.model.Topping import ToppingModel


class PizzaForm(forms.ModelForm):
    class Meta:
        model = PizzaModel
        fields = "__all__"


class ToppingForm(forms.ModelForm):
    class Meta:
        model = ToppingModel
        fields = "__all__"


def formset_view(request: HttpRequest):
    pizza_formset = formset_factory(ToppingForm, extra=5, min_num=1)
    formset = pizza_formset()

    return render(
        request=request,
        template_name="app_010/z/formset.html",
        context={
            "title": "formset example",
            "formset": formset,
        },
    )
