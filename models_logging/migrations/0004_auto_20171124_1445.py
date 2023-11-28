# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-24 11:45
from __future__ import unicode_literals

from django.db import migrations, models, connection


def forwards_func(apps, schema_editor):
    if connection.schema_name == 'public':
        return


class Migration(migrations.Migration):

    dependencies = [
        ('models_logging', '0003_auto_20170726_1552'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
        migrations.AlterField(
            model_name='change',
            name='object_id',
            field=models.IntegerField(help_text='Primary key of the model under version control.'),
        ),
    ]
