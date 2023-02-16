from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from news.views import IndexView,MessageViewHome
from django.views.generic import TemplateView
from exceptionsapp.views import error_404,error_500,error_403,error_400

handler404 = 'exceptionsapp.views.error_404'
handler403 = 'exceptionsapp.views.error_403'
handler400 = 'exceptionsapp.views.error_400'
handler400 = 'exceptionsapp.views.error_500'


urlpatterns = [
    path("", include("contracts.urls")),
    path("user/", include("users.urls")),
    path("", include("news.urls")),
    path("", include("company.urls")),
    path("", include("construction.urls")),
    path("", include("dam.urls")),
    path("", include("damknowledge.urls")),

    # home
    path("", IndexView.as_view(), name="index"),
    path('message/<slug:slug>/', MessageViewHome.as_view(), name='message'),
    #list of apps
    path('admin/', admin.site.urls),
    path("", include('django.contrib.auth.urls')),
    #external package
    path('ckeditor/', include('ckeditor_uploader.urls')),


    
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


