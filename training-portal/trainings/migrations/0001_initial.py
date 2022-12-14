# Generated by Django 4.1.1 on 2022-09-26 05:29

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('language', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('in_person', 'In Person'), ('online', 'Online')], max_length=100)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='accounts.trainee')),
                ('skill_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.skilllevel')),
            ],
        ),
        migrations.CreateModel(
            name='ThematicArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThematicAreaTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_tagged_items', to='contenttypes.contenttype', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='trainings.thematicarea')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ContentTrainee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('rate', models.IntegerField(null=True)),
                ('badge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainings.badge')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainings.content')),
                ('trainee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.trainee')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='thematic_area',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='trainings.ThematicAreaTag', to='trainings.ThematicArea', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='content',
            name='trainees',
            field=models.ManyToManyField(related_name='trainees', through='trainings.ContentTrainee', to='accounts.trainee'),
        ),
    ]
