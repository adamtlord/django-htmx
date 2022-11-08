from django.views.generic.base import TemplateView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET


class HomePageView(TemplateView):
    template_name = "marketing/home.html"


@require_GET
def favicon(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
            + '<text y=".9em" font-size="90">🔋</text>'
            + "</svg>"
        ),
        content_type="image/svg+xml",
    )
