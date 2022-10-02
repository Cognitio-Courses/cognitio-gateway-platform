from django.urls import path

from content_creator.views import DashboardView

app_name="content_creator"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard")
]
