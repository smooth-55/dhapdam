# Generated by Django 3.1.6 on 2021-12-22 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeprofile',
            name='date_joined',
            field=models.CharField(max_length=30, null=True, verbose_name='Join Date'),
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='leave_date',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Leave Date'),
        ),
    ]
