from django.urls import include, path
from demo.views import dashboard_view

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
]