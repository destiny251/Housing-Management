# Generated by Django 2.2.4 on 2020-08-20 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_property_sale_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='creator',
            field=models.TextField(blank=True, null=True),
        ),
    ]
