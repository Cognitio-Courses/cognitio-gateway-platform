# Generated by Django 4.1.1 on 2022-09-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_contentcreator_role_trainee_role_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skilllevel',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]