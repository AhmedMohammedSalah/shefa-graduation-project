# Generated by Django 3.2.18 on 2023-05-01 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalAnalysis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicaltest',
            name='test_type',
        ),
        migrations.AddField(
            model_name='medicaltest',
            name='result',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
