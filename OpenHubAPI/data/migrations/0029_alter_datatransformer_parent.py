# Generated by Django 3.2.5 on 2021-10-04 18:41

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0028_auto_20211004_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datatransformer',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.datatransformer'),
        ),
    ]