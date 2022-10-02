from django.db import models
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager

from trainings.data import COUNTRY_DICT

ACCOUNT_TYPES = (
    ('trainee', 'Trainee'),
    ('content_creator', 'Content Creator')
)

class SkillLevel(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
class Account(AbstractUser):
    email = models.EmailField(unique=True)
    account_type = models.CharField(max_length=50, default='trainee', choices=ACCOUNT_TYPES)

    @property
    def badges(self):
        badges = self.trainee.enrolled_contents.filter(badge__isnull=False).values("badge")
        return badges

SECTOR_LIST = (
    ('private', 'Private Sector'),
    ('public', 'Public Sector'),
    ('ngo', 'NGO')
)

class ContentCreator(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="content_creator")
    location = models.CharField(max_length=100, choices=COUNTRY_DICT.items())
    organization = models.CharField(max_length=100)
    sector = models.CharField(choices=SECTOR_LIST, max_length=100)
    specialization = TaggableManager(through='trainings.ThematicAreaTag', verbose_name="Specialization")     

    def __str__(self):
        return self.account.username
class Trainee(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="trainee")
    role = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    location = models.CharField(max_length=100, choices=COUNTRY_DICT.items())
    skill_level = models.ForeignKey(SkillLevel, on_delete=models.CASCADE)
    sector = models.CharField(max_length=100, null=True)
    discipline = TaggableManager(through='trainings.ThematicAreaTag', verbose_name="Discipline")
    technologies = TaggableManager(through='trainings.TechnologyTag', verbose_name="Technologies", help_text="Technologies tags")
    
    def __str__(self):
        return self.account.username
    
    @property
    def badges(self):
        badges = self.enrolled_contents.filter(badge__isnull=False)
        return badges

