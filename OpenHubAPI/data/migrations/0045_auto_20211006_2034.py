# Generated by Django 3.2.5 on 2021-10-06 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0044_auto_20211006_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatransformerconstants',
            name='data_transformer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.datatransformer'),
        ),
        migrations.AlterField(
            model_name='hardwaredatatransformer',
            name='data_transformer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.datatransformer'),
        ),
        migrations.AlterField(
            model_name='hardwarestatsdatatransformer',
            name='data_transformer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.datatransformer'),
        ),
    ]
