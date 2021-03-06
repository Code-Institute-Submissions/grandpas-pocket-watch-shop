# Generated by Django 3.1 on 2020-09-16 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_auto_20200916_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.appointmenttype'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='email',
            field=models.EmailField(max_length=70),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='name',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='watch_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.watchmodel'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='watch_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.watchtype'),
        ),
    ]
