# Generated by Django 3.1.6 on 2021-07-04 08:48

import contracts.models
from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_auto_20210704_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='date_of_completion_revised',
            field=jsonfield.fields.JSONField(blank=True, default=contracts.models.revised_completion, null=True, verbose_name='Date of Completion (Revised)'),
        ),
    ]
