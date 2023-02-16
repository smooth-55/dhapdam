from django import forms
from django.forms import ModelForm

from .models import *


class CommonMaterialTestForm(ModelForm):
    class Meta:
        model = EarthFillingMaterial
        fields = "__all__"


class FaceSlab2AForm(ModelForm):
    class Meta:
        model = FaceSlabBeddingMaterial2A
        fields = "__all__"


class FaceSlab2BForm(ModelForm):
    class Meta:
        model = FaceSlabBeddingMaterial2B
        fields = "__all__"


class SmallSizeRock300MMForm(ModelForm):
    class Meta:
        model = SmallSizeRock300MM
        fields = "__all__"


class SmallSizeRock600MMForm(forms.ModelForm):
    class Meta:
        model = SmallSizeRock600MM
        fields = "__all__"


class SecondClassRock1000MMForm(forms.ModelForm):
    class Meta:
        model = SecondClassRock1000MM
        fields = "__all__"


class RockFillForm(forms.ModelForm):
    class Meta:
        model = RockFill
        fields = "__all__"


class ConcreteAggregate40mmForm(forms.ModelForm):
    class Meta:
        model = ConcreteAggregate40mm
        fields = "__all__"


class ConcreteAggregate20mmForm(forms.ModelForm):
    class Meta:
        model = ConcreteAggregate20mm
        fields = "__all__"


class ConcreteAggregate10mmForm(forms.ModelForm):
    class Meta:
        model = ConcreteAggregate10mm
        fields = "__all__"


class FineAggregateForm(forms.ModelForm):
    class Meta:
        model = FineAggregate
        fields = "__all__"


class CementForm(forms.ModelForm):
    class Meta:
        model = Cement
        fields = "__all__"


class GranularSubBaseForm(forms.ModelForm):
    class Meta:
        model = GranularSubBase
        fields = "__all__"


class ConcreteTestsForm(forms.ModelForm):
    class Meta:
        model = ConcreteTests
        fields = "__all__"


class CompactionTestsForm(forms.ModelForm):
    class Meta:
        model = CompactionTests
        fields = "__all__"


class GroutingTestsForm(forms.ModelForm):
    class Meta:
        model = GroutingTests
        fields = "__all__"


class CopperWaterStopperTestsForm(forms.ModelForm):
    class Meta:
        model = CopperWaterStopperTests
        fields = "__all__"


class PermeabilityTestsForm(forms.ModelForm):
    class Meta:
        model = PermeabilityTests
        fields = "__all__"


class GeophysicalForm(forms.ModelForm):
    class Meta:
        model = Geophysical
        fields = "__all__"


class CoreDrilltestForm(forms.ModelForm):
    class Meta:
        model = CoreDrilltest
        fields = "__all__"


class QADocumentationForm(forms.ModelForm):
    class Meta:
        model = QADocumentation
        fields = "__all__"


class EarthMovingCompactionForm(forms.ModelForm):
    class Meta:
        model = EarthMovingCompaction
        fields = "__all__"


class ConcretingEquipmentsForm(forms.ModelForm):
    class Meta:
        model = ConcretingEquipments
        fields = "__all__"


class GroutingEquipmentsForm(forms.ModelForm):
    class Meta:
        model = GroutingEquipments
        fields = "__all__"


class BrazingEquipmentsForm(forms.ModelForm):
    class Meta:
        model = BrazingEquipments
        fields = "__all__"


class SurveyEquipmentsForm(forms.ModelForm):
    class Meta:
        model = SurveyEquipments
        fields = "__all__"


class LabEquipmentsForm(forms.ModelForm):
    class Meta:
        model = LabEquipments
        fields = "__all__"


class GeophysicalInvestigationEquipmentsForm(forms.ModelForm):
    class Meta:
        model = GeophysicalInvestigationEquipments
        fields = "__all__"
