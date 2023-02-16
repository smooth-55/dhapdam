from django.urls import path
from .views import *
from django.views.generic import TemplateView

app_name = "company"

urlpatterns = [
    # About us
    path("about/", AboutView.as_view(), name="about"),
    path("instrumentation/subdata/", ComingSooonView.as_view(), name="comingsoon"),


    path("citizen-charter/", CirChatView.as_view(), name="citizen-charter"),
    path(
        "contact/",
        ContactView.as_view(),
        name="contact",
    ),
    path(
        "organization-structure/",
        StructureView.as_view(),
        name="structure",
    ),
    # gallery
    path("photos/", PhotoView.as_view(), name="photo"),
    path("photos/category/<int:pk>", PhotoCategorysView.as_view(), name="photo-category"),

    path("videos/", VideoView.as_view(), name="video"),
    # document
    path("document/", DocumentView.as_view(), name="document"),

    #docuement category crud
    path("document/category/", DocumentCategoryView.as_view(), name="document-category"),
    path("document/category-create/", DocumentCategoryCreateView.as_view(), name="documentcategory-create"),
    path(
        "document/category-update/<int:pk>/",
        DocumentCategoryUpdateView.as_view(),
        name="documentcategory-update",
    ),
    path(
        "document/category-delete/<int:pk>/",
        DocumentCategoryDeleteView.as_view(),
        name="documentcategory-delete",
    ),
    # company profile
    path("admin/company/profile", CompanyProfileView.as_view(), name="company-profile"),
    path("admin/comapny-profile-create/", CompanyProfileCreateView.as_view(), name="companyprofile-create"),
    path(
        "admin/companyprofile-update/<int:pk>/",
        CompanyProfileUpdateView.as_view(),
        name="companyprofile-update",
    ),


    # download
    path("download/", DownloadView.as_view(), name="download"),
    # nagmati dam
    path("nagmatidam/", NagmatiDamView.as_view(), name="nagmatidam"),
    path("nagmati-features/", NagmatiFeaturesView.as_view(), name="nagmati-features"),
    path("nagmati-location/", NagmatiLocationView.as_view(), name="nagmati-location"),
    path("nagmati-maps/", NagmatiMapsView.as_view(), name="nagmati-maps"),
    path("nagmati-status/", NagmatiStatusView.as_view(), name="nagmati-status"),
    # imp-link
    path("imp-link/", ImportantLinkView.as_view(), name="imp-link"),
    # policy
    path("strategy-plan-policy/", PolicyUserView.as_view(), name="spp"),
    
    path("act-regualtions/", ActPolicyView.as_view(), name="actreg"),
    # project map
    path("projectmap/", ProjectMapView.as_view(), name="projectmap"),
    # company progress
    ####################### first trimester #################################
    path("fiscalyear/add/", FiscalYearAddView.as_view(), name="fiscalyear-add"),
    path("trimester/view/", TrimesterView.as_view(), name="show"),
    # path("fiscalmonth/add/",FiscalMonthAddView.as_view(),name='fiscalmonth-add'),
    path("progress/", ProgressView.as_view(), name="progress"),
    #Annual physical progress Graph
    path("graph/", GraphView.as_view(), name="graph"),
    path("graph/ajax", GraphAjaxView, name="graph-ajax"),

    #Annual physical progress Graph
    path("overall/graph/", OverallGraphView.as_view(), name="overall-graph"),
    path("overall/graph/ajax", OverallGraphAjaxView, name="overallgraph-ajax"),



    # Construction
    path("design-drawing/", DesignDrawingView.as_view(), name="design-drawing"),
    path("mos/", MethodOfStatementView.as_view(), name="mos"),
    path("reports/", ReportsView.as_view(), name="reports"),
    path("test-footage/", TestFootageView.as_view(), name="test-footage"),
    path("work-footage/", WorkFootageView.as_view(), name="work-footage"),
    path(
        "brazing-equipment/", BrazingEquipmentView.as_view(), name="brazing-equipment"
    ),
    path(
        "concreting-equipment/",
        ConcretingEquipmentView.as_view(),
        name="concreting-equipment",
    ),
    path("earth-equipment/", EarthEquipmentView.as_view(), name="earth-equipment"),
    path(
        "grouting-equipment/",
        GroutingEquipmentView.as_view(),
        name="grouting-equipment",
    ),
    # work test
    path(
        "construction/work/compaction-test/",
        CompactionTestView.as_view(),
        name="compaction-test",
    ),
    path(
        "construction/work/concrete-test/",
        ConcreteTestView.as_view(),
        name="concrete-test",
    ),
    path(
        "construction/work/copper-test/", CopperTestView.as_view(), name="copper-test"
    ),
    path(
        "construction/work/grouting-test/",
        GroutingTestView.as_view(),
        name="grouting-test",
    ),
    path(
        "construction/work/permeability-test/",
        PermeabilityTestView.as_view(),
        name="permeability-test",
    ),
    path(
        "construction/work/geophysical-test/",
        GeophysicalTestView.as_view(),
        name="geophysical-test",
    ),
    path(
        "construction/work/core-drill/", CoreDrillTestView.as_view(), name="core-drill"
    ),
    path(
        "documentation-test/",
        DocumentationTestView.as_view(),
        name="documentation-test",
    ),
    # material TEst
    # path("fiscalmonth/add/",FiscalMonthAddView.as_view(),name='fiscalmonth-add'),
    path("progress/", ProgressView.as_view(), name="progress"),
    # Construction
    path("design-drawing/", DesignDrawingView.as_view(), name="design-drawing"),
    path("mos/", MethodOfStatementView.as_view(), name="mos"),
    path("reports/", ReportsView.as_view(), name="reports"),
    path("test-footage/", TestFootageView.as_view(), name="test-footage"),
    path("work-footage/", WorkFootageView.as_view(), name="work-footage"),
    ##------------------------------ contruction section starts -------------------------- ##
    # equipment
    path(
        "construction/equipment/brazing-equipment/",
        BrazingEquipmentView.as_view(),
        name="brazing-equipment",
    ),
    path(
        "construction/equipment/concreting-equipment/",
        ConcretingEquipmentView.as_view(),
        name="concreting-equipment",
    ),
    path(
        "construction/equipment/earth-equipment/",
        EarthEquipmentView.as_view(),
        name="earth-equipment",
    ),
    path(
        "construction/equipment/grouting-equipment/",
        GroutingEquipmentView.as_view(),
        name="grouting-equipment",
    ),
    path(
        "construction/equipment/survey-equipment/",
        SurveyEquipmentView.as_view(),
        name="survey-equipment",
    ),
    path(
        "construction/equipment/lab-equipment/",
        LabEquipmentView.as_view(),
        name="lab-equipment",
    ),
    path(
        "construction/equipment/geophysical-equipment/",
        GeophysicalEquipmentView.as_view(),
        name="geophysical-equipment",
    ),
    # work test
    path(
        "construction/work/concrete-test/",
        ConcreteTestView.as_view(),
        name="concrete-test",
    ),
    path(
        "construction/work/compaction-test/",
        CompactionTestView.as_view(),
        name="compaction-test",
    ),
    path(
        "construction/work/copper-test/", CopperTestView.as_view(), name="copper-test"
    ),
    path(
        "construction/work/grouting-test/",
        GroutingTestView.as_view(),
        name="grouting-test",
    ),
    path(
        "construction/work/permeability-test/",
        PermeabilityTestView.as_view(),
        name="permeability-test",
    ),
    path(
        "construction/work/geophysical-test/",
        GeophysicalTestView.as_view(),
        name="geophysical-test",
    ),
    path(
        "construction/work/core-drill/", CoreDrillTestView.as_view(), name="core-drill"
    ),
    # documentation
    path(
        "documentation-test/",
        DocumentationTestView.as_view(),
        name="documentation-test",
    ),
    # material TEst
    path(
        "construction/material/earth-filling/",
        EarthFillingTestView.as_view(),
        name="earth-filling",
    ),
    path(
        "construction/material/face-slab-2a/",
        FaceSlabATestView.as_view(),
        name="face-slab-2a",
    ),
    path(
        "construction/material/face-slab-2b/",
        FaceSlabBTestView.as_view(),
        name="face-slab-2b",
    ),
    path(
        "construction/material/small-size-rock/",
        SmallRockTestView.as_view(),
        name="small-size-rock",
    ),
    path(
        "construction/material/first-class-rock/",
        FirstClassTestView.as_view(),
        name="first-class-rock",
    ),
    path(
        "construction/material/second-class-rock/",
        SecondClassTestView.as_view(),
        name="second-class-rock",
    ),
    path(
        "construction/material/rock-fill/", RockFillTestView.as_view(), name="rock-fill"
    ),
    path(
        "construction/material/concrete-aggregate-40mm/",
        ConcreteLargeTestView.as_view(),
        name="concrete-aggregate-40mm",
    ),
    path(
        "construction/material/concrete-aggregate-20mm/",
        ConcreteMediumTestView.as_view(),
        name="concrete-aggregate-20mm",
    ),
    path(
        "construction/material/concrete-aggregate-10mm/",
        ConcreteSmallTestView.as_view(),
        name="concrete-aggregate-10mm",
    ),
    path(
        "construction/material/fine-aggregate/",
        FineAggregateTestView.as_view(),
        name="fine-aggregate",
    ),
    path("construction/material/cement/", CementTestView.as_view(), name="cement"),
    path(
        "construction/material/granular/", GranularTestView.as_view(), name="granular"
    ),
    # admin panel
    path("user-navigate/", UserNavigateView.as_view(), name="user-navigate"),
    path("admin-dashboard/", DashboardView.as_view(), name="admin-dashboard"),
    # admin panel activity
    # admin photo
    # photo category 
    path("photo/category/", PhotoCategoryView.as_view(), name="photo-category"),
    path("photos/category/create/", PhotoCategoryCreateView.as_view(), name="photo-category-create"),
    path("photos/category/update/<int:pk>/", PhotocategoryUpdateView.as_view(), name="photo-category-update"),
    path("photos/category/delete/<int:pk>/", PhotoCategoryDeleteView.as_view(), name="photo-category-delete"),

    path("photo-table/", PhotoTableView.as_view(), name="photo-table"),
    path("photos/create/", PhotoCreateView.as_view(), name="photo-create"),
    path("photos/update/<int:pk>/", PhotoUpdateView.as_view(), name="photo-update"),
    path("photos/delete/<int:pk>/", PhotoDeleteView.as_view(), name="photo-delete"),
    # admin video
    path("video-table/", VideoTableView.as_view(), name="video-table"),
    path("video/create/", VideoCreateView.as_view(), name="video-create"),
    path("video/update/<int:pk>/", VideoUpdateView.as_view(), name="video-update"),
    path("video/delete/<int:pk>/", VideoDeleteView.as_view(), name="video-delete"),
    # About block
    path("about-intro/", AboutIntroView.as_view(), name="about-intro"),
    path("about-intro/create/", AboutCreateView.as_view(), name="about-create"),
    path(
        "about-intro/update/<int:pk>/", AboutUpdateView.as_view(), name="about-update"
    ),
    path(
        "about-intro/delete/<int:pk>/", AboutDeleteView.as_view(), name="about-delete"
    ),
    # employee detail
    path("admin/employee-list/", EmployeeTableView.as_view(), name="employee-list"),
    path("admin/add-employee/", AddEmployeeView.as_view(), name="add-employee"),
    path("admin/update/<int:pk>/", EditEmployeeView.as_view(), name="edit-employee"),
    path("admin/delete/<int:pk>/", EmployeeDeleteView.as_view(), name="employee-delete"),    

    # ex employee
    path("admin/ex-employee-list/", ExEmployeeTableView.as_view(), name="ex-employee-list"),
    path("admin/add-ex-employee/", AddExEmployeeView.as_view(), name="add-ex-employee"),
    path("admin/ex-employee-update/<int:pk>/", EditExEmployeeTableView.as_view(), name="edit-ex-employee"),
    path("admin/ex-employee-delete/<int:pk>/", ExEmployeeDeleteView.as_view(), name="ex-employee-delete"),    

    # ex project head
    path("admin/ex-projet-head-list/", ExProjectHeadTableView.as_view(), name="ex-project-list"),
    path("admin/add-ex-projecthead/", AddExProjectHeadView.as_view(), name="add-ex-projecthead"),

    path("admin/edit-ex-projet-head/<int:pk>/", EditExProjectHeadTableView.as_view(), name="edit-ex-project"),
    path("admin/ex-project-delete/<int:pk>/", ExprojectHeadDeleteView.as_view(), name="ex-employee-delete"),    

    

    # citizen charter
    path("citizen-table/", CitizenTable.as_view(), name="citizen-table"),
    path("citizen/create/", CitizenCreateView.as_view(), name="citizen-create"),
    path(
        "citizen/update/<int:pk>/", CitizenUpdateView.as_view(), name="citizen-update"
    ),
    path(
        "citizen/delete/<int:pk>/", CitizenDeleteView.as_view(), name="citizen-delete"
    ),
    # oragnization structure
    path(
        "organization-table/",
        OrganizationTableView.as_view(),
        name="organization-table",
    ),
    path(
        "organization/create/",
        OrganizationCreateView.as_view(),
        name="organization-create",
    ),
    path(
        "organization/update/<int:pk>/",
        OrganizationUpdateView.as_view(),
        name="organization-update",
    ),
    path(
        "organization/delete/<int:pk>/",
        OrganizationDeleteView.as_view(),
        name="organization-delete",
    ),
    # policy
    path("policy/", PolicyView.as_view(), name="policy"),
    path("policy/create/", PolicyCreateView.as_view(), name="policy-create"),
    path("policy/update/<int:pk>/", PolicyUpdateView.as_view(), name="policy-update"),
    path("policy/delete/<int:pk>/", PolicyDeleteView.as_view(), name="policy-delete"),
    # important links crud
    path("imp-link-table/", ImpLinkTable.as_view(), name="imp-link-table"),
    path("imp-link/create/", ImpLinkCreateView.as_view(), name="imp-link-create"),
    path(
        "imp-link/update/<int:pk>/", ImpLinkUpdateView.as_view(), name="imp-link-update"
    ),
    path(
        "imp-link/delete/<int:pk>/", ImpLinkDeleteView.as_view(), name="imp-link-delete"
    ),
    # document crud
    path("document-table/<int:pk>/", DocumentFilterTableView.as_view(), name="document-filter-table"),
    path("document-table/", DocumentTableView.as_view(), name="document-table"),
    path("document/create/", DocumentCreateView.as_view(), name="document-create"),
    path(
        "document/update/<int:pk>/",
        DocumentUpdateView.as_view(),
        name="document-update",
    ),
    path(
        "document/delete/<int:pk>/",
        DocumentDeleteView.as_view(),
        name="document-delete",
    ),
    path("document/category/", DocumentCategoryView.as_view(), name="document-category"),
    # download
    path("download-table/", DownloadTableView.as_view(), name="download-table"),
    path(
        "downloadfile/create/",
        DownloadFileCreateView.as_view(),
        name="downloadfile-create",
    ),
    path(
        "downloadlink/create/",
        DownloadLinkCreateView.as_view(),
        name="downloadlink-create",
    ),
    path(
        "downloadfile/update/<int:pk>/",
        DownloadFileUpdateView.as_view(),
        name="downloadfile-update",
    ),
    path(
        "downloadlink/update/<int:pk>/",
        DownloadLinkUpdateView.as_view(),
        name="downloadlink-update",
    ),
    path(
        "download/delete/<int:pk>/",
        DownloadDeleteView.as_view(),
        name="download-delete",
    ),
    # users
    path("users/", UsersTableView.as_view(), name="users"),
    path("add-user/", AddUserView.as_view(), name="add-user"),
    path("edit-user/<int:pk>/", EditUserView.as_view(), name="edit-user"),
    path("delete-user/<int:pk>/", DeleteUserView.as_view(), name="delete-user"),
    path("contact-table/", ContactTableView.as_view(), name="contact-table"),
    path(
        "contact/delete/<int:pk>/", ContactDeleteView.as_view(), name="contact-delete"
    ),
    # home slider
    path("homeslider/", HomeSliderTableView.as_view(), name="homeslider"),
    path(
        "homeslider/create/", HomesliderCreateView.as_view(), name="homeslider-create"
    ),
    path(
        "homeslider/update/<int:pk>/",
        HomesliderUpdateView.as_view(),
        name="homeslider-update",
    ),
    path(
        "homeslider/delete/<int:pk>/",
        HomesliderDeleteView.as_view(),
        name="homeslider-delete",
    ),
    # admin contract
    path("contract-table/", ContractTableView.as_view(), name="contract-table"),
    # path("add-contract/", AddContractView.as_view(), name="add-contract"),
    # path("edit-contract/", EditContractView.as_view(), name="edit-contract"),
    path("contract-detail/", ContractDetailTableView.as_view(), name="contract-detail"),
    path(
        "contract-complete/",
        ContractCompleteTableView.as_view(),
        name="contract-complete",
    ),
    # admin progess
    path("fiscal-year/", FiscalYearView.as_view(), name="fiscal-year"),
    path(
        "fiscal-year/create/", FiscalYearCreateView.as_view(), name="fiscal-year-create"
    ),
    path(
        "fiscal-year/update/<int:pk>/",
        FiscalYearUpdateView.as_view(),
        name="fiscal-year-update",
    ),
    path(
        "fiscal-year/delete/<int:pk>/",
        FiscalYearDeleteView.as_view(),
        name="fiscal-year-delete",
    ),
    path("first-trimesters/", FirstTrimestersView.as_view(), name="first-trimesters"),
    path(
        "second-trimesters/", SecondTrimestersView.as_view(), name="second-trimesters"
    ),
    path("third-trimesters/", ThirdTrimestersView.as_view(), name="third-trimesters"),
    # construtction silder crud
    path("construct-slider/", ConstructSliderView.as_view(), name="construct-slider"),
    path(
        "construct-slider/create/",
        ConstructionCreateView.as_view(),
        name="construct-create",
    ),
    path(
        "construct-slider/update/<int:pk>/",
        ConstructionUpdateView.as_view(),
        name="construct-update",
    ),
    path(
        "construct-slider/delete/<int:pk>/",
        ConstructionDeleteView.as_view(),
        name="construct-delete",
    ),
    # stakeholder slider crud
    path("stakeholder/", StakeholderSliderView.as_view(), name="stakeholder"),
    path(
        "stakeholder/create/",
        StakeholderCreateView.as_view(),
        name="stakeholder-create",
    ),
    path(
        "stakeholder/update/<int:pk>/",
        StakeholderUpdateView.as_view(),
        name="stakeholder-update",
    ),
    path(
        "stakeholder/delete/<int:pk>/",
        StakeholderDeleteView.as_view(),
        name="stakeholder-delete",
    ),
    # reservoir slider crud
    path("reservoir/", ReservoirSliderView.as_view(), name="reservoir"),
    path("reservoir/create/", ReservoirCreateView.as_view(), name="reservoir-create"),
    path(
        "reservoir/update/<int:pk>/",
        ReservoirUpdateView.as_view(),
        name="reservoir-update",
    ),
    path(
        "reservoir/delete/<int:pk>/",
        ReservoirDeleteView.as_view(),
        name="reservoir-delete",
    ),
    # admin contract
    # admin contract
    path("add-contract/", AddContractView.as_view(), name="add-contract"),
    path("edit-contract/", EditContractView.as_view(), name="edit-contract"),
    path("add-detail/", AddContractDetailTableView.as_view(), name="add-detail"),
    path("edit-detail/", EditContractDetailTableView.as_view(), name="edit-detail"),
    # path(
    #     "contract-features/",
    #     ContractFeaturesTableView.as_view(),
    #     name="contract-features",
    # ),
    # path(
    #     "contract-features/",
    #     ContractFeaturesTableView.as_view(),
    #     name="contract-features",
    # ),
    # path(
    #     "contract/add-features/",
    #     AddContractFeaturesTableView.as_view(),
    #     name="add-features",
    # ),
    path(
        "contract/edit-features/",
        EditContractFeaturesTableView.as_view(),
        name="edit-features",
    ),
    path(
        "contract-progress/",
        ContractProgressesTableView.as_view(),
        name="contract-progress",
    ),
    path(
        "contract/add-progress/",
        AddContractProgressesView.as_view(),
        name="add-contract-progress",
    ),
    path(
        "contract/edit-progress/",
        EditContractProgressesView.as_view(),
        name="edit-contract-progress",
    ),
    path(
        "contract-complete/",
        ContractCompleteTableView.as_view(),
        name="contract-complete",
    ),
    # admin progess
    path(
        "trimester/option/",
        TemplateView.as_view(template_name="admin/progress/trimester_home.html"),
        name="trimester-home",
    ),
    path("trimesters/", TrimestersView.as_view(), name="trimesters"),
    # progress section
    ##------------------------------ first trimester ---------------------------------------##
    path("add-first-trimesters/", AddTrimestersView.as_view(), name="add-trimesters"),
    path(
        "trimesters/month2/<int:pk>/add/",
        FirstTrimesterBhadraUpdateView.as_view(),
        name="firsttrimester-update",
    ),
    path(
        "trimesters/month3/<int:pk>/add/",
        FirstTrimesterAshojUpdateView.as_view(),
        name="firsttrimestermonth3-update",
    ),
    path(
        "trimesters/month4/<int:pk>/add/",
        FirstTrimesterKartikUpdateView.as_view(),
        name="firsttrimestermonth4-update",
    ),
    path(
        "firsttrimesters-periodic/<int:pk>/add/",
        FirstTrimesterUpdateView.as_view(),
        name="firsttrimesterperiodic",
    ),
    ##------------------------------ second trimester ---------------------------------------##
    path(
        "add-second-trimesters/<int:pk>/",
        AddSecondMangsirTrimestersView.as_view(),
        name="add-secondtrimesters",
    ),
    path(
        "add-second-trimesters/month2/<int:pk>/",
        SecondTrimestersPoushUpdateView.as_view(),
        name="secondtrimestermonth2-update",
    ),
    path(
        "add-second-trimesters/month3/<int:pk>/",
        SecondTrimestersMaghUpdateView.as_view(),
        name="secondtrimestermonth3-update",
    ),
    path(
        "add-second-trimesters/month4/<int:pk>/",
        SecondTrimestersFalgunUpdateView.as_view(),
        name="secondtrimestermonth4-update",
    ),
    path(
        "secondtrimesters-periodic/<int:pk>/add/",
        SecondTrimesterUpdateView.as_view(),
        name="secondtrimesterperiodic",
    ),
    ##------------------------------ third trimester ---------------------------------------##
    path(
        "add-third-trimesters/<int:pk>/",
        AddThirdChaitraTrimestersView.as_view(),
        name="add-thirdtrimesters",
    ),
    path(
        "add-third-trimesters/month2/<int:pk>/",
        ThirdTrimestersBaisakhUpdateView.as_view(),
        name="thirdtrimestermonth2-update",
    ),
    path(
        "add-third-trimesters/month3/<int:pk>/",
        ThirdTrimestersJesthaUpdateView.as_view(),
        name="thirdtrimestermonth3-update",
    ),
    path(
        "add-third-trimesters/month4/<int:pk>/",
        ThirdTrimestersAsarUpdateView.as_view(),
        name="thirdtrimestermonth4-update",
    ),
    path(
        "thirdtrimesters-periodic/<int:pk>/add/",
        ThirdTrimesterUpdateView.as_view(),
        name="thirdtrimesterperiodic",
    ),
    path("first-trimesters/years/<int:pk>", TrimestersYearView.as_view(), name="firsttrimesters-year"),
    path("second-trimesters/years/<int:pk>", SecondTrimesterYearView.as_view(), name="secondtrimesters-year"),
    path("third-trimesters/years/<int:pk>", ThirdTrimesterYearView.as_view(), name="thirdtrimesters-year"),




    # darta
    # path("darta/", DartaAddView.as_view(), name="add-darta"),
    # path("darta/", DartaAddView.as_view(), name="add-darta"),
    # path("darta-list/", DartaListView.as_view(), name="darta-list"),
    # path("darta/<int:pk>", DartaDetailView.as_view(), name="darta-detail"),
    # path("darta/<int:pk>/update", DartaUpdateView.as_view(), name="darta-update"),
    # path("darta/<int:pk>/delete", DartaDeleteView.as_view(), name="darta-delete"),
    # path("chalani/", ChalaniAddView.as_view(), name="add-chalani"),
    # path("chalani/", ChalaniAddView.as_view(), name="add-chalani"),
    # path("chalani-list/", ChalaniListView.as_view(), name="chalani-list"),
    # path("chalani/<int:pk>", ChalaniDetailView.as_view(), name="chalani-detail"),
    # path("chalani/<int:pk>/update", ChalaniUpdateView.as_view(), name="chalani-update"),
    # path("chalani/<int:pk>/delete", ChalaniDeleteView.as_view(), name="chalani-delete"),

    # #admin darta chalani
    path('admin/administration/file-upload', AdministrationFileUploadView.as_view(), name="administration-file"),
    path("admin/administration/file-upload/create/", AdministrationFileUploadCreateView.as_view(), name="administration-file-create"),
    path("admin/administration/file-upload/update/<int:pk>/", AdministrationFileUploadUpdateView.as_view(), name="administration-file-update"),
    path("admin/administration/file-upload/delete/<int:pk>/", AdministrationFileUploadDeleteView.as_view(), name="administration-file-delete"),

    path('admin/administration/darta', DartaTableView.as_view(), name="darta-table"),
    path('admin/administration/chalani',ChalaniTableView.as_view(), name="chalani-table"),


    # -------------------------__Accountant__------------------------------
    path('admin/accountant/file-upload', FileBudgetView.as_view(), name="file-budget"),
    path("admin/accountant/file-upload/create/", FileBudgetCreateView.as_view(), name="file-budget-create"),
    path("admin/accountant/file-upload/update/<int:pk>/", FileBudgetUpdateView.as_view(), name="file-budget-update"),
    path("admin/accountant/file-upload/delete/<int:pk>/", FileBudgetDeleteView.as_view(), name="file-budget-delete"),


    path('admin/accountant/current-budget', CurrentBudgetView.as_view(), name="current-budget"),
    path("admin/accountant/current-budget/create/", CurrentBudgetCreateView.as_view(), name="current-budget-create"),
    path("admin/accountant/current-budget/update/<int:pk>/", CurrentBudgetUpdateView.as_view(), name="current-budget-update"),
    path("admin/accountant/current-budget/delete/<int:pk>/", CurrentBudgetDeleteView.as_view(), name="current-budget-delete"),


    path('admin/accountant/capital-budget', CapitalBudgetView.as_view(), name="capital-budget"),
    path("admin/accountant/capital-budget/create/", CapitalBudgetCreateView.as_view(), name="capital-budget-create"),
    path("admin/accountant/capital-budget/update/<int:pk>/", CapitalBudgetUpdateView.as_view(), name="capital-budget-update"),
    path("admin/accountant/capital-budget/delete/<int:pk>/", CapitalBudgetDeleteView.as_view(), name="capital-budget-delete"),
    # live data=----------
    path("live-data/aws/",AwsView.as_view(), name="aws"),
    
    path("live-data/main/",InstrumentationView.as_view(), name="instrumentation"),
    path("live-data/saddle-1/",sdOneView.as_view(), name="sd1"),
    path("live-data/saddle-2/",sdTwoView.as_view(), name="sd2"),
    path("live-data/saddle-3/",sdThreeView.as_view(), name="sd3"),
    path("live-data/hydro/",HydroView.as_view(), name="hydro"),
]
