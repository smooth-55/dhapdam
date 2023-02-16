from django.shortcuts import render
from django.views.generic import (
    RedirectView,
    TemplateView,
    DetailView,
    CreateView,
    FormView,
    UpdateView,
    DeleteView,
    ListView,
)
from .models import News, Category, RecentActivities, HomeNotice, Message
from django.urls import reverse_lazy
from company.models import (
    Photos,
    Videos,
    Visitor,
    StakeHolders,
    Reservoir,
    ConstructionWork,
    HomepageSliderImages,
    Introduction,
    FiscalYear,
    PhotoCategory,
    AdminstrationUploadFile
)
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse

from .forms import *
from bootstrap_modal_forms.generic import BSModalCreateView
from django.views.generic.base import ContextMixin
from django.contrib.messages.views import SuccessMessageMixin
from company.views import AddSuccessMixin, UpdateSuccessMixin, DeleteSuccessMixin

from django.utils.decorators import method_decorator
from news.models import Message
from company.utils.calculation import graph_calc
from users.decorators import (
    AllUserRequiredMixin,
    AccountantRequiredMixin,
    AdminstrationRequiredMixin,
    AllUserRequiredAndAdminstration
)
from damknowledge.models import (
    DamLiteraures,
    DamSalientFeatures,
    StorageProjectInPipeline,
    NameOfDam,
    Lake,
)
from django.http import FileResponse, Http404
from pytube import YouTube 
from company.forms import AdminstrationUploadFileForm
from django.db.models import Q
from datetime import date
# Create your views here.


class IndexView(TemplateView):
    """
    Home page
    """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["chief"] = Message.objects.filter(designation="U")
        context["info_officer"] = Message.objects.filter(designation="E")
        try:
            context["news"] = News.objects.filter(display=True).order_by("-created_at")
            context["recent"] = RecentActivities.objects.filter(display=True).order_by('-id')
            context["photos"] = Photos.objects.filter(category__isnull=True).order_by("-id")[:2]
            context["photos_catgeory"] = PhotoCategory.objects.all().order_by("-id")[:1]
            videos = Videos.objects.all()
            context["videos"] = videos
            context["stakeholders"] = StakeHolders.objects.all()
            context["reservoir"] = Reservoir.objects.last()
            context["constructions"] = ConstructionWork.objects.last()
            context["homeslider"] = HomepageSliderImages.objects.all()

            
        except ConstructionWork.DoesNotExist or HomepageSliderImages.DoesNotExist:
            context["constructions"] = None
            
        try:
            context["intro"] = Introduction.objects.last()
        
        except:
            context["intro"] = None
        try:
            context["notice"] = HomeNotice.objects.latest("created_at")
        except:
            context["notice"] = None
        
           
        
        # try:
        #     yrs = FiscalYear.objects.last()
        #     if yrs:
        #         context["yrs"] = yrs
        #         year_name = FiscalYear.objects.get(id=yrs.id)
        #         total_cost = graph_calc(year_name)
        #         context["total_cost"] = total_cost
        #     context["fiscal"] = FiscalYear.objects.all()
        #     # get the different each month data
           
        # except FiscalYear.DoesNotExist:
        #     total_cost = None
            

        #pass videos thumbnail
        thumbnail = []
        title = []
        links = []
        for video in videos:
            link = video.link
            thumbnail.append(YouTube(link).thumbnail_url)
            if YouTube(link).title:
                title.append(YouTube(link).title)
            links.append(link)
        context["thumbnails"] = thumbnail
        context['videos_all'] = zip(thumbnail,title,links)
        # th_title = zip(thumbnail,title)
        # data = zip(th_title,link)


        # link="https://www.youtube.com/watch?v=ILchJJrEuiQ"
        # context['yt'] = YouTube(link).thumbnail_url
    

        return context


class MessageViewHome(DetailView):
    """
    Message from chief
    """
    model = Message
    template_name = "frontend/message.html"
    context_object_name = "messages"



class BaseSiderbarView(ContextMixin):
    template_name = "layout/admin/header.html"


"""===================================
--------- News section start ---------
======================================"""



class CategoryView(AllUserRequiredMixin,TemplateView):
    """
    category of news and recent activities
    """

    template_name = "admin/news/category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["title"] = "Category"
        return context



