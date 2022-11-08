from accounts.forms import UserRegisterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.http import HttpResponse


class HTMXFormClientResponseMixin:
    def form_valid(self, form):
        response = super().form_valid(form)
        response["HX-Redirect"] = self.get_success_url()
        response.status_code = 200
        return response


class HTMXPartialTemplateMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        base_template = "base.html"
        partial = False
        if self.request.htmx:
            base_template = "partial.html"
            partial = True
        context["base_template"] = base_template
        context["partial"] = partial
        return context


class SignUpView(HTMXFormClientResponseMixin, HTMXPartialTemplateMixin, SuccessMessageMixin, CreateView):
    template_name = "registration/register.html"
    success_url = reverse_lazy("dashboard")
    form_class = UserRegisterForm
    success_message = "Your profile was created successfully"

    def form_valid(self, form):
        """If the form is valid, save the associated model and log the user in."""
        response = super().form_valid(form)
        user = form.save()
        auth_login(self.request, user)
        response["HX-Redirect"] = self.get_success_url()
        response.status_code = 200
        return response


signup_view = SignUpView.as_view()


class AccountLoginView(HTMXFormClientResponseMixin, HTMXPartialTemplateMixin, LoginView):
    pass


login_view = AccountLoginView.as_view()


class AccountLogoutView(HTMXPartialTemplateMixin, TemplateView):
    template_name = "registration/logout.html"


logout_confirm_view = AccountLogoutView.as_view()
