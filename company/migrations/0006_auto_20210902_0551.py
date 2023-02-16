# Generated by Django 3.1.6 on 2021-09-02 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20210829_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnail', verbose_name='Thumbnail'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Title'),
        ),
    ]