class CategoryCreateView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    model = Category
    fields = ("type",)
    success_url = reverse_lazy("news:category-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Category"
        return context



class CategoryUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Category
    fields = ("type",)
    success_url = reverse_lazy("news:category-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Category"
        return context



class CategoryDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Category
    success_url = reverse_lazy("news:category-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel"] = "news:category-table"
        return context


class NewsDetailView(DetailView):
    """
    Detail of News
    """

    template_name = "news/news-detail.html"
    model = News
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recent"] = News.objects.all()
        return context


class NewsView(TemplateView):
    template_name = "news/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news"] = News.objects.all()
        return context

class AllNewsView(TemplateView):
    template_name = "news/all-news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news"] = News.objects.all()
        return context

class NewsTableView(AllUserRequiredMixin,TemplateView):
    """
    data view table
    """
    template_name = "admin/news/news-table.html"

    def get_context_data(self, **kwargs):
        context = super(NewsTableView, self).get_context_data(**kwargs)
        context["news"] = News.objects.all()
        context["title"] = "News"
        return context

class AddAdminNewsView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/news/add-news.html"
    form_class = NewsForm
    success_url = reverse_lazy("news:news-table")

    def get_context_data(self, **kwargs):
        context = super(AddAdminNewsView, self).get_context_data(**kwargs)
        context["title"] = "News"
        return context



class EditAdminNewsView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/news/edit-news.html"
    model = News
    form_class = NewsForm
    success_url = reverse_lazy("news:news-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "News"
        return context



class NewsDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = News
    success_url = reverse_lazy("news:news-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel"] = "news:news-table"
        return context


"""===================================
---- Recent Activity section  -----
======================================"""


class RecentActivityDetailView(DetailView):
    template_name = "news/recent-activity-detail.html"
    model = RecentActivities
    context_object_name = "activities"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recents"] = RecentActivities.objects.all()
        return context


class RecentActivityView(TemplateView):
    template_name = "news/recent-activity.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["activities"] = RecentActivities.objects.all()
        return context

class AllRecentActivityView(TemplateView):
    template_name = "news/all-recent-activity.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["activities"] = RecentActivities.objects.all()
        return context

class RecentActivityTableView(AllUserRequiredMixin,TemplateView):
    """ "
    add actvity
    """

    template_name = "admin/news/recent-activity-table.html"

    def get_context_data(self, **kwargs):
        context = super(RecentActivityTableView, self).get_context_data(**kwargs)
        context["activities"] = RecentActivities.objects.all()
        context["title"] = "Recent Activity"
        return context



class AddAdminRecentView (TemplateView):
    template_name = "admin/news/add-recent-activity.html"
class EditAdminRecentView (TemplateView):
    template_name = "admin/news/edit-recent-activity.html"

class AddAdminRecentView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/news/add-recent-activity.html"
    form_class = RecentActivitiesForm
    success_url = reverse_lazy("news:recentactivity-table")

    def get_context_data(self, **kwargs):
        context = super(AddAdminRecentView, self).get_context_data(**kwargs)
        context["title"] = "Recent Activity"
        return context



class EditAdminRecentView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/news/edit-recent-activity.html"
    model = RecentActivities
    form_class = RecentActivitiesForm
    success_url = reverse_lazy("news:recentactivity-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Recent Activity"
        return context



class RecentActivityDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = RecentActivities
    success_url = reverse_lazy("news:recentactivity-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel"] = "news:recentactivity-table"
        return context
# ##############################################################
# class AddAdminNewsView(TemplateView):
#     template_name = "admin/news/add-news.html"

###########################recent activity ###################

"""===================================
------ dam knowledge client side-------
======================================"""


class LiteratureView(TemplateView):
    template_name = "dam-knowledge/literatures.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dam_literatures"] = DamLiteraures.objects.all()
        context["title"] = "Dam Literatures"
        return context

class DamKnowledgeSalientFeaturesView(TemplateView):
    template_name = "dam-knowledge/features.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dam_salient_features"] = DamSalientFeatures.objects.all()
        return context



class PipeLineView(TemplateView):
    template_name = "dam-knowledge/pipeline.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["storage_project_pipeline"] = StorageProjectInPipeline.objects.all()
        return context


class NameOfDamView(TemplateView):
    template_name = "dam-knowledge/name-of-dam.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name_of_dam"] = NameOfDam.objects.all()
        context["title"] = "Name of Dam"
        return context



