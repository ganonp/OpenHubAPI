# Generated by Django 3.2.5 on 2021-10-03 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0023_auto_20211002_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datatransformer',
            name='data_transformer_child',
        ),
        migrations.AlterField(
            model_name='datatransformer',
            name='data_transformer_parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.datatransformer'),
        ),
    ]
