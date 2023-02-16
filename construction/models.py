from django.db import models


"""===================================
--------- Tests & QA/QC --------------
======================================"""

##----------------------- Material tests ----------------------------##


class CommonMaterialTests(models.Model):
    """
    Includes all the common attributes of Material tests  section
    """

    name_of_test = models.CharField(
        ("Name of Test"), max_length=100, null=True, blank=True
    )
    no_of_test = models.DecimalField(
        ("Number of Test"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    test_standard = models.CharField(
        ("Test Standard"), max_length=100, null=True, blank=True
    )
    remarks = models.TextField(("Remarks"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ("-id",)


class EarthFillingMaterial(CommonMaterialTests):
    """
    Earth Filling Material
    """

    pass

    def __str__(self):
        return "Earth Filling Material" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Earth Filling Material"


class FaceSlabBeddingMaterial2A(CommonMaterialTests):
    """
    Face slab Bedding Material 2A
    """

    pass

    def __str__(self):
        return "Face Slab Bedding Material 2A" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Face Slab Bedding Material 2A"


class FaceSlabBeddingMaterial2B(CommonMaterialTests):
    """
    Face slab Bedding Material 2B
    """

    pass

    def __str__(self):
        return "Face Slab Bedding Material 2B" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Face Slab Bedding Material 2B"


class SmallSizeRock300MM(CommonMaterialTests):
    """
    Small Size Rock Fill 300MM
    """

    pass

    def __str__(self):
        return "Small Size Rock Fill 300MM" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Small Size Rock Fill 300MM"


class SmallSizeRock600MM(CommonMaterialTests):
    """
    Small Size Rock Fill 600MM
    """

    pass

    def __str__(self):
        return "Small Size Rock Fill 600MM" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Small Size Rock Fill 600MM"


class SecondClassRock1000MM(CommonMaterialTests):
    """
    Second Class Rock 1000MM
    """

    pass

    def __str__(self):
        return "Second Class Rock 1000MM" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Second Class Rock 1000MM"


class RockFill(CommonMaterialTests):
    """
    Rock Fill
    """

    pass

    def __str__(self):
        return "Rock Fill" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Rock Fill"


class ConcreteAggregate40mm(CommonMaterialTests):
    """
    Concrete Aggregate(40mm)
    """

    pass

    def __str__(self):
        return "Concrete Aggregate (40mm)" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Concrete Aggregate(40mm)"


class ConcreteAggregate20mm(CommonMaterialTests):
    """
    Concrete Aggregate (20mm)
    """

    pass

    def __str__(self):
        return "Concrete Aggregate (20mm)" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Concrete Aggregate(20mm)"


class ConcreteAggregate10mm(CommonMaterialTests):
    """
    Concrete Aggregate (10mm)
    """

    pass

    def __str__(self):
        return "Concrete Aggregate (10mm)" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Concrete Aggregate(10mm)"


class FineAggregate(CommonMaterialTests):
    """
    Fine Aggregate
    """

    pass

    def __str__(self):
        return "FineAggregate" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "FineAggregate"


class Cement(CommonMaterialTests):
    """
    Cement
    """

    pass

    def __str__(self):
        return "Cement" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Cement"


class GranularSubBase(CommonMaterialTests):
    """
    Granular Sub base
    """

    pass

    def __str__(self):
        return "Granular Sub Base" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Granular Sub Base"


##----------------------- Material tests ends  ----------------------------##

##----------------------- work tests starts  ----------------------------##
class ConcreteTests(CommonMaterialTests):
    pass

    def __str__(self):
        return "Concrete Tests" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Concrete Tests"


class CompactionTests(CommonMaterialTests):
    pass

    def __str__(self):
        return "Compaction Tests" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Compaction Tests"


class GroutingTests(CommonMaterialTests):
    pass

    def __str__(self):
        return "Grouting Tests" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Grouting Tests"


class CopperWaterStopperTests(CommonMaterialTests):
    pass

    def __str__(self):
        return "Copper Water Stopper Tests" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Copper Water Stopper Tests"


class PermeabilityTests(CommonMaterialTests):
    pass

    def __str__(self):
        return "Permeability Tests" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Permeability Tests"


class Geophysical(CommonMaterialTests):
    pass

    def __str__(self):
        return "Geophysical Investigation" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "Geophysical Investigation"


class CoreDrilltest(models.Model):
    no_of_test = models.DecimalField(
        ("Number of Test"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    location = models.CharField(("Location"), max_length=200, null=True, blank=True)
    drilling_depth = models.DecimalField(
        ("Drilling Depth(m)"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    depth_slightly_weatherd_gneiss = models.DecimalField(
        ("Depth Slightly Weatherd Gneiss(m)"),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    coordinate = models.CharField(
        ("Co-ordinate"), max_length=200, null=True, blank=True
    )

    def __str__(self):
        return "Core Drill test" + " " + str(self.no_of_test)

    class Meta:
        verbose_name_plural = "Core Drill test"


##----------------------- work tests  ends ----------------------------##


##----------------------- QA,QC Documentation  starts----------------------------##


class QADocumentation(models.Model):
    name_of_test = models.CharField(
        ("Name of Test"), max_length=600, null=True, blank=True
    )
    no_of_test = models.DecimalField(
        ("Number of Test"), max_digits=10, decimal_places=2, null=True, blank=True
    )
    test_standard = models.CharField(
        ("Test Standard"), max_length=600, null=True, blank=True
    )
    remarks = models.TextField(("Remarks"), null=True, blank=True)

    def __str__(self):
        return "QADocumentation" + " " + self.name_of_test

    class Meta:
        verbose_name_plural = "QA/AC Documentation"


"""===================================
--------- Construction Equipment -----
====================================="""


class CommonConstruction(models.Model):
    """
    Includes all the common attributes of Construction equipment  section
    """

    description = models.TextField(("Description"), null=True, blank=True)
    specification = models.TextField(("Specification"), null=True, blank=True)
    quantity = models.IntegerField(("Quantity"), null=True, blank=True)
    remarks = models.TextField(("Remarks"), null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ("-id",)


class EarthMovingCompaction(CommonConstruction):
    """
    Earth Moving Compaction
    """

    def __str__(self):
        return "Earth Moving Compaction" + " " + str(self.id)

    class Meta:
        verbose_name_plural = "Earth Moving Compaction"


class ConcretingEquipments(CommonConstruction):
    """
    Concreting Equipments
    """

    def __str__(self):
        return "Concreting Equipments" + " " + str(self.id)

    class Meta:
        verbose_name_plural = "Concreting Equipments"


class GroutingEquipments(CommonConstruction):
    """
    Grouting Equipments
    """

    def __str__(self):
        return "Grouting Equipments" + " " + str(self.id)

    class Meta:
        verbose_name_plural = "Grouting Equipments"


class BrazingEquipments(CommonConstruction):
    """
    Brazing Equipments
    """

    def __str__(self):
        return "Brazing Equipments" + " " + str(self.id)

    class Meta:
        verbose_name_plural = "Brazing Equipments"


class SurveyEquipments(CommonConstruction):
    """
    Survey Equipments
    """

    def __str__(self):
        return "Survey Equipments" + " " + str(self.id)

    class Meta:
        verbose_name_plural = "Survey Equipments"


class LabEquipments(CommonConstruction):
    """
    Lab Equipments
    """

    def __str__(self):
        return "Lab Equipments" + " " + str(self.id)

    class Meta:
        verbose_name_plural = "Lab Equipments"


class GeophysicalInvestigationEquipments(CommonConstruction):
    """
    Geophysical Investigation Equipments
    """

    def __str__(self):
        return "Geophysical Investigation Equipments" + " " + str(self.id)

    class Meta:
        verbose_name_plural = "Geophysical Investigation Equipments"


"""===================================
--------- Design/Drawings---------
====================================="""


class Design(models.Model):
    """
    Design/Drawings
    """

    description = models.TextField(("Description"))
    no_of_revisions = models.IntegerField(("Number of Revisions"))
    name_of_major_work = models.CharField(("Name of Major Work"), max_length=200)
    remarks = models.TextField(("Remarks"), null=True, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ("-id",)
        verbose_name_plural = "Design/Drawings"


"""===================================
--------- Method of statements ---------
====================================="""


class MethodOfStatements(models.Model):
    """
    Methods of statements
    """

    description = models.TextField(("Description of Method of Statement"))
    no_of_revisions = models.IntegerField(("Number of Revisions"))
    name_of_major_work = models.CharField(
        ("Name of Major Work"),
        max_length=200,
    )
    remarks = models.TextField(("Remarks"), null=True, blank=True)

    class Meta:
        ordering = ("-id",)
        verbose_name_plural = "Methods of Statements"

    def __str__(self):
        return self.description


class Reports(models.Model):
    name_of_report = models.CharField(
        ("Name of Report"),
        max_length=200,
    )
    no_of_reports = models.IntegerField(("Number of Reports"))
    remarks = models.TextField(("Remarks"), null=True, blank=True)

    class Meta:
        ordering = ("-id",)
        verbose_name_plural = "Name of Report"

    def __str__(self):
        return self.name_of_report


"""===================================
--------------- Footages ---------
====================================="""


class Footages(models.Model):
    """
    Footages
    """

    name_of_work = models.CharField(("Name of Work"), max_length=100)
    url = models.URLField(("URL of file"), blank=True, null=True, max_length=300)
    duration_of_clip = models.CharField(("Duration of Clip"), max_length=100)
    remarks = models.TextField(("Remarks"), null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ("-id",)


class WorkFootages(Footages):
    """
    Work Footages
    """

    pass

    def __str__(self):
        return "Work Footages" + " " + self.name_of_work

    class Meta:
        verbose_name_plural = "Work Footages"


class TestFootages(Footages):
    """
    Test Footages
    """

    pass

    def __str__(self):
        return "Test Footages" + " " + self.name_of_work

    class Meta:
        verbose_name_plural = "Test Footages"
