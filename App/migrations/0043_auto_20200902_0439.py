# Generated by Django 2.2.4 on 2020-09-02 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0042_auto_20200902_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='boost',
            name='price',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='boost',
            name='price_per_unit',
            field=models.TextField(blank=True, null=True),
        ),
    ]
