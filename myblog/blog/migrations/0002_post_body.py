# Generated by Django 5.0.4 on 2024-06-12 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default=datetime.datetime(2024, 6, 12, 11, 8, 58, 273246, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]