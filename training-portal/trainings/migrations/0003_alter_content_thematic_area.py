# Generated by Django 4.1.1 on 2022-09-26 09:16

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0002_alter_content_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='thematic_area',
            field=taggit.managers.TaggableManager(help_text='Thematic area tags', through='trainings.ThematicAreaTag', to='trainings.ThematicArea', verbose_name='Thematic Area'),
        ),
    ]
