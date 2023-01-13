# Generated by Django 4.1.4 on 2023-01-05 00:26

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("musker", "0002_profile_date_modified"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="date_joined",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name=django.contrib.auth.models.User,
            ),
            preserve_default=False,
        ),
    ]
