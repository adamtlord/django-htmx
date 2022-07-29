from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.views.defaults import page_not_found, server_error
from django.conf.urls.static import static


urlpatterns = [
    path("", include("marketing.urls")),
    path("accounts/", include("accounts.urls")),
    path("demo/", include("demo.urls")),
    path(r"admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
