# Generated by Django 2.2.4 on 2020-09-02 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0048_auto_20200902_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='boost',
            name='time',
            field=models.TextField(default='1'),
            preserve_default=False,
        ),
    ]