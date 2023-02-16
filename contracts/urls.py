from django.urls import path
from .views import *

app_name = "contracts"

urlpatterns = [
    # get list of contract or single contract
    path("contracts/completed/", ContractCompletedView.as_view(), name="contract"),
    path("contracts/ongoing/", ContractOngoingView.as_view(), name="contract=ongoing"),
    path(
        "contracts/progress/", ContractProgressView.as_view(), name="contract-progress"
    ),
    path("contracts/<int:pk>", ContractCompletedView.as_view(), name="contract"),
    # ----------static url----------------
    path("contracts-ongoing/", ClientContractOngoingView.as_view(), name="c-ongoing"),
    path("contracts-completed/", ClientContractCompletedView.as_view(), name="c-completed"),
    path("contracts-progress/", ClientContractProgressView.as_view(), name="c-progress"),
    # ----------static url----------------
    # add and update of contract
    # path("contract/add", ContractCreateView.as_view(), name="contract-add"),
    path("contract/add", addContract, name="contract-add"),
    path("contract/<int:pk>", ContractDetailView.as_view(), name="contract-detail"),
    path("contract-list/", ContractListView.as_view(), name="contract-list"),
    path(
        "contract/update/<int:pk>", ContractUpdateView.as_view(), name="contract-update"
    ),
    path(
        "contract/delete/<int:pk>", ContractDeleteView.as_view(), name="contract-delete"
    ),
    # add and update of contract detail
    path("contract-detail/", ContractDetailList.as_view(), name="contract-detail-list"),
    path(
        "contract/<int:pk>",
        ContractDetailDetailView.as_view(),
        name="contract-detail-detail",
    ),
    path(
        "contract-detail/add", ContractDetailAdd.as_view(), name="contract-detail-add"
    ),
    path(
        "contract-detail/<int:pk>/update",
        ContractDetailUpdate.as_view(),
        name="contract-detail-update",
    ),
    path(
        "contract-detail/<int:pk>/delete",
        ContractDetailDelete.as_view(),
        name="contract-detail-delete",
    ),
    # crud for contract Feature
    path("contract-feature/", ContractFeatureList.as_view(), name="contract-feature"),
    path(
        "contract-feature/<int:pk>",
        ContractFeatureDetail.as_view(),
        name="contract-feature-detail",
    ),
    path(
        "contract-feature/add",
        ContractFeatureCreate.as_view(),
        name="contract-feature-add",
    ),
    path(
        "contract-feature/<int:pk>/update",
        ContractFeatureUpdate.as_view(),
        name="contract-feature-update",
    ),
    path(
        "contract-feature/<int:pk>/delete",
        ContractFeatureUpdate.as_view(),
        name="contract-feature-delete",
    ),
    # Crud for Contract Progress
    path("contract-progress/", ContractProgressGet.as_view(), name="contract-progress"),
    path(
        "contract-progress/add",
        ContractProgressAdd.as_view(),
        name="contract-progress-add",
    ),
    path(
        "contract-progress/<int:pk>/update",
        ContractProgressUpdate.as_view(),
        name="contract-progress-update",
    ),
    path(
        "contract-progress/<int:pk>/delete",
        ContractProgressDelete.as_view(),
        name="contract-progress-delete",
    ),
    # get url of different contract elements
    path(
        "contract/<int:pk>/intro",
        ContractIntroductionView.as_view(),
        name="contract-intro",
    ),
    path(
        "contract/<int:pk>/feature",
        ContractFeatureView.as_view(),
        name="contract-feature",
    ),
    path(
        "contract/<int:pk>/location",
        ContractLocationView.as_view(),
        name="contract-location",
    ),
    path(
        "contract/<int:pk>/design-quality",
        ContractDesignQualityView.as_view(),
        name="contract-design-quality",
    ),
    path(
        "contract/<int:pk>/env-aspects",
        ContractEnviromentalAspects.as_view(),
        name="contract-env-aspects",
    ),
    # for displaying purposes only
    path("dhap-dam/", DhapdamView.as_view(), name="dhap-dam"),
    path("dhap-features/", DhapFeaturesView.as_view(), name="dhap-features"),
    path("dhap-location/", DhapLocationView.as_view(), name="dhap-location"),
    path(
        "dhap-work-components/",
        DhapWorkComponentsView.as_view(),
        name="dhap-work-components",
    ),
    path(
        "dhap-work-components/<int:pk>/",
        DhapWorkComponentsDetailView.as_view(),
        name="dhap-work-components-detail",
    ),
    path("dhap-contract/", DhapContractDetailView.as_view(), name="dhap-contract"),
    path("dhap-design/", DhapDesignView.as_view(), name="dhap-design"),
    path(
        "dhap-environmental/",
        DhapEnvironmentalView.as_view(),
        name="dhap-environmental",
    ),
    path("dhap-maps/", DhapMapsView.as_view(), name="dhap-maps"),
]
