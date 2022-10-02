from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.views.generic import RedirectView
from django.urls import  reverse
from django.contrib.auth.models import Group
from accounts.forms import AccountRegisterForm, ContentCreatorAccountRegisterForm

from accounts.models import SECTOR_LIST, Account, ContentCreator, SkillLevel, Trainee
from trainings.data import COUNTRY_LIST
from trainings.models import ThematicArea, Technology


class AccountLoginView(LoginView):
    template_name = "accounts/auth/login.html"
    redirect_authenticated_user = True
    
    def get_success_url(self):
        user = self.request.user
        if user.is_superuser:
            return "/admin/"
        if user.account_type == 'trainee':
            return reverse("trainee:dashboard")
        else:
            return "/admin/"
    

class AccountRegisterView(SuccessMessageMixin, CreateView):
    
    template_name = 'accounts/auth/register.html'
    form_class = AccountRegisterForm
    success_message = "You are successfully registered! Login now."
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thematic_areas'] = ThematicArea.objects.all()
        context['skill_levels'] = SkillLevel.objects.all()
        context['technologies'] = Technology.objects.all()
        context['countries'] = COUNTRY_LIST
        context['sectors'] = SECTOR_LIST
        return context
    
    
    def form_valid(self, form):
        new_user = form.save(commit=True)
        print(form.cleaned_data)
        new_trainee = Trainee.objects.create(account=new_user,
                                             skill_level=form.cleaned_data['skill_level'],
                                             discipline=form.cleaned_data['discipline'],
                                             occupation=form.cleaned_data['occupation'],
                                             location=form.cleaned_data['location'],
                                             role=form.cleaned_data['role'],
                                             sector=form.cleaned_data['sector'],
                                             technologies=form.cleaned_data['technologies'],
                                             )
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("account:login") + "?register=true"


class ContentCreatorAccountRegisterView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/auth/content_creator/register.html'
    form_class = ContentCreatorAccountRegisterForm
    success_message = "You are successfully registered! Login now."
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thematic_areas'] = ThematicArea.objects.all()
        context['skill_levels'] = SkillLevel.objects.all()
        context['countries'] = COUNTRY_LIST
        context['sectors'] = SECTOR_LIST
        return context
    
    
    def form_valid(self, form):
        content_creator_group = Group.objects.get(name='content_creator')
        new_user = form.save(commit=False)
        new_user.is_active = False
        new_user.is_staff = True
        new_user.account_type = 'content_creator'
        new_user.save()
        new_user.groups.add(content_creator_group)
        new_trainee = ContentCreator.objects.create(account=new_user,
                                             specialization=form.cleaned_data['specialization'],
                                             location=form.cleaned_data['location'],
                                             sector=form.cleaned_data['sector'],
                                             )
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("account:login")+ "?register=true"
    


class RedirectLoggedinAccountView(RedirectView):
    permanent= True
    
    def get_redirect_url(self, *args, **kwargs):
        authenticated_user = self.request.user
        if authenticated_user.account_type == "trainee":
            return reverse("trainee:dashboard")
        return "/admin/"



class AccountLogoutView(LogoutView):
    
    def get_success_url(self):
        return reverse("account:login")