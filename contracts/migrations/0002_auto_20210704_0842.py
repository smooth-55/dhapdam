# Generated by Django 3.1.6 on 2021-07-04 08:42

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='date_of_completion_revised',
            field=jsonfield.fields.JSONField(blank=True, null=True, verbose_name='Date of Completion (Revised)'),
        ),
    ]
