# Generated by Django 3.1.6 on 2021-09-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0009_auto_20210917_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractprogress',
            name='financial_progress_amount',
            field=models.DecimalField(blank=True, decimal_places=15, max_digits=30, null=True, verbose_name='Financial Percent Amount'),
        ),
    ]
