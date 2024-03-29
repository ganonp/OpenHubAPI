# Generated by Django 3.2.3 on 2021-06-09 21:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255, null=True)),
                ('type', models.CharField(max_length=255, null=True)),
                ('display_name', models.CharField(max_length=255, null=True)),
                ('aid', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Calibration',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CalibrationConstants',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255, null=True)),
                ('value', models.CharField(max_length=255, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('channel_index', models.IntegerField(null=True)),
                ('type', models.CharField(max_length=15)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('DHT22', 'Dht22'), ('MCP3008', 'Mcp3008'), ('ModProbe', 'Modprobe'), ('PiPico', 'Pipico'), ('VEML7700', 'Veml7700')], default='PiPico', max_length=10)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HardwareChannelTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware_type', models.CharField(max_length=10)),
                ('channel_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DHT22',
            fields=[
                ('hardware_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.hardware')),
                ('pin', models.IntegerField()),
            ],
            bases=('data.hardware',),
        ),
        migrations.CreateModel(
            name='MCP3008',
            fields=[
                ('hardware_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.hardware')),
                ('sck', models.IntegerField()),
                ('miso', models.IntegerField()),
                ('cs_pin', models.IntegerField()),
                ('num_channels', models.IntegerField()),
            ],
            bases=('data.hardware',),
        ),
        migrations.CreateModel(
            name='ModProbe',
            fields=[
                ('hardware_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.hardware')),
                ('base_dir', models.CharField(max_length=100, null=True)),
                ('file_name', models.CharField(max_length=100, null=True)),
            ],
            bases=('data.hardware',),
        ),
        migrations.CreateModel(
            name='PiPico',
            fields=[
                ('hardware_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.hardware')),
                ('pi_gpio_interrupt', models.IntegerField()),
            ],
            bases=('data.hardware',),
        ),
        migrations.CreateModel(
            name='VEML7700',
            fields=[
                ('hardware_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.hardware')),
                ('scl', models.IntegerField()),
                ('sda', models.IntegerField()),
            ],
            bases=('data.hardware',),
        ),
        migrations.CreateModel(
            name='HardwareConfig',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255, null=True)),
                ('value', models.CharField(max_length=255, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hardware', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.hardware')),
            ],
        ),
        migrations.AddIndex(
            model_name='hardware',
            index=models.Index(fields=['id'], name='data_hardwa_id_792ac4_idx'),
        ),
        migrations.AddField(
            model_name='channel',
            name='hardware',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.hardware'),
        ),
        migrations.AddField(
            model_name='calibrationconstants',
            name='calibration',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='data.calibration'),
        ),
        migrations.AddField(
            model_name='calibration',
            name='accessory',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.accessory'),
        ),
        migrations.AddField(
            model_name='accessory',
            name='channels',
            field=models.ManyToManyField(to='data.Channel'),
        ),
        migrations.AddIndex(
            model_name='hardwareconfig',
            index=models.Index(fields=['id', 'hardware'], name='data_hardwa_id_9f4bd6_idx'),
        ),
        migrations.AddIndex(
            model_name='channel',
            index=models.Index(fields=['id', 'hardware'], name='data_channe_id_469160_idx'),
        ),
        migrations.AddIndex(
            model_name='calibrationconstants',
            index=models.Index(fields=['id'], name='data_calibr_id_0c5a5a_idx'),
        ),
        migrations.AddIndex(
            model_name='calibration',
            index=models.Index(fields=['id'], name='data_calibr_id_c3df15_idx'),
        ),
        migrations.AddIndex(
            model_name='accessory',
            index=models.Index(fields=['id'], name='data_access_id_df10ff_idx'),
        ),
    ]