class LakeView(TemplateView):
    template_name = "dam-knowledge/lake.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lakes"] = Lake.objects.all()
        return context






# admin dam knowledge


# administration
class AdministrationLoginView(TemplateView):
    template_name = "administration/login.html"


# ----------------------CRUD operation on darta---------------------
class DartaChalaniView(AllUserRequiredAndAdminstration,TemplateView):
    template_name = "administration/darta-chalani.html"


class DartaListView(AllUserRequiredAndAdminstration,TemplateView):
    template_name = "administration/darta-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dartas"] = Darta.objects.all().order_by("-id")
        print("darta",context["dartas"])
        return context



class DartaFormView(SuccessMessageMixin,AllUserRequiredAndAdminstration, CreateView):
    """
    darta form display in client side
    """

    template_name = "administration/darta-form.html"
    form_class = DartaForm
    success_url = reverse_lazy("news:darta-list")

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            files = request.FILES.getlist("image")
            if files:
                bulk_file_upload = []
                for element in files:
                    upload_file = Darta(
                        darta_no = form.cleaned_data["darta_no"],
                        date = form.cleaned_data["date"],
                        patra_no = form.cleaned_data["patra_no"],
                        cha_no = form.cleaned_data["cha_no"],
                        patra_received_date = form.cleaned_data["patra_received_date"],
                        sender = form.cleaned_data["sender"],
                        address = form.cleaned_data["address"],
                        subject = form.cleaned_data["subject"],
                        medium = form.cleaned_data["medium"],
                        remark = form.cleaned_data["remark"],
                        image = element

                    )
                    bulk_file_upload.append(upload_file)
                Darta.objects.bulk_create(bulk_file_upload)
                return redirect(reverse("news:darta-list"))




class DartaUpdateView(UpdateSuccessMixin,AllUserRequiredAndAdminstration, UpdateView):
    model = Darta
    form_class = DartaForm
    context_object_name = "darta"
    template_name = "administration/darta-update.html"
    success_url = reverse_lazy("news:darta-list")



class DartaDeleteView(DeleteSuccessMixin,AllUserRequiredAndAdminstration, DeleteView):
    template_name = "admin/delete.html"
    model = Darta
    success_url = reverse_lazy("news:darta-list")


class DartaDetailView(AllUserRequiredAndAdminstration,DetailView):
    model = Darta
    form_class = DartaForm
    context_object_name = "darta"
    template_name = "registration/help.html"


# -------------------------------End of Darta View----------------------


# --------------------------CRUD for chalani----------------------


class ChalaniListView(AllUserRequiredAndAdminstration,ListView):
    template_name = "administration/chalani-list.html"
    model = Chalani
    context_object_name = "chalani"



class ChalaniFormView(SuccessMessageMixin,AllUserRequiredAndAdminstration, CreateView):
    """
    chalani form display in client side
    """

    template_name = "administration/chalani-form.html"
    form_class = ChalaniForm
    success_message = "Chalani Added Successfully"
    success_url = reverse_lazy("news:chalani-list")


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            files = request.FILES.getlist("image")
            if files:
                bulk_file_upload = []
                for element in files:
                    upload_file = Chalani(
                        chalani_no = form.cleaned_data["chalani_no"], #चलानी नंं.*
                        date = form.cleaned_data["date"], #चलानी मिति*
                        patra_no = form.cleaned_data["patra_no"],
                        chalani_perform_date = form.cleaned_data["chalani_perform_date"],
                        sender = form.cleaned_data["sender"],
                        address = form.cleaned_data["address"],
                        subject = form.cleaned_data["subject"],
                        remark = form.cleaned_data["remark"],
                        image = element

                    )
                    bulk_file_upload.append(upload_file)
                Chalani.objects.bulk_create(bulk_file_upload)
                return redirect(reverse("news:chalani-list"))
        else:
            context = {'form':form}
            print("form",form.errors)
            return render(self.request, "administration/chalani-form.html",context)





class ChalaniUpdateView(UpdateSuccessMixin,AllUserRequiredAndAdminstration, UpdateView):
    model = Chalani
    form_class = ChalaniForm
    context_object_name = "chalani"
    template_name = "administration/chalani-update.html"
    success_url = reverse_lazy("news:chalani-list")




