# Generated by Django 4.0.1 on 2022-09-08 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_tableorder_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='count',
            field=models.IntegerField(default=1, max_length=20),
        ),
    ]
