# Generated by Django 3.2.5 on 2021-10-03 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0024_auto_20211003_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hub',
            name='keep_statistics',
        ),
        migrations.AddField(
            model_name='channel',
            name='keep_statistics',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
