from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.db.models import Count
from django.contrib import messages
from accounts.mixins import AccountLoginRequiredMixin
from accounts.models import Account, SkillLevel, Trainee
from trainings.models import Content, ContentTrainee, Technology, ThematicArea


class DashboardView(AccountLoginRequiredMixin,ListView):
    model = Content
    paginate_by = 20
    template_name = "trainee/pages/dashboard.html"
    
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


class ContentDetailsView(AccountLoginRequiredMixin, DetailView):
    template_name = 'trainee/pages/content_details.html'
    model = Content
    pk_url_kwarg = "id"
    
    def post(self, *args, **kwargs):
        user = self.request.user
        content = self.get_object()
        content.trainees.add(user.trainee)
        return HttpResponseRedirect(self.request.path_info)
    
    def get_context_data(self, **kwargs):
        user = self.request.user
        trainee = user.trainee
        context =  super().get_context_data(**kwargs)
        try:
            context['enrolled_content'] = ContentTrainee.objects.get(content=self.get_object(), trainee=trainee)
        except:
            context['enrolled_content'] = None
        return context
    

class RateContentView(AccountLoginRequiredMixin,View):
    http_method_names = ['post']
    model = None

    def post(self, request,  *args, **kwargs):
        content_id = self.request.POST['content_id']
        rate = self.request.POST['rate']
        content = Content.objects.get(pk=content_id)
        user = self.request.user
        trainee = user.trainee
        content_trainee = ContentTrainee.objects.get(trainee=trainee, content=content)
        content_trainee.rate = rate
        content_trainee.save()
        messages.add_message(request,messages.SUCCESS, "Content successfully rated")
        return HttpResponseRedirect(reverse("trainee:content.details", kwargs={'id':content_id}))
        
        
class LeaderboardsView(ListView):
    queryset = Trainee.objects.filter(enrolled_contents__badge__isnull=False).values('account__username', 'account__first_name','account__last_name').annotate(badge_count=Count('enrolled_contents')).order_by('-badge_count')
    template_name = "trainee/pages/leaderboards.html"