# Generated by Django 3.1.6 on 2021-10-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dam', '0009_auto_20210919_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majorworkcomponents',
            name='title',
            field=models.TextField(verbose_name='Title'),
        ),
    ]