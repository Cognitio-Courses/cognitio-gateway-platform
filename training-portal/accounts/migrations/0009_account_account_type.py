# Generated by Django 4.1.1 on 2022-09-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_skilllevel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.CharField(default='trainee', max_length=50),
        ),
    ]
