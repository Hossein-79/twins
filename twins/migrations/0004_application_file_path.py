# Generated by Django 4.1 on 2022-08-20 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twins', '0003_remove_application_badge_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='file_path',
            field=models.CharField(default='', max_length=64),
        ),
    ]
