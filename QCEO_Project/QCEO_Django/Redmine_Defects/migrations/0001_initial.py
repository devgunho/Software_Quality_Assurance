# Generated by Django 3.0.4 on 2020-03-31 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RedmineDefects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(default=0)),
                ('project', models.TextField(blank=True)),
                ('proj_type', models.TextField(blank=True)),
                ('proj_status', models.TextField(blank=True)),
                ('priority', models.TextField(blank=True)),
                ('title', models.TextField(blank=True)),
                ('author', models.TextField(blank=True)),
                ('master', models.TextField(blank=True)),
                ('category', models.TextField(blank=True)),
                ('target_version', models.TextField(blank=True)),
                ('change', models.TextField(blank=True)),
                ('start_time', models.TextField(blank=True)),
                ('deadline', models.TextField(blank=True)),
            ],
        ),
    ]
