# Generated by Django 3.2.5 on 2021-10-02 22:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0022_auto_20210929_1837'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataTransformer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('accessory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='data.accessory')),
                ('data_transformer_child', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='data_child', to='data.datatransformer')),
                ('data_transformer_parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_parent', to='data.datatransformer')),
            ],
        ),
        migrations.CreateModel(
            name='HardwareStats',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255, null=True)),
                ('value', models.FloatField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('hardware', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.hardware')),
            ],
        ),
        migrations.AddField(
            model_name='hub',
            name='keep_statistics',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.CreateModel(
            name='HardwareStatsDataTransformer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('index', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('data_transformer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.datatransformer')),
                ('hardware_stat', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.hardwarestats')),
            ],
        ),
        migrations.CreateModel(
            name='HardwareDataTransformer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('index', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('data_transformer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.datatransformer')),
                ('hardware', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.hardware')),
            ],
        ),
        migrations.CreateModel(
            name='DataTransformerConstants',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255, null=True)),
                ('index', models.IntegerField()),
                ('value', models.FloatField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('data_transformer', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.datatransformer')),
            ],
        ),
        migrations.AddIndex(
            model_name='hardwarestatsdatatransformer',
            index=models.Index(fields=['id', 'data_transformer'], name='data_hardwa_id_b714f1_idx'),
        ),
        migrations.AddIndex(
            model_name='hardwarestats',
            index=models.Index(fields=['id', 'hardware'], name='data_hardwa_id_5b03a1_idx'),
        ),
        migrations.AddIndex(
            model_name='hardwaredatatransformer',
            index=models.Index(fields=['id', 'data_transformer', 'hardware'], name='data_hardwa_id_c5fb61_idx'),
        ),
        migrations.AddIndex(
            model_name='datatransformerconstants',
            index=models.Index(fields=['id', 'data_transformer'], name='data_datatr_id_94efc8_idx'),
        ),
        migrations.AddIndex(
            model_name='datatransformer',
            index=models.Index(fields=['id', 'accessory'], name='data_datatr_id_9bcd89_idx'),
        ),
    ]