# Generated by Django 3.1.6 on 2021-09-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0005_remove_contract_date_of_completion_revised'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='date_of_completion_revised',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Completion (Revised)'),
        ),
    ]
