# Generated by Django 3.1.6 on 2021-09-16 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0006_contract_date_of_completion_revised'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractprogress',
            name='financial_percent_amount',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Financial Percent Amount'),
        ),
        migrations.AlterField(
            model_name='contractprogress',
            name='financial_progress_amount',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Financial Progress Amount'),
        ),
        migrations.AlterField(
            model_name='contractprogress',
            name='physical_percent_amount',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Physical Percent Amount'),
        ),
        migrations.AlterField(
            model_name='contractprogress',
            name='time_elapsed_on_revise_schedule',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Time Elapsed based on revised schedule'),
        ),
        migrations.AlterField(
            model_name='contractprogress',
            name='time_extended_on_original_schedule',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Time Extended based on original Schedule'),
        ),
        migrations.AlterField(
            model_name='contractprogress',
            name='time_remaining_on_extended_schedule',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Time Remaining based on extended schedule'),
        ),
    ]
