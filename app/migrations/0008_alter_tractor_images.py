# Generated by Django 4.2.16 on 2024-11-24 19:24

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_implement_description_implement_compatibility_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tractor',
            name='images',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='tractor_images'),
        ),
    ]
