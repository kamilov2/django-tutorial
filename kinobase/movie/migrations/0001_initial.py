# Generated by Django 5.0.4 on 2024-04-22 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('actor', models.BooleanField(default=False)),
                ('director', models.BooleanField(default=False)),
                ('producer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Guest', max_length=150)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(blank=True, upload_to='posters/%Y/%B')),
                ('name', models.CharField(max_length=150)),
                ('origin_name', models.CharField(blank=True, max_length=150)),
                ('year', models.PositiveSmallIntegerField(default=0)),
                ('quality', models.CharField(blank=True, choices=[('ts', 'TS'), ('bdrip', 'BDRIP'), ('hdrip', 'HDRIP')], max_length=150)),
                ('duration', models.CharField(blank=True, max_length=150)),
                ('short_description', models.TextField(blank=True)),
                ('sd_file_url', models.URLField(blank=True)),
                ('hd_file_url', models.URLField(blank=True)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('imdb_rating', models.PositiveIntegerField(default=0)),
                ('kp_rating', models.PositiveIntegerField(default=0)),
                ('author', models.ManyToManyField(null=True, related_name='movies', to='movie.author')),
                ('genres', models.ManyToManyField(null=True, to='movie.genre')),
            ],
        ),
    ]
