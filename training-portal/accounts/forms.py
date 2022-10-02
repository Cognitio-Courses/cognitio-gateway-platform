from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from accounts.models import SECTOR_LIST, SkillLevel
from trainings.data import COUNTRY_TUPLES
from trainings.models import Technology, ThematicArea


class AccountRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    skill_level = forms.ModelChoiceField(queryset=SkillLevel.objects.all())
    occupation = forms.CharField(max_length=100)
    discipline = forms.ModelMultipleChoiceField(queryset=ThematicArea.objects.all())
    location = forms.ChoiceField(choices=COUNTRY_TUPLES)
    sector = forms.CharField()
    role = forms.CharField()
    technologies = forms.ModelChoiceField(queryset=Technology.objects.all())

    class Meta:
        model = get_user_model()
        fields = ('username', 'last_name', 'email', 'first_name')
        


class ContentCreatorAccountRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    skill_level = forms.ModelChoiceField(queryset=SkillLevel.objects.all())
    occupation = forms.CharField(max_length=100)
    specialization = forms.ModelMultipleChoiceField(queryset=ThematicArea.objects.all())
    location = forms.ChoiceField(choices=COUNTRY_TUPLES)
    sector = forms.ChoiceField(choices=SECTOR_LIST)

    class Meta:
        model = get_user_model()
        fields = ('username', 'last_name', 'email', 'first_name')