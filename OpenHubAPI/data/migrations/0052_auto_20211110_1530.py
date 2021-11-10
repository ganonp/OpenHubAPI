# Generated by Django 3.2.5 on 2021-08-14 18:37

from django.db import migrations

def gen(apps, schema_editor):
    from data.models.models import DataTransformerTypes

    types = ['INVERSE']

    for type in types:
        cat = DataTransformerTypes.objects.create()
        cat.type = type
        cat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('data', '0051_auto_20211108_2346'),
    ]

    operations = [
        migrations.RunPython(gen, reverse_code=migrations.RunPython.noop),
    ]