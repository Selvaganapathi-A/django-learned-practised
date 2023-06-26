from django.urls import path

from . import views

# Put app name here
app_name: str = "app04"

# add your routes here.
urlpatterns = [
    path("", views.index, name="index"),
    path(
        "templateview/",
        views.MyTemplateView.as_view(
            extra_context={
                "web_page_title": "🍫 View",
            }
        ),
        name="templateview",
    ),
]
