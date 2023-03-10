# Generated by Django 3.1.6 on 2021-09-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0015_auto_20210928_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractprogress',
            name='time_elapsed_on_revise_schedule',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Time Elapsed based on revised schedule'),
        ),
        migrations.AlterField(
            model_name='contractprogress',
            name='time_extended_on_original_schedule',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Time Extended based on original Schedule'),
        ),
        migrations.AlterField(
            model_name='contractprogress',
            name='time_remaining_on_extended_schedule',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Time Remaining based on extended schedule'),
        ),
    ]
