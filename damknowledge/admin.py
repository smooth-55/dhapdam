from django.contrib import admin
from .models import (
    DamLiteraures,
    DamSalientFeatures,
    StorageProjectInPipeline,
    NameOfDam,
    Lake,
)



# Register your models here.
admin.site.register(
    [   
        
    DamLiteraures,
    DamSalientFeatures,
    StorageProjectInPipeline,
    NameOfDam,
    Lake,
        ]
)
