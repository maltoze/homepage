# Generated by Django 2.2.4 on 2019-08-21 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelog', '0002_auto_20190821_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travellog',
            name='plan_time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='travellog',
            name='travel_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]