# Generated by Django 4.0.2 on 2022-02-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_short_intro_profile_social_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]