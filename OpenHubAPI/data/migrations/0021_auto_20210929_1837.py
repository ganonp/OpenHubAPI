# Generated by Django 3.2.5 on 2021-08-14 18:37

from django.db import migrations


def gen(apps, schema_editor):
    from data.models.models import HardwareChannelTypes

    hardware_channel_types = [('DHT22', 'DHT22Humidity'),
                              ('DHT22', 'DHT22Temp'),
                              ('MCP3008', 'MCP3008Analog'),
                              ('ModProbe', 'ModProbeTemp'),
                              ('VEML7700', 'VEML7700Light'),
                              ('VEML7700', 'VEML7700Lux')
                              ]

    for (hard, channel) in hardware_channel_types:
        cat = HardwareChannelTypes.objects.create()
        cat.hardware_type = hard
        cat.channel_type = channel
        cat.save()


class Migration(migrations.Migration):
    dependencies = [
        ('data', '0020_auto_20210924_1837'),
    ]

    operations = [
        migrations.RunPython(gen, reverse_code=migrations.RunPython.noop),
    ]
