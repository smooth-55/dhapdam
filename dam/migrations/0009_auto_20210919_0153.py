# Generated by Django 3.1.6 on 2021-09-19 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dam', '0008_auto_20210918_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractdetail',
            name='contract_amount_with_VAT',
            field=models.DecimalField(decimal_places=5, max_digits=20, verbose_name='Contract AMount with VAT'),
        ),
    ]