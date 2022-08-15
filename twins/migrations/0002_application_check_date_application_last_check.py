# Generated by Django 4.1 on 2022-08-15 06:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('twins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='check_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='last_check',
            field=models.DateField(auto_now=True),
        ),
    ]
