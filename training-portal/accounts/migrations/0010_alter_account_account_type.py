# Generated by Django 4.1.1 on 2022-09-29 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_account_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('trainee', 'Trainee'), ('content_creator', 'Content Creator')], default='trainee', max_length=50),
        ),
    ]
