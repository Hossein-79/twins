# Generated by Django 4.1 on 2022-08-16 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twins', '0002_application_check_date_application_last_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='badge',
        ),
        migrations.RemoveField(
            model_name='application',
            name='commit_id',
        ),
        migrations.RemoveField(
            model_name='application',
            name='last_check',
        ),
        migrations.AddField(
            model_name='application',
            name='commit_hash',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='application',
            name='owner_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='application',
            name='repository_name',
            field=models.CharField(max_length=64),
        ),
    ]
