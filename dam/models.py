from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class DamIntroduction(models.Model):
    """Model describes the project name"""

    project_name = models.CharField(
        ("Name of Project"), max_length=80, null=True, blank=True, unique=True
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "DamIntroduction"

    def __str__(self):
        return str(self.id)


class IntroductionOfDam(models.Model):
    """Model to store intoduction of dam"""
    introduction = models.OneToOneField(
        DamIntroduction,
        on_delete=models.CASCADE,
        related_name="introduction_of_dam",
        null=True,
        blank=True,
    )
    content = models.TextField(("Content"), null=True)
    image = models.FileField(upload_to="introduction", null=True, blank=True)
    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "IntroductionOfDam"

    def __str__(self):
        return  str(self.id)


class SalientFeatures(models.Model):
    """Model  to store the features of project"""

    introduction = models.OneToOneField(
        DamIntroduction,
        on_delete=models.CASCADE,
        related_name="salient_features",
        null=True,
        blank=True,
    )
    # common attributes
    content = models.TextField(("Content"), null=True, blank=True)
    dam_type = models.CharField(("Type of Dam"), max_length=80, null=True, blank=True)
    location_of_dam = models.CharField(
        ("Location of Dam"), max_length=200, null=True, blank=True
    )
    dam_height = models.CharField(
        ("Dam height (D/S toe to crest)	"), max_length=80, null=True, blank=True
    )
    dam_top_length = models.CharField(
        ("Dam top Length (Crest Length)"), max_length=80, null=True, blank=True
    )
    dam_crest_elevation = models.CharField(
        ("Dam crest elevation"), max_length=80, null=True, blank=True
    )
    crest_width = models.CharField(
        ("Crest Width"), max_length=80, null=True, blank=True
    )
    Concrete_face_thickness = models.CharField(
        ("Concrete face thickness"), max_length=80, null=True, blank=True
    )
    Freeboard = models.CharField(("Freeboard"), max_length=80, null=True, blank=True)
    cost_of_project = models.CharField(
        ("Cost of Project"), max_length=60, null=True, blank=True
    )
    # separate attributes
    upstream_slope_inclination = models.CharField(
        ("Upstream slope inclination"), max_length=30, null=True, blank=True
    )
    downstream_slope_inclination = models.CharField(
        ("Downstream slope inclination"), max_length=30, null=True, blank=True
    )
    reservoir_volume = models.CharField(
        ("Reservour Volume"), max_length=30, null=True, blank=True
    )
    reservoir_surface_area_at_fsl = models.CharField(
        ("Reservoir surface area at FSL"), max_length=30, null=True, blank=True
    )
    dam_volume = models.CharField(("Dam Volume"), max_length=30, null=True, blank=True)
    full_supply_level = models.CharField(
        ("Full Supply Level"), max_length=100, null=True, blank=True
    )
    design_discharge = models.CharField(
        ("Design Discharge"), max_length=30, null=True, blank=True
    )
    power_of_production = models.CharField(
        ("Power of Production"), max_length=60, null=True, blank=True
    )
    normal_waterlevel = models.CharField(
        ("Normal Water Level"), max_length=60, null=True, blank=True
    )
    saddle_dam = models.CharField(("Saddle Dam"), max_length=60, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "SalientFeatures"

    def __str__(self):
        return str(self.id)


class LocationAndAccessibility(models.Model):
    """Model to store location of project and accessibility"""

    introduction = models.OneToOneField(
        DamIntroduction,
        on_delete=models.CASCADE,
        related_name="location_and_accessibility",
        null=True,
        blank=True,
    )
    content = models.TextField(("Content"))
    image = models.ImageField(upload_to="Location_and_accessibility")
    # in case of accessibility
    accessibility_content = models.TextField(("Accessibility"), null=True, blank=True)
    accessibility_image = models.ImageField(
        upload_to="accessibility", null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "LocationAndAccessibility"

    def __str__(self):
        return self.introduction.project_name + "" + str(self.id)



class MajorWorkComponentsDhapDam(models.Model):
    """Model to store major work components for dhapdam"""
    DAMTYPE = (
        ("M", "Main Dam"),
        ("S", "Saddle Dam")
    )

    introduction = models.ForeignKey(
        DamIntroduction,
        on_delete=models.CASCADE,
        related_name="work_components_dhapdam",
        null=True,
        blank=True,
    )
    sub_dam = models.CharField(
        ("Work Components Dam Type"), max_length=2, choices=DAMTYPE, null=True
    ) #main dam or saddle dam
    title = models.CharField(("Sub Dam Name"),max_length=60)
    image = models.FileField(upload_to="components") #filefield as it may required  pdf too in future
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "MajorWorkComponents Dhapdam"

    def __str__(self):
        return self.sub_dam + "" + str(self.title)



class MajorWorkComponents(models.Model):
    """Model to store major work components for nagmati"""

    introduction = models.ForeignKey(
        DamIntroduction,
        on_delete=models.CASCADE,
        related_name="work_components",
        null=True,
        blank=True,
    )
    title = models.TextField(("Title"))
    image = models.ImageField(upload_to="components", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "MajorWorkComponents"

    def __str__(self):
        return self.title + "" + str(self.id)


class SubMajorWorkComponents(models.Model):
    major_work_components = models.ForeignKey(
        MajorWorkComponents,
        on_delete=models.CASCADE,
        related_name="sub_major_work_components",
        null=True,
        blank=True,
    )
    title = models.CharField(("Title"), max_length=60, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "SubMajorWorkComponents"

    def __str__(self):
        return self.major_work_components.title + "" + str(self.id)


class ContractDetail(models.Model):
    """Model to store contract details"""

    introduction = models.OneToOneField(
        DamIntroduction,
        on_delete=models.CASCADE,
        related_name="contract_details",
        null=True,
        blank=True,
    )
    content = models.TextField(("Content"))
    Name_of_work = models.CharField(
        ("Name of Work"),
        max_length=250,
    )
    client = models.CharField(("Client"), max_length=60)
    contract_no = models.CharField(("Contract No"), max_length=60, unique=True)
    name_of_contractor = models.CharField(
        ("Name of Contractor"), max_length=60, null=True, blank=True
    )
    date_of_agreement = models.DateField(("Date of Agreement"), null=True, blank=True)
    intial_date_of_completion = models.DateField(
        ("Intial date of completion"), null=True, blank=True
    )
    revised_date_of_completion = models.DateField(
        ("revised date of completion"), null=True, blank=True
    )
    contract_amount_with_VAT = models.DecimalField(
        ("Contract AMount with VAT"), max_digits=20, decimal_places=5
    )
    physical_progress = models.CharField(
        ("Physical Progress"), max_length=60, null=True, blank=True
    )
    financial_progress = models.CharField(
        ("Financial Progress"), max_length=60, null=True, blank=True
    )
    responsible_person = models.CharField(
        ("Responsible Person"), max_length=60, null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "ContractDetail"

    def __str__(self):
        return self.introduction.project_name + "" + str(self.id)


class DesignAndQualityAspects(models.Model):
    """Model to store Design and Quality Aspects"""

    introduction = models.OneToOneField(
        DamIntroduction,
        on_delete=models.CASCADE,
        related_name="design_and_quality_aspects",
        null=True,
        blank=True,
    )
    content = models.TextField(("Content"))

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "DesignAndQualityAspects"

    def __str__(self):
        return self.introduction.project_name


class SubDesignAndQualityAspects(models.Model):
    """ "model to store the sub category of design and quality aspects"""

    design_and_quality_aspects = models.ForeignKey(
        DesignAndQualityAspects,
        on_delete=models.CASCADE,
        related_name="subdesign_and_quality_aspects",
        null=True,
        blank=True,
    )
    title = models.CharField(("Title"), max_length=60, null=True, blank=True)
    sub_title = ArrayField(
        models.CharField(max_length=32),blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "SubDesignAndQualityAspects"

    def __str__(self):
        return str(self.id)


class EnvironmentalAspects(models.Model):
    """ "model to store the environmental aspects and present status of project"""

    introduction = models.OneToOneField(
        DamIntroduction,
        on_delete=models.CASCADE,
        related_name="environmental_aspects",
        null=True,
        blank=True,
    )
    title = models.CharField(("Title"), max_length=60, null=True, blank=True)
    content = models.TextField(("Content"), null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "EnvironmentalAspects"

    def __str__(self):
        return str(self.id)


class Maps(models.Model):
    """ "model to store map of  project"""

    introduction = models.ForeignKey(
        DamIntroduction,
        on_delete=models.CASCADE,
        related_name="maps",
        null=True,
        blank=True,
    )
    title = models.CharField(("Title"), max_length=60, null=True, blank=True)
    image = models.FileField(upload_to="maps")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]
        verbose_name_plural = "Maps"

    def __str__(self):
        return self.introduction.project_name + "" + str(self.id)
