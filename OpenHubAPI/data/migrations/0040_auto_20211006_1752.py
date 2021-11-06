# Generated by Django 3.2.5 on 2021-10-06 17:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0039_auto_20211006_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatransformerconstants',
            name='id',
            field=models.UUIDField(blank=True, default=uuid.UUID('6a9f6e8a-da78-4395-9c01-6e769a63372d'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='hardwarestatsdatatransformer',
            name='id',
            field=models.UUIDField(blank=True, default=uuid.UUID('d59c951e-2990-4bb8-9d15-15a7160afdf1'), primary_key=True, serialize=False),
        ),
    ]
