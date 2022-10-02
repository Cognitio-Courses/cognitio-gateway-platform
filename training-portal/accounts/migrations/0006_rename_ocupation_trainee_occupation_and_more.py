# Generated by Django 4.1.1 on 2022-09-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_persona_trainee_location_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainee',
            old_name='ocupation',
            new_name='occupation',
        ),
        migrations.AddField(
            model_name='contentcreator',
            name='location',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contentcreator',
            name='organization',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]