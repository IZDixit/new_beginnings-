from django.urls import path
from .views import HomePageView, DashboardView, InputView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("input/", InputView.as_view(), name="input"),
]