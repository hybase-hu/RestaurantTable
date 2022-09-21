# Generated by Django 4.0.1 on 2022-09-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_food_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.CharField(choices=[('1', 'starter'), ('2', 'soup'), ('3', 'main'), ('4', 'pizza'), ('5', 'hamburger'), ('6', 'dessert'), ('7', 'wine'), ('8', 'beer')], max_length=2),
        ),
    ]
