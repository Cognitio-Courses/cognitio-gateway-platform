# Generated by Django 4.1.1 on 2022-09-26 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_trainee_thematic_area'),
        ('trainings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='accounts.contentcreator'),
        ),
    ]
