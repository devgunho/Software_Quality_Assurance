# Generated by Django 2.0.4 on 2018-05-09 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logperform', '0002_auto_20180503_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Performagent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='에이전트이름')),
                ('agentfile', models.FileField(blank=True, upload_to='', verbose_name='에이전트파일')),
            ],
        ),
        migrations.RenameModel(
            old_name='Agent',
            new_name='Logagent',
        ),
    ]