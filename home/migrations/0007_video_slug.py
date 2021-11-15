# Generated by Django 3.2.6 on 2021-11-14 07:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20211114_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]