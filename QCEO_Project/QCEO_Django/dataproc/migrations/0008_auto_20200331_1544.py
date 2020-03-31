# Generated by Django 3.0.4 on 2020-03-31 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataproc', '0007_auto_20180615_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='project',
            field=models.CharField(blank=True, choices=[('SecuMS', 'SecuMS'), ('UniTy UNIX', 'OmniGuard Unix'), ('UAC for Windows(SE)', 'OmniGuard Windows'), ('FOSSGuard', 'FOSSGuard'), ('Athena Dev', 'Athena')], max_length=30, verbose_name='프로젝트'),
        ),
        migrations.AlterField(
            model_name='process',
            name='project',
            field=models.CharField(choices=[('SecuMS', 'SecuMS'), ('OmniGuard Unix', 'OmniGuard Unix'), ('OmniGuard Windows', 'OmniGuard Windows'), ('FOSSGuard', 'FOSSGuard'), ('Athena', 'Athena')], max_length=30, verbose_name='프로젝트'),
        ),
    ]
