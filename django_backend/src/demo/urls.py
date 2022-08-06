from django.urls import include, path
from django.views.generic import RedirectView
from demo.views import app_view, dashboard_view, table_view, todo_view

urlpatterns = [
    path("", RedirectView.as_view(pattern_name='dashboard', permanent=False), name="app"),
    path("dashboard", dashboard_view, name="dashboard"),
    path("table", table_view, name="table"),
    path("todo", todo_view, name="todo"),
]