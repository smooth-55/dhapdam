# Generated by Django 3.1.6 on 2021-07-02 07:02

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DesignAndQualityAspects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
            ],
            options={
                'verbose_name_plural': 'DesignAndQualityAspects',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=80, null=True, unique=True, verbose_name='Name of Project')),
                ('content', models.TextField(null=True, verbose_name='Content')),
                ('image', models.FileField(blank=True, null=True, upload_to='introduction')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Introduction',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='MajorWorkComponents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('image', models.ImageField(blank=True, null=True, upload_to='components')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('introduction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_components', to='dam.introduction')),
            ],
            options={
                'verbose_name_plural': 'MajorWorkComponents',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SubMajorWorkComponents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True, verbose_name='Title')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('major_work_components', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_major_work_components', to='dam.majorworkcomponents')),
            ],
            options={
                'verbose_name_plural': 'SubMajorWorkComponents',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SubDesignAndQualityAspects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True, verbose_name='Title')),
                ('sub_title', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=32), blank=True, size=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('design_and_quality_aspects', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subdesign_and_quality_aspects', to='dam.designandqualityaspects')),
            ],
            options={
                'verbose_name_plural': 'SubDesignAndQualityAspects',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SalientFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('dam_type', models.CharField(blank=True, max_length=80, null=True, verbose_name='Type of Dam')),
                ('location_of_dam', models.CharField(blank=True, max_length=200, null=True, verbose_name='Location of Dam')),
                ('dam_height', models.CharField(blank=True, max_length=80, null=True, verbose_name='Dam height (D/S toe to crest)\t')),
                ('dam_top_length', models.CharField(blank=True, max_length=80, null=True, verbose_name='Dam top Length (Crest Length)')),
                ('crest_width', models.CharField(blank=True, max_length=80, null=True, verbose_name='Dam crest elevation\t')),
                ('Concrete_face_thickness', models.CharField(blank=True, max_length=80, null=True, verbose_name='Concrete face thickness')),
                ('Freeboard', models.CharField(blank=True, max_length=80, null=True, verbose_name='Freeboard')),
                ('cost_of_project', models.CharField(blank=True, max_length=60, null=True, verbose_name='Cost of Project')),
                ('upstream_slope_inclination', models.CharField(blank=True, max_length=30, null=True, verbose_name='Upstream slope inclination')),
                ('downstream_slope_inclination', models.CharField(blank=True, max_length=30, null=True, verbose_name='Downstream slope inclination')),
                ('reservoir_volume', models.CharField(blank=True, max_length=30, null=True, verbose_name='Reservour Volume')),
                ('dam_volume', models.CharField(blank=True, max_length=30, null=True, verbose_name='Dam Volume')),
                ('full_supply_level', models.CharField(blank=True, max_length=100, null=True, verbose_name='Full Supply Level')),
                ('design_discharge', models.CharField(blank=True, max_length=30, null=True, verbose_name='Design Discharge')),
                ('power_of_production', models.CharField(blank=True, max_length=60, null=True, verbose_name='Power of Production')),
                ('normal_waterlevel', models.CharField(blank=True, max_length=60, null=True, verbose_name='Normal Water Level')),
                ('saddle_dam', models.CharField(blank=True, max_length=60, null=True, verbose_name='Saddle Dam')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('introduction', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salient_features', to='dam.introduction')),
            ],
            options={
                'verbose_name_plural': 'SalientFeatures',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True, verbose_name='Title')),
                ('image', models.FileField(upload_to='maps')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('introduction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maps', to='dam.introduction')),
            ],
            options={
                'verbose_name_plural': 'Maps',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='LocationAndAccessibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
                ('image', models.ImageField(upload_to='Location_and_accessibility')),
                ('accessibility_content', models.TextField(blank=True, null=True, verbose_name='Accessibility')),
                ('accessibility_image', models.ImageField(blank=True, null=True, upload_to='accessibility')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('introduction', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_and_accessibility', to='dam.introduction')),
            ],
            options={
                'verbose_name_plural': 'LocationAndAccessibility',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='EnvironmentalAspects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=60, null=True, verbose_name='Title')),
                ('content', models.TextField(null=True, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('introduction', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='environmental_aspects', to='dam.introduction')),
            ],
            options={
                'verbose_name_plural': 'EnvironmentalAspects',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='designandqualityaspects',
            name='introduction',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='design_and_quality_aspects', to='dam.introduction'),
        ),
        migrations.CreateModel(
            name='ContractDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Content')),
                ('Name_of_work', models.CharField(max_length=60, verbose_name='Name of Work')),
                ('client', models.CharField(max_length=60, verbose_name='Clinet')),
                ('contract_no', models.CharField(max_length=60, unique=True, verbose_name='Contract No')),
                ('name_of_contractor', models.CharField(blank=True, max_length=60, null=True, verbose_name='Name of Contractor')),
                ('date_of_agreement', models.DateField(blank=True, null=True, verbose_name='Date of Agreement')),
                ('intial_date_of_completion', models.DateField(blank=True, null=True, verbose_name='Intial date of completion')),
                ('revised_date_of_completion', models.DateField(blank=True, null=True, verbose_name='revised date of completion')),
                ('contract_amount_with_VAT', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Contract AMount with VAT')),
                ('physical_progress', models.CharField(blank=True, max_length=60, null=True, verbose_name='Physical Progress')),
                ('financial_progress', models.CharField(blank=True, max_length=60, null=True, verbose_name='Financial Progress')),
                ('responsible_person', models.CharField(blank=True, max_length=60, null=True, verbose_name='Responsible Person')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('introduction', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_details', to='dam.introduction')),
            ],
            options={
                'verbose_name_plural': 'ContractDetail',
                'ordering': ['-id'],
            },
        ),
    ]
