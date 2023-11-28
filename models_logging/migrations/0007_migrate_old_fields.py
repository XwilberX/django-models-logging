from django.db import migrations, models, connection
import models_logging.models


def forwards_func(apps, schema_editor):
    if connection.schema_name == 'public':
        return


class Migration(migrations.Migration):

    dependencies = [
        ('models_logging', '0006_auto_20211020_2036'),
    ]

    operations = [
        migrations.RunPython(forwards_func),
        migrations.AlterField(
            model_name='change',
            name='changed_data',
            field=models.JSONField(
                blank=True,
                encoder=models_logging.models.get_encoder,
                null=True
            ),
        )
    ]
