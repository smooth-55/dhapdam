# Generated by Django 3.1.6 on 2021-09-27 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('damknowledge', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='damliteraures',
            name='content',
        ),
        migrations.RemoveField(
            model_name='lake',
            name='content',
        ),
        migrations.RemoveField(
            model_name='nameofdam',
            name='content',
        ),
        migrations.AddField(
            model_name='damliteraures',
            name='link',
            field=models.URLField(max_length=800, null=True, verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='lake',
            name='link',
            field=models.URLField(max_length=800, null=True, verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='nameofdam',
            name='link',
            field=models.URLField(max_length=800, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='damliteraures',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='lake',
            name='title',
            field=models.CharField(max_length=150, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='nameofdam',
            name='title',
            field=models.CharField(max_length=200, null=True, verbose_name='Title'),
        ),
    ]