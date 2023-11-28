# Generated by Django 3.2.11 on 2022-11-23 15:04

from django.db import migrations, models, connection

import models_logging.models


def forwards_func(apps, schema_editor):
    if connection.schema_name == "public":
        return


class Migration(migrations.Migration):

    dependencies = [
        ("models_logging", "0007_migrate_old_fields"),
    ]

    operations = [
        migrations.RunPython(forwards_func),
        migrations.AddField(
            model_name="change",
            name="extras",
            field=models.JSONField(
                blank=True,
                default=dict,
                encoder=models_logging.models.get_encoder,
                null=True,
            ),
        ),
    ]
