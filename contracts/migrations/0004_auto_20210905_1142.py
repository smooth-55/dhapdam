# Generated by Django 3.1.6 on 2021-09-05 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0003_auto_20210704_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='date_of_completion_revised',
            field=models.DateField(blank=True, null=True, verbose_name='Date of Completion (Revised)'),
        ),
    ]
