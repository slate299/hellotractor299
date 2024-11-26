# Generated by Django 4.2.16 on 2024-11-23 17:09

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_implement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='implement',
            name='description',
        ),
        migrations.AddField(
            model_name='implement',
            name='compatibility',
            field=models.CharField(default='unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='implement',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='implement',
            name='stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='implement',
            name='wishlist_users',
            field=models.ManyToManyField(blank=True, related_name='wishlist_implements', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='implement',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='implement',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='implements/'),
        ),
        migrations.AlterField(
            model_name='implement',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tractor',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tractor',
            name='wishlist_users',
            field=models.ManyToManyField(blank=True, related_name='wishlist_tractors', to=settings.AUTH_USER_MODEL),
        ),
    ]
