# Generated by Django 4.0.1 on 2022-09-06 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='table',
            name='is_reserved',
            field=models.BooleanField(default=False),
        ),
    ]
