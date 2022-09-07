from django.urls import include, path
from django.views.generic import RedirectView
from demo.views import dashboard_view, table_view, todo_view, person_list

urlpatterns = [
    path("", RedirectView.as_view(pattern_name='dashboard', permanent=False), name="app"),
    path("dashboard", dashboard_view, name="dashboard"),
    path("table", table_view, name="table"),
    path("todo", todo_view, name="todo"),

    path("people", person_list, name="person_list")
]