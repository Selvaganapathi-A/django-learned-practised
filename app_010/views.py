from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

import datetime

from dateutil.relativedelta import relativedelta

import pytz

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name="app_010/index.html",
        context={
            "web_page_title": "App 010",
        },
    )


def humanized_view(request: HttpRequest) -> HttpResponse:
    """
    Humanize View
    --> https://docs.djangoproject.com/en/4.2/ref/contrib/humanize/
    """
    india_timezone = pytz.timezone("Asia/Calcutta")
    b_day = datetime.datetime(2023, 8, 5, 22, 15, 18, tzinfo=india_timezone)
    rand_date = datetime.date.today() + relativedelta(days=1)
    rand_datetime = datetime.datetime.now(india_timezone) + relativedelta(
        hours=1, minutes=23, weeks=1, days=2
    )
    return render(
        request=request,
        template_name="app_010/extra/template_001.html",
        context={
            "web_page_title": "humanized data",
            "b_day": b_day,
            "rand_date": rand_date,
            "rand_datetime": rand_datetime,
        },
    )
