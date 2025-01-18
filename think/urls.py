from django.urls import path
from .views import HomePageView, DashboardView, InputView

urlpatterns = [
    # URL pattern for the home page
    path("", HomePageView.as_view(), name="home"),
    # URL pattern for the dashboard page
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    # URL pattern for the input page
    path("input/", InputView.as_view(), name="input"),
]