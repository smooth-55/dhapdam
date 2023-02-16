from .models import (
    DamIntroduction,
    SalientFeatures,
    LocationAndAccessibility,
    MajorWorkComponents,
    MajorWorkComponentsDhapDam,
    SubMajorWorkComponents,
    ContractDetail,
    DesignAndQualityAspects,
    SubDesignAndQualityAspects,
    EnvironmentalAspects,
    Maps,
    IntroductionOfDam,
)
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget



class DateInput(forms.DateInput):
    input_type = "date"


class IntroductionOfDamForm(ModelForm):
    content = forms.CharField(widget = CKEditorWidget())

    class Meta:
        model = IntroductionOfDam
        fields = (
            "content",
            "image",
        )


class SalientFeaturesForm(ModelForm):
    content = forms.CharField(widget = CKEditorWidget())

    class Meta:
        model = SalientFeatures
        fields = (
            "content",
            "dam_type",
            "location_of_dam",
            "dam_height",
            "dam_top_length",
            "crest_width",
            "upstream_slope_inclination",
            "downstream_slope_inclination",
            "Concrete_face_thickness",
            "normal_waterlevel",
            "Freeboard",
            "reservoir_volume",
            "saddle_dam",
            "dam_crest_elevation",
        )


class LocationAndAccessibilityForm(ModelForm):
    content = forms.CharField(widget = CKEditorWidget())
    accessibility_content = forms.CharField(widget = CKEditorWidget())

    class Meta:
        model = LocationAndAccessibility
        fields = (
            "content",
            "image",
            "accessibility_content",
            "accessibility_image",
        )


class MajorWorkComponentsDhapdamForm(ModelForm):
    """Form for major work components in dhapdam"""
    description = forms.CharField(widget = CKEditorWidget())

    class Meta:
        model = MajorWorkComponentsDhapDam
        fields = (
            "sub_dam",
            "title",
            "image",
            "description"
        )



class MajorWorkComponentsForm(ModelForm):
    title = forms.CharField(widget = CKEditorWidget(),required=True)

    class Meta:
        model = MajorWorkComponents
        fields = (
            "title",
            "image",
        )


class SubMajorWorkComponentsForm(ModelForm):
    title = forms.CharField(
        max_length=100,
        required=True,
        error_messages={"required": "Please enter title"},
    )

    class Meta:
        model = SubMajorWorkComponents
        fields = (
            "major_work_components",
            "title",
        )

class DhapEnvironmentalAspectsForm(ModelForm):
    content = forms.CharField(widget = CKEditorWidget())
    class Meta:
        model = EnvironmentalAspects
        fields = (
            "content",
            )

class ContractDetailForm(ModelForm):
    class Meta:
        model = ContractDetail
        fields = (
            "content",
            "Name_of_work",
            "client",
            "contract_no",
            "name_of_contractor",
            "date_of_agreement",
            "intial_date_of_completion",
            "revised_date_of_completion",
            "contract_amount_with_VAT",
            "physical_progress",
            "financial_progress",
            "responsible_person",
        )
        widgets = {
            "date_of_agreement": DateInput,
            "intial_date_of_completion": DateInput,
            "revised_date_of_completion": DateInput,
        }


class DesignAndQualityAspectsForm(ModelForm):
    content = forms.CharField(widget = CKEditorWidget())
    class Meta:
        model = DesignAndQualityAspects
        fields = (
            "content",
            )


class SubDesignAndQualityAspectsForm(ModelForm):
    class Meta:
        model = SubDesignAndQualityAspects
        fields = (
            "design_and_quality_aspects",
            "title",
            "sub_title",
        )


# salient features for nagmati
class SalientFeaturesNagmatiForm(ModelForm):

    content = forms.CharField(widget = CKEditorWidget())

    class Meta:
        model = SalientFeatures
        fields = (
            "content",
            "dam_type",
            "dam_height",
            "dam_top_length",
            "dam_crest_elevation",
            "crest_width",
            "dam_volume",
            "full_supply_level",
            "Freeboard",
            "design_discharge",
            "power_of_production",
            "cost_of_project",
            "reservoir_surface_area_at_fsl",
            
        )
