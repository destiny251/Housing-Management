# Generated by Django 2.2.4 on 2020-09-02 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0044_boost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boost',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]