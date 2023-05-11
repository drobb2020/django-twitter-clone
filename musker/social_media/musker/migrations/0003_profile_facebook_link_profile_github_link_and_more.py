# Generated by Django 4.1.4 on 2023-05-03 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("musker", "0002_meep_likes_alter_profile_profile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="facebook_link",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="github_link",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="homepage_link",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="linkedin_link",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="profile_bio",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]