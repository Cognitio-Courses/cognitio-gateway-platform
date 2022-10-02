from django.core.management.base import BaseCommand
from accounts.models import SkillLevel

from trainings.models import Technology, ThematicArea


class Command(BaseCommand):
    help = "Intialize data neeeded"
    
    def handle(self, *args, **options):
        
        ThematicArea(name="Agriculture",).save()
        ThematicArea(name="Climate").save()
        ThematicArea(name="Disaster Risk Reduction").save()
        ThematicArea(name="Water Resources").save()
        ThematicArea(name="Air Quality").save()
        ThematicArea(name="Health Science").save()
        
        
        
        Technology(name="ArcGIS").save()
        Technology(name="WorldVIEW").save()
        Technology(name="Sentinel").save()
        Technology(name="Google Earth Engine").save()
        Technology(name="Giovanni").save()
        Technology(name="AppEARS").save()
        
        
        SkillLevel.objects.bulk_create([
            SkillLevel(name="Beginner"),
            SkillLevel(name="Intermediate"),
            SkillLevel(name="Advance"),
        ])