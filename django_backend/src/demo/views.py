from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_GET, require_http_methods
from django.shortcuts import render


@require_GET
def app_view(request: HttpRequest) -> HttpResponse:
    context = {
        "base_template": "app.html",
    }
    return render(request, "demo/dashboard.html", context)


@require_GET
def dashboard_view(request: HttpRequest) -> HttpResponse:
    if request.htmx:
        base_template = "app_stage.html"
    else:
        base_template = "app.html"

    context = {
        "base_template": base_template,
    }
    return render(request, "demo/dashboard.html", context)


@require_GET
def table_view(request: HttpRequest) -> HttpResponse:
    if request.htmx:
        base_template = "app_stage.html"
    else:
        base_template = "app.html"

    context = {
        "key": "value",
        "base_template": base_template,
    }
    return render(request, "demo/table.html", context)


@require_GET
def todo_view(request: HttpRequest) -> HttpResponse:
    if request.htmx:
        base_template = "app_stage.html"
    else:
        base_template = "app.html"

    context = {
        "key": "value",
        "base_template": base_template,
    }
    return render(request, "demo/todo.html", context)
