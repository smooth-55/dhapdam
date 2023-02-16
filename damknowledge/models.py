from django.db import models

# Create your models here.
class DamLiteraures(models.Model):
    """
    Model to store the dam literatures description
    """

    title = models.CharField(("Title"), max_length=100, null=True)
    link = models.URLField(("Link"), max_length=800, null=True,blank=True)
    files = models.FileField(("File"),upload_to="damliteratures/image/",null=True,blank=True)

    def __str__(self):
        return "dam literures of" + " " + self.title

    class Meta:
        ordering = ["-id"]
        db_table = "dam_literatures"


class DamSalientFeatures(models.Model):
    """
    Model to store the salient features of dam
    """

    name_of_dam_or_reservoir = models.CharField(max_length=50)
    location = models.CharField(max_length=50, null=True, blank=True)
    main_purpose = models.CharField(max_length=50, null=True, blank=True)
    volume = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    height_of_dam = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True, blank=True
    )
    as_per_size = models.CharField(max_length=50,null=True, blank=True)
    as_per_construction_material = models.CharField(max_length=50)
    governing_icold_criteria_for_large_dams = models.CharField(
        max_length=120, null=True, blank=True
    )


    def __str__(self):
        return "dam salient features of" + " " + self.name_of_dam_or_reservoir

    class Meta:
        ordering = ["-id"]
        db_table = "dam_salient_features"


class StorageProjectInPipeline(models.Model):
    """
    Model to store the storage project in pipeline
    """

    name_of_dam_or_reservoir = models.CharField(max_length=50)
    location = models.CharField(max_length=50,null=True, blank=True)
    main_purpose = models.CharField(max_length=50, null=True, blank=True)
    volume_gross = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True, blank=True
    )
    height_of_dam = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True, blank=True
    )
    as_per_size = models.CharField(max_length=50,null=True, blank=True)
    as_per_construction_material = models.CharField(max_length=50)
    governing_icold_criteria_for_large_dams = models.CharField(
        max_length=120, null=True, blank=True
    )
    link = models.URLField(("Link"), max_length=800, null=True)


    def __str__(self):
        return "storage project in pipeline" + " " + self.name_of_dam_or_reservoir

    class Meta:
        ordering = ["-id"]
        db_table = "storage_project_in_pipeline"


class NameOfDam(models.Model):
    """
    Model to store the name of dam
    """

    title = models.CharField(("Title"), max_length=200, null=True)
    link = models.URLField(("Link"), max_length=800, null=True)

    def __str__(self):
        return "name of dam" + " " + self.title

    class Meta:
        ordering = ["-id"]
        db_table = "name_of_dam"


class Lake(models.Model):
    """
    Model to store name of lake
    """

    title = models.CharField(("Title"), max_length=150, null=True)
    link = models.URLField(("Link"), max_length=800, null=True)

    def __str__(self):
        return "name of lake" + " " + str(self.id)

    class Meta:
        ordering = ["-id"]
