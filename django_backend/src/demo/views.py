import time
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_GET, require_http_methods
from django.shortcuts import render
from django.db.models import Q
from demo.models import Person
from faker import Faker
from core.decorators import htmx_login_required



class HTMXAppTemplateMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_template = "app.html"
        if self.request.htmx:
            base_template = "app_stage.html"
        context["base_template"] = base_template
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "demo/dashboard_page.html"


dashboard_view = DashboardView.as_view()


class TableView(LoginRequiredMixin, TemplateView):
    template_name = "demo/table_page.html"


table_view = TableView.as_view()


class TodoView(LoginRequiredMixin, TemplateView):
    template_name = "demo/todo_page.html"


todo_view = TodoView.as_view()


@htmx_login_required
def person_list(request: HttpRequest) -> HttpResponse:
    template = "demo/person_table.html"

    page_num = request.GET.get("page", "1")
    per_page = request.GET.get("pp", "10")
    query = request.GET.get("q", "")

    people = Person.objects.all()
    if query:
        people = people.filter(
            Q(firstname__icontains=query) | Q(lastname__icontains=query) | Q(title__icontains=query)
        )
    paginator = Paginator(people, int(per_page))
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    d = {
        "page": page,
        "count": paginator.count,
        "page_range": paginator.get_elided_page_range(page_num, on_each_side=1, on_ends=2),
        "per_page": per_page,
        "query": query,
        "page_size_options": ["10", "25", "50", "100"],
    }

    return render(request, template, d)


@htmx_login_required
def featured_people(request: HttpRequest) -> HttpResponse:
    people = Person.objects.all().order_by("?")[:4]
    template = "demo/featured_people.html"

    d = {"people": people}

    return render(request, template, d)


@htmx_login_required
def random_stat(request: HttpRequest) -> HttpResponse:
    template = "demo/stat_card.html"
    fake = Faker()
    sleep = fake.random_int(min=0, max=3)
    time.sleep(sleep)
    title = fake.catch_phrase()
    stat1 = fake.random_number(digits=5)
    add = fake.boolean()
    difference = fake.random_int(max=stat1)
    factor = 1 if add else -1
    stat2 = stat1 + (factor * difference)

    d = {
        "title": title,
        "stat1": stat1,
        "add": add,
        "difference": f"{(difference / stat1)*100:.2f}",
        "factor": factor,
        "stat2": stat2,
    }

    return render(request, template, d)
