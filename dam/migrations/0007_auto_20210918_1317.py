# Generated by Django 3.1.6 on 2021-09-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dam', '0006_auto_20210704_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractdetail',
            name='contract_amount_with_VAT',
            field=models.DecimalField(decimal_places=10, max_digits=20, verbose_name='Contract AMount with VAT'),
        ),
    ]
