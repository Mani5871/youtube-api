# Generated by Django 3.2.6 on 2021-11-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_video_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.TextField(null=True),
        ),
    ]