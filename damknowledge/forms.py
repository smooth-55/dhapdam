
from django.core.exceptions import ValidationError
from ckeditor.widgets import CKEditorWidget
from .models import (
    DamLiteraures,
    DamSalientFeatures,
    StorageProjectInPipeline,
    NameOfDam,
    Lake,
)
from django.forms import ModelForm
from django import forms


class DamLiterauresLinkForm(ModelForm):

    class Meta:
        model = DamLiteraures
        fields = (
            "title",
            "link",
        )


class DamLiterauresFileForm(ModelForm):

    class Meta:
        model = DamLiteraures
        fields = (
            "title",
            "files",

        )

class DamLiterauresForm(ModelForm):

    class Meta:
        model = DamLiteraures
        fields = (
            "title",
            "link",
            "files",

        )


class DamSalientFeaturesForm(ModelForm):

    class Meta:
        model = DamSalientFeatures
        fields = ('name_of_dam_or_reservoir', 'location', 'main_purpose', 'volume', 'height_of_dam', 'as_per_size', 'as_per_construction_material', 'governing_icold_criteria_for_large_dams', )

    
class StorageProjectInPipelineForm(ModelForm):

    class Meta:
        model = StorageProjectInPipeline
        fields = ('name_of_dam_or_reservoir', 'location', 'main_purpose', 'volume_gross', 'height_of_dam', 'as_per_size', 'as_per_construction_material', 'governing_icold_criteria_for_large_dams',"link" )


class NameOfDamForm(ModelForm):

    class Meta:
        model = NameOfDam
        fields = (
            "title",
            "link",

        )



class LakeForm(ModelForm):

    class Meta:
        model = Lake
        fields = (
            "title",
            "link",

        )
