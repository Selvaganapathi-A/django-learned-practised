"""
URL configuration for Organisation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.png")),
    ),
    path("admin/", admin.site.urls),
    path("", include("index.urls", namespace="index")),
    path("app01/", include("app_001.urls", namespace="app_001")),
    path("app02/", include("app_002.urls", namespace="app_002")),
    path("app03/", include("app_003.urls", namespace="app_003")),
    path("app04/", include("app_004.urls", namespace="app_004")),
    path("app05/", include("app_005.urls", namespace="app_005")),
    path("app06/", include("app_006.urls", namespace="app_006")),
    path("app07/", include("app_007.urls", namespace="app_007")),
    path("app08/", include("app_008.urls", namespace="app_008")),
    path("app09/", include("app_009.urls", namespace="app_009")),
    path("app10/", include("app_010.urls", namespace="app_010")),
]


if settings.DEBUG:
    urlpatterns = (
        urlpatterns
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
