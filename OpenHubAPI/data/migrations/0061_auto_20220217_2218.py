# Generated by Django 3.2.9 on 2022-02-17 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0060_auto_20220125_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelStatDataPoint',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('value', models.IntegerField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('channel', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.channel')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='calibrationconstants',
            name='calibration',
        ),
        migrations.DeleteModel(
            name='Calibration',
        ),
        migrations.DeleteModel(
            name='CalibrationConstants',
        ),
    ]