# Generated by Django 5.0.6 on 2024-07-12 10:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2024, 7, 12, 10, 42, 34, 104632, tzinfo=datetime.timezone.utc), max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2024, 7, 12, 10, 42, 37, 511011, tzinfo=datetime.timezone.utc), max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2024, 7, 12, 10, 42, 40, 86836, tzinfo=datetime.timezone.utc), max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
