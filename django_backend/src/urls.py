from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.views.defaults import page_not_found, server_error
from django.conf.urls.static import static


urlpatterns = [
    path(r"admin/", admin.site.urls),
    path("", include('marketing.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
