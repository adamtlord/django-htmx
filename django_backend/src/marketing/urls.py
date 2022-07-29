from django.urls import path

from marketing.views import HomePageView, favicon


urlpatterns = [
    path("favicon.ico", favicon),
    path("", HomePageView.as_view(), name="home"),
]