class ChalaniDeleteView(DeleteSuccessMixin,AllUserRequiredAndAdminstration, DeleteView):
    template_name = "admin/delete.html"
    model = Chalani
    success_url = reverse_lazy("news:chalani-list")



class ChalaniDetailView(DetailView):
    model = Chalani
    form_class = ChalaniForm
    context_object_name = "chalani"
    template_name = "registration/help.html"
# -------------------------------------End of Chalani---------------

# ============= upload file===============

class CUploadFileView(AllUserRequiredAndAdminstration, TemplateView):
    template_name = "administration/upload-file/file-table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "administration_file_upload"
        context["files"] = AdminstrationUploadFile.objects.all().order_by("-id")
        return context

class CAddUploadFileView(
    AddSuccessMixin, AllUserRequiredAndAdminstration, CreateView
):
    template_name = "administration/upload-file/add-file.html"
    form_class = AdminstrationUploadFileForm
    success_url = reverse_lazy("company:administration-file")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "File"
        return context
    
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            fiscal_year = form.cleaned_data["fiscal_year"]
            title = form.cleaned_data["title"]
            files = request.FILES.getlist("files")
            print("files",files)
            if files:
                bulk_file_upload = []
                for element in files:
                    upload_file = AdminstrationUploadFile(
                        fiscal_year=fiscal_year,
                        title=title,
                        files=element,

                    )
                    bulk_file_upload.append(upload_file)
                AdminstrationUploadFile.objects.bulk_create(bulk_file_upload)
                    # doc = Documents.objects.create(
                    #     category=category, name=name, file=element
                    # )
                return redirect(reverse("news:c-upload-file"))



class CEditUploadUpdateFileView(
    UpdateSuccessMixin, AllUserRequiredAndAdminstration, UpdateView
):
    template_name = "administration/upload-file/edit-file.html"
    model = AdminstrationUploadFile
    fields = [
        "fiscal_year",
        "title",
        "files",
    ]
    success_url = reverse_lazy("news:c-upload-file")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "administration-file"
        return context


class CEditUploadDeleteFileView(
    DeleteSuccessMixin, AllUserRequiredAndAdminstration, DeleteView
):
    template_name = "admin/delete.html"
    model = AdminstrationUploadFile
    success_url = reverse_lazy("news:c-upload-file")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "administration-file"
        return context





class AdminProfileView(TemplateView):
    template_name = "admin/administration/admin-profile.html"


"""===================================
---- messages section   -----
======================================"""


# class MessageView(AllUserRequiredMixin,TemplateView):
#     template_name = "admin/message.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["messages"] = Message.objects.all()
#         return context



class MessageView(AllUserRequiredMixin,TemplateView):
    template_name = "admin/message.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message_data"] = Message.objects.all()
        context["title"] = "Messages"
        return context


class MessageCreateView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    form_class = MessageForm
    success_url = reverse_lazy("news:admin-message")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Message"
        return context



class MessageUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("news:admin-message")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "message"
        return context



class MessageDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Message
    success_url = reverse_lazy("news:admin-message")


"""===================================
---- Notice section section  -----
======================================"""


class NoticeView(TemplateView):
    template_name = "admin/news/notice-modal.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notices"] = HomeNotice.objects.all()
        context["title"] = "Notice"
        return context



class NoticeCreateView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    form_class = HomeNoticeForm
    success_url = reverse_lazy("news:notice")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Notice"
        return context



class NoticeUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = HomeNotice
    form_class = HomeNoticeForm
    success_url = reverse_lazy("news:notice")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Notice"
        return context



class NoticeDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = HomeNotice
    success_url = reverse_lazy("news:notice")


class DartaSearch(ListView):
    """
    Darta search
    """
    template_name = "administration/darta-list.html"
    model = Darta

    def get_queryset(self): # new
        print("darta from",self.request.GET.get("from"))
        from_date = self.request.GET.get("from",None)
        to_date = self.request.GET.get("to",None)
        darta =  Darta.objects.filter(
            Q(date__gte=from_date) & Q(date__lte=to_date)
        )
        
        print("darta",darta)
        return darta
    
    def  get_context_data(self, *args, **kwargs):
        context = super(DartaSearch,self).get_context_data(**kwargs)
        querySet = self.get_queryset()

        context["darta"] = querySet


        return context