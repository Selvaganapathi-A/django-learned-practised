from django.http.request import HttpHeaders, HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse, StreamingHttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View

from typing import Self

from app_010.form.Demo import DemoForm


class Demo_Render(View):
    def get(self: Self, request: HttpRequest):
        form = DemoForm()
        return render(
            request=request,
            template_name="app_010/Demo/form.html",
            context={"form": form},
        )

    def post(self: Self, request: HttpRequest):
        form: DemoForm = DemoForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect(to=reverse_lazy("app10:demo_form"), permanent=True)
        return render(
            request=request,
            template_name="app_010/Demo/form.html",
            context={"form": form},
        )

    pass
