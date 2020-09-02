# Generated by Django 2.2.4 on 2020-09-02 03:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0040_auto_20200902_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='boost',
            name='area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='boost',
            name='bathrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='boost',
            name='bedrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='boost',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='boost',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 9, 2, 3, 24, 11, 659637, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boost',
            name='rooms',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]