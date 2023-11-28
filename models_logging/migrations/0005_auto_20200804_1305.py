# Generated by Django 2.2.2 on 2020-08-04 13:05
from django.db import migrations, models, connection
import django.db.models.deletion
import models_logging.models
from models_logging.settings import LOGGING_USER_MODEL


def forwards_func(apps, schema_editor):
    if connection.schema_name == 'public':
        return
    

operations = [
    migrations.RunPython(forwards_func),
    migrations.AlterField(
        model_name='change',
        name='user',
        field=models.ForeignKey(blank=True, help_text='The user who created this changes.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=LOGGING_USER_MODEL, verbose_name='User'),
    ),
    migrations.AlterField(
        model_name='revision',
        name='comment',
        field=models.TextField(blank=True, help_text='A text comment on this revision.', verbose_name='comment'),
    ),
    migrations.RemoveField(
        model_name='change',
        name='comment',
    ),
]

class Migration(migrations.Migration):

    dependencies = [
        ('models_logging', '0004_auto_20171124_1445'),
    ]

    operations = operations
