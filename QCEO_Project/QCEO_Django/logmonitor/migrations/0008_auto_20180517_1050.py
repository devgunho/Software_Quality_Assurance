# Generated by Django 2.0.4 on 2018-05-17 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logmonitor', '0007_auto_20180517_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoringproduct',
            name='product',
            field=models.CharField(max_length=30, unique=True, verbose_name='제품'),
        ),
    ]