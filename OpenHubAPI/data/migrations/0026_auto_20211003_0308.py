# Generated by Django 3.2.5 on 2021-10-03 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0025_auto_20211003_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='datatransformer',
            name='type',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='hardwaredatatransformer',
            name='index',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
