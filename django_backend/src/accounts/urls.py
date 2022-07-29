from django.urls import include, path
from accounts.views import signup_view, login_view, logout_confirm_view

urlpatterns = [
    path("register/", signup_view, name="account_signup"),
    path("login/", login_view, name="account_login"),
    path("logout-confirm/", logout_confirm_view, name="account_logout"),
    path("", include("django.contrib.auth.urls")),
]