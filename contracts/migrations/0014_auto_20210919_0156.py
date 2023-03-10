# Generated by Django 3.1.6 on 2021-09-19 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0013_auto_20210918_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='actual_expenditure',
            field=models.DecimalField(decimal_places=5, max_digits=20, verbose_name='Actual expenditure'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='amount',
            field=models.DecimalField(decimal_places=5, max_digits=20, verbose_name='Amount of agreement'),
        ),
        migrations.AlterField(
            model_name='contractprogress',
            name='financial_percent_amount',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=30, null=True, verbose_name='Financial Percent Amount'),
        ),
        migrations.AlterField(
            model_name='contractprogress',
            name='financial_progress_amount',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=30, null=True, verbose_name='Financial Percent Amount'),
        ),
        migrations.AlterField(
            model_name='contractprogress',
            name='physical_percent_amount',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=30, null=True, verbose_name='Physical Percent Amount'),
        ),
    ]
