from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_GET, require_http_methods
from django.shortcuts import render
from demo.models import Person

class HTMXAppTemplateMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_template = "app.html"
        if self.request.htmx:
            base_template = "app_stage.html"
        context["base_template"] = base_template
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "demo/dashboard.html"


dashboard_view = DashboardView.as_view()


class TableView(LoginRequiredMixin, TemplateView):
    template_name = "demo/table.html"


table_view = TableView.as_view()


class TodoView(LoginRequiredMixin, TemplateView):
    template_name = "demo/todo.html"


todo_view = TodoView.as_view()


@login_required
def person_list(request: HttpRequest) -> HttpResponse:
    page_num = request.GET.get("page", "1")
    people = Person.objects.all()
    template = "demo/person_table.html"
    paginator = Paginator(people, 10)
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    d = {
        "page": page,
        "paginator": paginator
    }

    return render(
        request,
        template,
        d
    )
