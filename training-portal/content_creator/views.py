from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = "content_creator/base.html"