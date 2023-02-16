from django.urls import path
from .views import *

app_name = "news"
urlpatterns = [
    # path("news/", NewsView.as_view(), name="news"),
    path("news-detail/<int:pk>/", NewsDetailView.as_view(), name="news-detail"),
    path("news/list/", NewsView.as_view(), name="news"),
    path("news/all-list/", AllNewsView.as_view(), name="news-all"),
    # news crud
    path("category", CategoryView.as_view(), name="category-table"),
    path("category-create/", CategoryCreateView.as_view(), name="category-create"),
    path(
        "category-update/<int:pk>/",
        CategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "category-delete/<int:pk>/",
        CategoryDeleteView.as_view(),
        name="category-delete",
    ),
    path("news-table/", NewsTableView.as_view(), name="news-table"),
    # add news/notice
    path("admin/add-news/", AddAdminNewsView.as_view(), name="add-anews"),
    # update news/notice
    path("admin/edit-news/<int:pk>/", EditAdminNewsView.as_view(), name="edit-anews"),
    ##########################
    path("news-delete/<int:pk>/", NewsDeleteView.as_view(), name="news-delete"),
    path(
        "recentactivity-detail/<int:pk>/",
        RecentActivityDetailView.as_view(),
        name="recentactivity-detail",
    ),
    path("recent-activity/list/", RecentActivityView.as_view(), name="recent-activity"),
     path("recent-activity/all-list/", AllRecentActivityView.as_view(), name="all-recent-activity"),
    # recent actvities crud
    path(
        "recent-activity/table/",
        RecentActivityTableView.as_view(),
        name="recentactivity-table",
    ),
    #####################recent activity #########
     path("recent-activity/add-recent-activity/", AddAdminRecentView.as_view(), name="add-arecent-activity"),
    # update news/notice
    path("recent-activity/edit-recent-activity/<int:pk>/", EditAdminRecentView.as_view(), name="edit-arecent-activity"),
    ##########################
    path(
        "recent-activity-delete/<int:pk>/",
        RecentActivityDeleteView.as_view(),
        name="recentactivity-delete",
    ),
    # dam knowledge
    path("damknowledge-salient-features/", DamKnowledgeSalientFeaturesView.as_view(), name="damknowledge"),
    path("pipeline/", PipeLineView.as_view(), name="pipeline"),
    path("name-of-dam/", NameOfDamView.as_view(), name="name-of-dam"),
    path("lake/", LakeView.as_view(), name="lake"),
    path("literature/", LiteratureView.as_view(), name="literatures"),
    # admin dam knowledge
    
    # administration
    path(
        "administration/login",
        AdministrationLoginView.as_view(),
        name="administration-login",
    ),
    path(
        "administration/darta-chalani", DartaChalaniView.as_view(), name="darta-chalani"
    ),
    path("administration/darta-list", DartaListView.as_view(), name="darta-list"),
    path("administration/darta-form", DartaFormView.as_view(), name="darta-form"),
    path("administration/chalani-list", ChalaniListView.as_view(), name="chalani-list"),
    path("administration/chalani-form", ChalaniFormView.as_view(), name="chalani-form"),
    path("darta/<int:pk>", DartaDetailView.as_view(), name="darta-detail"),
    path("darta/<int:pk>/update", DartaUpdateView.as_view(), name="darta-update"),
    path("darta/<int:pk>/delete", DartaDeleteView.as_view(), name="darta-delete"),
    path("chalani/<int:pk>", ChalaniDetailView.as_view(), name="chalani-detail"),
    path("chalani/<int:pk>/update", ChalaniUpdateView.as_view(), name="chalani-update"),
    path("chalani/<int:pk>/delete", ChalaniDeleteView.as_view(), name="chalani-delete"),
    path("administration/upload-file/", CUploadFileView.as_view(), name="c-upload-file"),
    path("administration/upload-file/add", CAddUploadFileView.as_view(), name="c-add-file"),
    path("administration/upload-file/edit/<int:pk>/", CEditUploadUpdateFileView.as_view(), name="c-edit-file"),
    path("administration/upload-file/delete/<int:pk>/", CEditUploadDeleteFileView.as_view(), name="c-delete-file"),

    # ========= Notice ========
    path("notice/", NoticeView.as_view(), name="notice"),
    path("notice/create/", NoticeCreateView.as_view(), name="notice-create"),
    path("notice/update/<int:pk>/", NoticeUpdateView.as_view(), name="notice-update"),
    path("notice/delete/<int:pk>/", NoticeDeleteView.as_view(), name="notice-delete"),
    path("admin/profile/", AdminProfileView.as_view(), name="admin-profile"),
    # message
    path("admin/messages/", MessageView.as_view(), name="admin-message"),
    path("messages/create/", MessageCreateView.as_view(), name="message-create"),
    path("messages/update/<int:pk>/", MessageUpdateView.as_view(), name="messages-update"),
    path("messages/delete/<int:pk>/", MessageDeleteView.as_view(), name="message-delete"),

    path("darta/search",DartaSearch.as_view(),name="darta-search")
    # for displying pdf
    #     path("admin/message/create/", MessageCreateView.as_view(), name="message-create"),
    #     path("admin/message/update/<int:pk>/", MessageUpdateView.as_view(), name="message-update"),
    #     path("admin/message/delete/<int:pk>/", MessageDeleteView.as_view(), name="message-delete"),
]
