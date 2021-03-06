# Generated by Django 2.2.4 on 2020-08-20 21:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('email', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='property',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 8, 20, 21, 23, 33, 932433, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
