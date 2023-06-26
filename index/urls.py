from django.urls import path

from . import views

# Put app name here
app_name: str = "index"

# add your routes here.
urlpatterns = [
    path("", views.index, name="index"),
]

# Page not found
# handler404 = "index.views.my_custom_page_not_found_view"
handler404 = views.my_custom_page_not_found_view

# Server Error
# handler500 = "index.views.my_custom_error_view"
handler500 = views.my_custom_error_view


# Permission Denied
# handler403 = "index.views.my_custom_permission_denied_view"
handler403 = views.my_custom_permission_denied_view

# Bad Request
# handler400 = "index.views.my_custom_bad_request_view"
handler400 = views.my_custom_bad_request_view
