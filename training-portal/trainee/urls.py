from django.urls import path

from trainee.views import ContentDetailsView, DashboardView, LeaderboardsView, RateContentView

app_name="trainee"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("leaderboards", LeaderboardsView.as_view(), name="leaderboards"),
    path("content/rate", RateContentView.as_view(), name="content.rate"),
    path("content/<id>", ContentDetailsView.as_view(), name="content.details"),
    
]
