# Generated by Django 3.1.6 on 2021-09-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20210906_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='link',
            field=models.URLField(max_length=500, null=True, verbose_name='Videos Url'),
        ),
    ]
