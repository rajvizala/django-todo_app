# Generated by Django 3.0 on 2023-01-14 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20230113_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_updated',
            field=models.TimeField(auto_now=True),
        ),
    ]
