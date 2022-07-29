from django.shortcuts import render
from django.views.generic.base import TemplateView


class DashboardView(TemplateView):
    template_name = "demo/dashboard.html"

dashboard_view = DashboardView.as_view()