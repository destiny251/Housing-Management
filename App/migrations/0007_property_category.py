# Generated by Django 2.2.4 on 2020-08-20 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_article_summmary'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='category',
            field=models.TextField(blank=True, null=True),
        ),
    ]
