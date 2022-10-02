from django.urls import path

from trainings.views import LandingPageView, PublicContentDetailsView, PublicContentListView

app_name = "training"

urlpatterns = [
    path('', LandingPageView.as_view(), name="landing_page"),
    path('courses', PublicContentListView.as_view(), name="course.list"),
    path('courses/<id>', PublicContentDetailsView.as_view(), name="course.details"),
]
