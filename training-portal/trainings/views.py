from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView ,DetailView
from trainings.models import Content, SkillLevel, ThematicArea, Technology


class LandingPageView(TemplateView):
    template_name = 'pages/landing_page.html'
    
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect("https://cognitio.cirrolytix.com")
    

class PublicContentListView(ListView):
    model = Content
    paginate_by = 20
    template_name = "pages/public/content_list.html"
    
    def get_queryset(self):
        queryset =  super().get_queryset()
        
        disciplines = self.request.GET.getlist('disciplines')
        tools = self.request.GET.getlist('tools')
        skill_levels = self.request.GET.getlist('skill_levels')
        search = self.request.GET.get('search')
        
        contents = queryset
        
        if search:
            contents = contents.filter(title__contains=search)
            return contents 
        
        if len(skill_levels) > 0:
            contents = contents.filter(skill_level__in=skill_levels)
            
        if len(disciplines) > 0:
            contents = contents.filter(thematic_area__slug__in=disciplines)
            
        if len(tools) > 0:
            contents = contents.filter(technologies__slug__in=tools)
            
        return contents
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["skill_levels"] = SkillLevel.objects.all()
        context["tools"] = Technology.objects.all()
        context["disciplines"] = ThematicArea.objects.all()
        
        disciplines = self.request.GET.getlist('disciplines')
        tools = self.request.GET.getlist('tools')
        skill_levels = self.request.GET.getlist('skill_levels')
        
        
        context["checked_skill_levels"] = [x for x in map(lambda x: int(x), skill_levels)]
        context["checked_disciplines"] = disciplines
        context["checked_tools"] = tools
        
        return context
    

class PublicContentDetailsView( DetailView):
    template_name = 'pages/public/content_details.html'
    model = Content
    pk_url_kwarg = "id"
    