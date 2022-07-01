from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.views.defaults import page_not_found, server_error
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path(r"admin/", admin.site.urls),
    path("", include('marketing.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns("/static/")
