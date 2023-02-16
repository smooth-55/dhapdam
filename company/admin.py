from django.contrib import admin
from .models import (
    Introduction,
    Contact,
    Structure,
    CitizenCharter,
    Photos,
    Videos,
    Downloads,
    HomepageSliderImages,
    Policy,
    ImportantLinks,
    FiscalYear,
    StakeHolders,
    ConstructionWork,
    Reservoir,
    Visitor,
    FirstTrimester,
    SecondTrimester,
    ThirdTrimester,
    Darta,
    Chalani,
    DocumentCategory,
    Documents,
    CompanyProfile,
    CurrentBudget,
    CapitalBudget,
    AccountUploadFile,
    AdminstrationUploadFile,
    PhotoCategory
)



# Register your models here.
admin.site.register(
    [   
        
        Introduction,
        Contact,
        Structure,
        CitizenCharter,
        Photos,
        Videos,
        Downloads,
        Policy,
        ImportantLinks,
        HomepageSliderImages,
        FiscalYear,
        StakeHolders,
        ConstructionWork,
        Reservoir,
        Visitor,
        FirstTrimester,
        SecondTrimester,
        ThirdTrimester,
        Darta,
        Chalani,
        DocumentCategory,
        Documents,
        CompanyProfile,
        CurrentBudget,
        CapitalBudget,
        AccountUploadFile,
        AdminstrationUploadFile,
        PhotoCategory
    ]
)
