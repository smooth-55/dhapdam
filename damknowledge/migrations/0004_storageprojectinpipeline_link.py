# Generated by Django 3.1.6 on 2021-10-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('damknowledge', '0003_auto_20210930_0815'),
    ]

    operations = [
        migrations.AddField(
            model_name='storageprojectinpipeline',
            name='link',
            field=models.URLField(max_length=800, null=True, verbose_name='Link'),
        ),
    ]
