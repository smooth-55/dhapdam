# Generated by Django 3.1.6 on 2021-09-27 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_auto_20210927_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='darta',
            name='medium',
            field=models.CharField(choices=[('E', 'Email'), ('H', 'Hard Copy')], max_length=20, null=True),
        ),
    ]
