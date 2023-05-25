# Generated by Django 4.2.1 on 2023-05-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_customuser_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'ذكر'), ('female', 'أنثى')], default='male', max_length=10, null=True),
        ),
    ]