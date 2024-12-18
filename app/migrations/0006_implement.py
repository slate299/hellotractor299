# Generated by Django 4.2.16 on 2024-11-23 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_delete_seller'),
    ]

    operations = [
        migrations.CreateModel(
            name='Implement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(max_length=100)),
                ('images', models.ImageField(upload_to='implement_images/')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='implements', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
