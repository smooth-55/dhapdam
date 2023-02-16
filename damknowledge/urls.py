from django.urls import path
from .views import (
    DamLiteratureTableView,
    DamLiteratureLinkCreateView,
    DamLiteratureFileCreateView,
    DamLiteratureUpdateView,
    DamLiteratureDeleteView,
    SalientFeaturesTableView,
    SalientFeaturesCreateView,
    SalientFeaturesUpdateView,
    SalientFeaturesDeleteView,
    StorageProjectsTableView,
    StorageProjectCreateView,
    StorageProjectUpdateView,
    StorageProjectDeleteView,
    NameOfDamTableView,
    NameOfDamCreateView,
    NameOfDamUpdateView,
    NameOfDamDeleteView,
    LakesTableView,
    LakesCreateView,
    LakesUpdateView,
    LakesDeleteView,


)

app_name = "damknowledge"
urlpatterns = [
    # dam literature
    path(
        "dam-literature-table/",
        DamLiteratureTableView.as_view(),
        name="dam-literature-table",
    ),
    path(
        "dam-literature-link/create/",
        DamLiteratureLinkCreateView.as_view(),
        name="dam-literaturelink-create",
    ),

    path(
        "dam-literature/create/",
        DamLiteratureFileCreateView.as_view(),
        name="dam-literaturefile-create",
    ),
    path(
        "dam-literature/update/<int:pk>/",
        DamLiteratureUpdateView.as_view(),
        name="dam-literature-update",
    ),
    path(
        "dam-literature/delete/<int:pk>/",
        DamLiteratureDeleteView.as_view(),
        name="dam-literature-delete",
    ),
    # salient features
    path(
        "salient-features-table/",
        SalientFeaturesTableView.as_view(),
        name="salient-features-table",
    ),
    path(
        "salient-features/create/",
        SalientFeaturesCreateView.as_view(),
        name="salient-features-create",
    ),
    path(
        "salient-features/update/<int:pk>/",
        SalientFeaturesUpdateView.as_view(),
        name="salient-features-update",
    ),
    path(
        "salient-features/delete/<int:pk>/",
        SalientFeaturesDeleteView.as_view(),
        name="salient-features-delete",
    ),

    # storage projects pipeline
    path(
        "storage-projects-table/",
        StorageProjectsTableView.as_view(),
        name="storage-projects-table",
    ),
    path(
        "storage-projects/create/",
        StorageProjectCreateView.as_view(),
        name="storage-projects-create",
    ),
    path(
        "storage-projects/update/<int:pk>/",
        StorageProjectUpdateView.as_view(),
        name="storage-projects-update",
    ),
    path(
        "storage-projects/delete/<int:pk>/",
        StorageProjectDeleteView.as_view(),
        name="storage-projects-delete",
    ),
    # name of dam
    path(
        "name-of-dam-table/",
        NameOfDamTableView.as_view(),
        name="name-of-dam-table",
    ),
    path(
        "name-of-dam/create/",
        NameOfDamCreateView.as_view(),
        name="name-of-dam-create",
    ),
    path(
        "name-of-dam/update/<int:pk>/",
        NameOfDamUpdateView.as_view(),
        name="name-of-dam-update",
    ),
    path(
        "name-of-dam/delete/<int:pk>/",
        NameOfDamDeleteView.as_view(),
        name="name-of-dam-delete",
    ),


    # name of dam
    path(
        "lakes-table/",
        LakesTableView.as_view(),
        name="lakes-table",
    ),
    path(
        "lakes/create/",
        LakesCreateView.as_view(),
        name="lakes-create",
    ),
    path(
        "lakes/update/<int:pk>/",
        LakesUpdateView.as_view(),
        name="lakes-update",
    ),
    path(
        "lakes/delete/<int:pk>/",
        LakesDeleteView.as_view(),
        name="lakes-delete",
    ),
]