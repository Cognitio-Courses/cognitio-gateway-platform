
from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase
from accounts.models import ContentCreator, SkillLevel, Trainee
from trainings.data import COUNTRY_TUPLES

CONTENT_TYPES = (
    ('in_person', 'In Person'),
    ('online', 'Online'),
)

class ThematicArea(TagBase):
    
    def __str__(self):
        return self.name


class ThematicAreaTag(GenericTaggedItemBase):
    tag = models.ForeignKey(ThematicArea, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_items")


class Technology(TagBase):
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Technologies"

class TechnologyTag(GenericTaggedItemBase):
    tag = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_items")


class Badge(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Content(models.Model):
    creator = models.ForeignKey(ContentCreator, on_delete=models.CASCADE, related_name="contents")
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.CharField(max_length=255)
    date = models.DateTimeField()
    language = models.CharField(max_length=50)
    type = models.CharField(choices=CONTENT_TYPES, max_length=100)
    thematic_area = TaggableManager(through=ThematicAreaTag, verbose_name="Thematic Area", help_text="Thematic area tags")
    technologies = TaggableManager(through=TechnologyTag, verbose_name="Technologies", help_text="Technologies tags")
    skill_level = models.ForeignKey(SkillLevel, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, choices=COUNTRY_TUPLES, null=True)
    trainees = models.ManyToManyField(Trainee, through='ContentTrainee', related_name='trainees')

    def __str__(self):
        return self.title
    
    @property
    def rate(self):
        rates = self.content_trainees.filter(rate__isnull=False).aggregate(models.Avg('rate'))
        return rates

class ContentTrainee(models.Model):
    trainee = models.ForeignKey(Trainee, on_delete=models.CASCADE, related_name="enrolled_contents")
    content = models.ForeignKey('Content', on_delete=models.CASCADE, related_name="content_trainees")
    badge = models.ForeignKey(Badge, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True)
    rate = models.IntegerField(null=True)
    
    
    def __str__(self):
        return f"{self.trainee.account.get_full_name()} - {self.content.title}"
    