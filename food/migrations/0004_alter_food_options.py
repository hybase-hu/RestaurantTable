# Generated by Django 4.0.1 on 2022-09-08 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_food_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['category', 'name']},
        ),
    ]
