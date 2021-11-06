# Generated by Django 3.2.5 on 2021-11-05 15:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0048_alter_datatransformerconstants_data_transformer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelStats',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255, null=True)),
                ('value', models.FloatField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('channel', models.ManyToManyField(to='data.Channel')),
            ],
        ),
        migrations.RemoveField(
            model_name='hardwarestats',
            name='hardware',
        ),
        migrations.AddField(
            model_name='datatransformer',
            name='channels',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='data.Channel'),
        ),
        migrations.DeleteModel(
            name='HardwareDataTransformer',
        ),
        migrations.DeleteModel(
            name='HardwareStats',
        ),
        migrations.DeleteModel(
            name='HardwareStatsDataTransformer',
        ),
        migrations.AddField(
            model_name='datatransformer',
            name='channel_stats',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='data.ChannelStats'),
        ),
        migrations.AddIndex(
            model_name='channelstats',
            index=models.Index(fields=['id'], name='data_channe_id_d04541_idx'),
        ),
    ]
