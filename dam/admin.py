from django.contrib import admin

from .models import (
    DamIntroduction,
    SalientFeatures,
    LocationAndAccessibility,
    MajorWorkComponents,
    SubMajorWorkComponents,
    ContractDetail,
    DesignAndQualityAspects,
    SubDesignAndQualityAspects,
    EnvironmentalAspects,
    Maps,
    IntroductionOfDam,
    MajorWorkComponentsDhapDam
)

# Register your models here.

admin.site.register(
    [
        DamIntroduction,
        SalientFeatures,
        LocationAndAccessibility,
        MajorWorkComponents,
        SubMajorWorkComponents,
        ContractDetail,
        DesignAndQualityAspects,
        SubDesignAndQualityAspects,
        EnvironmentalAspects,
        Maps,
        IntroductionOfDam,
        MajorWorkComponentsDhapDam
    ]
)
