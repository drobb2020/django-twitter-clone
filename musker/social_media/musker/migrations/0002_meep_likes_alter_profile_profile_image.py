# Generated by Django 4.1.4 on 2023-04-05 21:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("musker", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="meep",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]
