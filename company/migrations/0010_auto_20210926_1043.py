# Generated by Django 3.1.6 on 2021-09-26 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20210916_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='darta',
            name='date',
            field=models.CharField(max_length=80, verbose_name='Darta Date'),
        ),
        migrations.AlterField(
            model_name='darta',
            name='patra_received_date',
            field=models.CharField(max_length=80, verbose_name='Patra Received Date'),
        ),
    ]
