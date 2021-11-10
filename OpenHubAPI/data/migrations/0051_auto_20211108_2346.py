# Generated by Django 3.2.5 on 2021-11-08 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0050_auto_20211106_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='nickname',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.RemoveField(
            model_name='channelstats',
            name='channel',
        ),
        migrations.AddField(
            model_name='channelstats',
            name='channel',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.channel'),
        ),
        migrations.AlterField(
            model_name='channelstats',
            name='type',
            field=models.CharField(choices=[('MIN', 'MIN'), ('MAX', 'MAX')], default='MIN', max_length=25),
        ),
    ]
