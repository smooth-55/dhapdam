from django.urls import path
from .views import *

app_name = "dam"

urlpatterns = [    
    #---------------------dhap-dam----------------------
    #introduction
    path("admin/dhapdam/introduction", DhapIntroView.as_view(), name="dadmin-intro"),
    path("admin/dhapdam/introduction/create/", AddDhapIntroCreateView.as_view(), name="add-dhap-intro"),
    path("admin/dhapdam/introduction/<int:pk>/update",
        DhapIntroUpdateView.as_view(),
        name="dhap-intro-update",
    ),
    path("admin/dhapdam/introduction/<int:pk>/delete",
        DhapIntroDeleteView.as_view(),
        name="dhap-intro-delete",
    ),

    #features
    path("admin/dhapdam/features", DhapFeaturesView.as_view(), name="dadmin-features"),
    # add featute
    path("admin/dhapdam/add-features", DhapAddFeatures.as_view(), name="dadmin-add-features"),
    #edit feature
    path("admin/dhapdam/edit-features/<int:pk>/", DhapEditFeatures.as_view(), name="dadmin-edit-features"),
    
    # path(
    #     "contract-progress/<int:pk>/delete",
    #     ContractProgressDelete.as_view(),
    #     name="contract-progress-delete",
    # ),

    #location  and accessibility
    path("admin/dhapdam/location", DhapLocationView.as_view(), name="dadmin-location"),
    path("admin/dhapdam/location/create/", DhapLocationCreateView.as_view(), name="add-dhap-location"),
    path("admin/dhapdam/location/<int:pk>/update",
        DhapLocationUpdateView.as_view(),
        name="dhap-location-update",
    ),
    # path("admin/dhapdam/location/<int:pk>/delete",
    #     DhapIntroDeleteView.as_view(),
    #     name="dhap-location-delete",
    # ),

    #work components
    path("admin/dhapdam/work-components", DhapWorkComponentView.as_view(), name="dadmin-work-components"),
    path("admin/dhapdam/work-components/create/", DhapWorkComponentCreateView.as_view(), name="add-dhap-work-components"),
    path("admin/dhapdam/work-components/<int:pk>/update",
        DhapWorkComponentUpdateView.as_view(),
        name="dhap-work-components-update",
    ),
    path("admin/dhapdam/work-components/<int:pk>/delete",
        DhapWorkComponentDeleteView.as_view(),
        name="dhapwork-components-delete",
    ),
    # sub work component
    path("admin/dhapdam/sub-work-components", DhapSubWorkComponentView.as_view(), name="dadmin-sub-subwork"),
    path("admin/dhapdam/sub-work-components/create/", DhapSubWorkComponentCreateView.as_view(), name="add-dhap-subwork-components"),
    path("admin/dhapdam/sub-work-components/<int:pk>/update",
        DhapSubWorkComponentUpdateView.as_view(),
        name="dhap-subwork-components-update",
    ),
    path("admin/dhapdam/sub-work-components/<int:pk>/delete",
        DhapSubWorkComponentDeleteView.as_view(),
        name="dhap-subwork-components-delete",
    ),
    # contract
    path("admin/dhapdam/contract-detail", DhapContractDetailView.as_view(), name="dadmin-contract-detail"),
     # add detail
    path("admin/dhapdam/add-detail", DhapAddContractDetail.as_view(), name="dadmin-add-detail"),
    #edit detail
    path("admin/dhapdam/edit-detail<int:pk>/", DhapEditContractDetail.as_view(), name="dadmin-edit-detail"),

    #design and quality aspects
    path("admin/dhapdam/design-quality", DhapDesignQualityView.as_view(), name="dadmin-design-quality"),
    path("admin/dhapdam/design-quality/add/", DhapDesignQualityCreateView.as_view(), name="add-dadmin-design-quality"),
    path("admin/dhapdam/design-quality/edit/<int:pk>/",
        DhapDesignQualityUpdateView.as_view(),
        name="dadmin-design-quality-update",
    ),



    # sub design
    path("admin/dhapdam/sub-design-quality", DhapSubDesignQualityView.as_view(), name="dadmin-sub-design-quality"),
    path("admin/dhapdam/sub-design-quality/create/", DhapSubDesignQualityCreateView.as_view(), name="add-dadmin-sub-design-quality"),
    path("admin/dhapdam/sub-design-quality/<int:pk>/update",
        DhapSubDesignQualityUpdateView.as_view(),
        name="dadmin-design-sub-quality-update",
    ),
    path("admin/dhapdam/sub-design-quality/<int:pk>/delete",
        DhapSubDesignQualityDeleteView.as_view(),
        name="dadmin-design-sub-quality-delete",
    ),
    # path("admin/dhapdam/list-design-quality", DhapListDesignQualityView.as_view(), name="dadmin-list-design"),

    path("admin/dhapdam/environmental-aspects", DhapEnvironmentalAspectsView.as_view(), name="dadmin-environmental-aspects"),
    path("admin/dhapdam/environmental-aspects/add/", DhapEnvironmentalAspectsCreateView.as_view(), name="add-dadmin-environmental-aspects"),
    path("admin/dhapdam/environmental-aspects/edit",
        DhapEnvironmentalAspectsUpdateView.as_view(),
        name="dadmin-environmental-aspects-update",
    ),
    #maps
    path("admin/dhapdam/maps", DhapMapsView.as_view(), name="dadmin-maps"),
    path("admin/dhapdam/maps/create/", MapsCreateView.as_view(), name="add-maps"),
    path("admin/dhapdam/maps/<int:pk>/update",
        MapsUpdateView.as_view(),
        name="maps-update",
    ),
    path("admin/dhapdam/maps/<int:pk>/delete",
        MapsDeleteView.as_view(),
        name="maps-delete",
    ),
    

    #-------------------nagmati dam-------------------
    #introduction
    path("admin/nagmati/introduction", NagmatiIntroView.as_view(), name="nadmin-intro"),
    path("admin/nagmati/introduction/create/", AddNagmatiIntroCreateView.as_view(), name="add-nagmati-intro"),
    path("admin/nagmati/introduction/<int:pk>/update",
        NagmatiIntroUpdateView.as_view(),
        name="nagmati-intro-update",
    ),
    #location
    path("admin/nagmati/location", NagmatiLocationView.as_view(), name="nadmin-location"),  
    path("admin/nagmati/location/create/", NagmatiLocationCreateView.as_view(), name="add-nagmati-location"),
    path("admin/nagmati/location/<int:pk>/update",
        NagmatiLocationUpdateView.as_view(),
        name="nagmati-location-update",
    ),
    #status of project
    path("admin/nagmati/project-status", NagmatiProjectStatusView.as_view(), name="nadmin-project-status"),
    path("admin/dhapdam/project-status/create/", NagmatiProjectStatusCreateView.as_view(), name="add-nadmin-project-status"),
    path("admin/dhapdam/project-status/<int:pk>/update",
        NagmatiProjectStatusUpdateView.as_view(),
        name="nadmin-project-statusupdate",
    ),
    #maps
    path("admin/nagmati/maps", NagmatiMapsView.as_view(), name="nadmin-maps"),
    path("admin/nagmati/maps/create/", NagmatiMapsCreateView.as_view(), name="add-nagmati-maps"),
    path("admin/nagmati/maps/<int:pk>/update",
        NagmatiMapsUpdateView.as_view(),
        name="maps-nagmati-update",
    ),
    path("admin/nagmati/maps/<int:pk>/delete",
        NagmatiMapsDeleteView.as_view(),
        name="maps-nagmati-delete",
    ),
    
    #salient features
    path("admin/nagmati/features", NagmatiFeaturesView.as_view(), name="nadmin-features"),
     # add featute
    path("admin/nagmati/add-features", NagmatiAddFeatures.as_view(), name="nadmin-add-features"),
    #edit feature
    path("admin/nagmati/edit-features/<int:pk>/", NagmatiEditFeatures.as_view(), name="nadmin-edit-features"),
    
    
]