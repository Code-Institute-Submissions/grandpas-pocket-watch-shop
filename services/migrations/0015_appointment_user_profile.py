# Generated by Django 3.1 on 2020-09-22 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('services', '0014_auto_20200918_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='appointments', to='profiles.userprofile'),
        ),
    ]
