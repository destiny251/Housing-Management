# Generated by Django 2.2.4 on 2020-08-23 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0019_tour'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='phone',
            field=models.TextField(blank=True, null=True),
        ),
    ]
