# Generated by Django 4.2.16 on 2024-11-22 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tractor_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='description',
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
