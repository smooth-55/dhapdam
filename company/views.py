import json
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
    View,
)
from .models import (
    Photos,
    Videos,
    Introduction,
    ImportantLinks,
    Policy,
    Structure,
    Downloads,
    CitizenCharter,
    Documents,
    Contact,
    HomepageSliderImages,
    Darta,
    Chalani,
    ConstructionWork,
    Reservoir,
    StakeHolders,
    FiscalYear,
    DocumentCategory,
    CompanyProfile,
    AccountUploadFile,
    AdminstrationUploadFile,
    CurrentBudget,
    CapitalBudget,
    PhotoCategory,
)
from contracts.models import Contract
from users.models import UserProfile, EmployeeProfile
from .forms import *
from users.forms import RegisterForm, UpdateUserForm, EmployeeForm
from django.urls import reverse_lazy, reverse
from company.utils.calculation import (
    calc_cumulative,
    periodic_percent,
    yearly_percentage,
    graph_calc,
    calculate_total,
    firsttrim_data_update,
    secondtrim_data_update,
    thirdtrim_data_update,
    yearly_percentage_trimester,
    calc_cumulative_physical_progress,
    overall_graph_calc,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.conf import settings
from django.views.generic.edit import FormView
from django.views import View
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

# from bagmati.settings import EMAIL_HOST_USER
from django.utils.html import strip_tags
from django.conf import settings

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from users.decorators import (
    AllUserRequiredMixin,
    AccountantRequiredMixin,
    AdminstrationRequiredMixin,
    AllUserRequiredAndAdminstration,
    AllUserRequiredAndAccounant,
)
from django.shortcuts import redirect
from construction.models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from dam.models import (
    IntroductionOfDam,
    DamIntroduction,
    SalientFeatures,
    LocationAndAccessibility,
    EnvironmentalAspects,
    Maps,
)
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from pytube import YouTube
from django.db.models import F

########## about us ###############
class AddSuccessMixin(SuccessMessageMixin, View):
    """
    success messages after added data
    """

    success_message = "Form has been Successfully Submitted"


class UpdateSuccessMixin(SuccessMessageMixin, View):
    """
    success messages after updated data
    """

    success_message = "Form has been Successfully Updated"


class DeleteSuccessMixin(SuccessMessageMixin, View):
    """
    success messages after delete data
    """

    success_message = "Data has been Successfully deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class AboutView(TemplateView):
    """
    about us
    """

    template_name = "aboutus/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["introduction"] = Introduction.objects.last()
        except:
            context["introduction"] = None
        return context


class ContactView(AddSuccessMixin, CreateView):
    form_class = ContactForm
    template_name = "frontend/contact.html"
    success_url = reverse_lazy("company:contact")

    def post(self, request, *args, **kwargs):
        form = ContactForm(self.request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]

            sender_name, from_email, to, = (
                name,
                email,
                settings.EMAIL_HOST_USER,
            )

            html_content = render_to_string(
                "email.html", {"sender_name": sender_name, "message": message}
            )  # render with dynamic value
            text_content = strip_tags(
                html_content
            )  # Strip the html tag. So people can see the pure text at least.
            subject = "Greetings"

            # create the email, and attach the HTML version as well.
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")

            msg.send()
            messages.success(request, "Message successfully send", extra_tags="contact")

            return super().form_valid(form)

        else:
            print("form errors", form.errors)
            if form.errors:
                form_errors = form.errors
            else:
                form_errors = None
            return render(
                request,
                "frontend/contact.html",
                context={"form": form, "form_errors": form_errors},
            )


class CirChatView(TemplateView):
    """
    citizen charter
    """

    template_name = "aboutus/citchat.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["citizen"] = CitizenCharter.objects.last()
        except:
            context["citizen"] = None
        return context


class StructureView(TemplateView):
    """
    organization structure
    """

    template_name = "aboutus/orgstr.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["structure"] = Structure.objects.last()
        except:
            context["structure"] = None
        return context


# photo category
"""===================================
------ Photo category crud  ---
======================================"""


# class PhotoCategoryView (TemplateView):
#     template_name = "admin/gallery/photo-category.html"


class PhotoCategoryView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/gallery/photo-category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["photo_category"] = PhotoCategory.objects.all()
        context["title"] = "Photo category"
        return context


class PhotoCategoryCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    # since it consists two fields
    model = PhotoCategory
    fields = ("name",)
    success_url = reverse_lazy("company:photo-category")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Photo Category"
        return context


class PhotocategoryUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = PhotoCategory
    fields = ("name",)
    success_url = reverse_lazy("company:photo-category")

    def get_context_data(self, **kwargs):
        print("shshshshsh")
        context = super().get_context_data(**kwargs)
        context["title"] = "Photo Category"
        return context


class PhotoCategoryDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = PhotoCategory
    success_url = reverse_lazy("company:photo-category")


class PhotoView(TemplateView):
    """
    List of photos
    """

    template_name = "gallery/photo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["photos"] = Photos.objects.filter(category__isnull=True).order_by("-id")
        context["photos_catgeory"] = PhotoCategory.objects.all().order_by("-id")
        print("data", context["photos_catgeory"])
        return context


class PhotoCategorysView(DetailView):
    """
    List of photos
    """

    model = Photos
    template_name = "gallery/photo_category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        photo_id = self.object.pk
        try:
            photo = Photos.objects.get(id=self.object.pk)
        except Photos.DoesNotExist:
            pass
        print("photo_id", photo.category)
        context["photos"] = Photos.objects.filter(category=photo.category).order_by(
            "-id"
        )
        print("data", context["photos"])
        return context


class VideoView(TemplateView):
    """
    List of Videos
    """

    template_name = "gallery/video.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        videos = Videos.objects.all().order_by("-id")
        thumbnail = []
        title = []
        links = []
        for video in videos:
            link = video.link
            thumbnail.append(YouTube(link).thumbnail_url)
            title.append(YouTube(link).title)
            links.append(link)
        context["thumbnails"] = thumbnail
        print("thumbnail", thumbnail)
        print("title", title)
        context["videos_all"] = zip(thumbnail, title, links)
        return context


class ImportantLinkView(TemplateView):
    """
    Important Links
    """

    template_name = "frontend/imp-link.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["implinks"] = ImportantLinks.objects.all()
        return context


class FiscalYearAddView(AddSuccessMixin, CreateView):
    """
    Fiscal year
    """

    form_class = FiscalYearForm
    template_name = "company/fiscalyear_form.html"
    success_url = reverse_lazy("company:fiscalyear-add")


class TrimesterView(TemplateView):
    template_name = "company/display.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["years"] = FiscalYear.objects.all()
        return context


class FirstTrimesterAddView(FormView):
    """
    First trimester
    """

    template_name = "company/firsttrimester.html"
    success_url = reverse_lazy("company:firsttrimestermonth1-add")

    # pass all the form
    def get(self, request, *args, **kwargs):
        form = FirstTrimesterForm()
        form.prefix = "form"
        context = {
            "form": form,
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form1 = FirstTrimesterForm(self.request.POST, prefix="form")
        if form1.is_valid():
            f_month = form1.save(commit=False)
            periodic_amt = form1.cleaned_data["month1_periodic_amount"]
            month_name = form1.cleaned_data["month1"]
            periodic_tar = form1.cleaned_data["periodic_target"]
            cumulative_amt = calc_cumulative(periodic_amt, month_name)
            f_month.month1_cumulative_amount = cumulative_amt
            f_month.save()
            return super().form_valid(form1)


# progress
class ProgressView(ListView):
    template_name = "frontend/progress.html"
    model = FiscalYear

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == "GET":
            year_id = self.request.GET.get("yearId")
            if year_id is not None:
                yrs = FiscalYear.objects.get(id=year_id)
                context["yrs"] = yrs
                context["fiscal"] = FiscalYear.objects.all()

                # first trim
                try:
                    first_trim = FirstTrimester.objects.get(year=yrs)

                except FirstTrimester.DoesNotExist:
                    first_trim = None

                try:
                    second_trim = SecondTrimester.objects.get(year=yrs)

                except SecondTrimester.DoesNotExist:
                    second_trim = None

                try:
                    third_trim = ThirdTrimester.objects.get(year=yrs)

                except ThirdTrimester.DoesNotExist:
                    third_trim = None

            else:
                yrs = FiscalYear.objects.last()
                context["yrs"] = yrs
                context["fiscal"] = FiscalYear.objects.all()

                # first trim

                try:
                    first_trim = FirstTrimester.objects.get(year=yrs)

                except FirstTrimester.DoesNotExist:
                    first_trim = None

                try:
                    print("yrs", yrs)
                    second_trim = SecondTrimester.objects.get(year=yrs)

                except SecondTrimester.DoesNotExist:
                    second_trim = None

                try:
                    third_trim = ThirdTrimester.objects.get(year=yrs)

                except ThirdTrimester.DoesNotExist:
                    third_trim = None
            context["first_trim"] = first_trim
            context["second_trim"] = second_trim
            context["third_trim"] = third_trim
            # calculate periodic percentage of first trimester
            print("first trim", first_trim)
            if first_trim is not None:
                if first_trim.trimester_cumulative and first_trim.periodic_target:
                    periodic_first_trim = periodic_percent(
                        first_trim.trimester_cumulative, first_trim.periodic_target
                    )
                    print("periodic_first_trim", periodic_first_trim)
                    context["periodic_first_trim"] = periodic_first_trim

            if second_trim:
                if second_trim.trimester_cumulative and second_trim.periodic_target:
                    periodic_second_trim = periodic_percent(
                        second_trim.trimester_cumulative, second_trim.periodic_target
                    )
                    print("periodic_second_trim", periodic_second_trim)
                    context["periodic_second_trim"] = periodic_second_trim

            if third_trim:
                if third_trim.trimester_cumulative and third_trim.periodic_target:
                    periodic_third_trim = periodic_percent(
                        third_trim.trimester_cumulative, third_trim.periodic_target
                    )
                    context["periodic_third_trim"] = periodic_third_trim

            total = calculate_total(first_trim, second_trim, third_trim)
            context["total"] = total

            # pass yealry percentage
            if yrs:
                year_percentage_data = yearly_percentage_trimester(yrs)
                print("year_percentage_data", year_percentage_data)
                context["first_trim_yearly_percentage"] = year_percentage_data.get(
                    "first_trim_calc"
                )
                context["second_trim_yearly_percentage"] = year_percentage_data.get(
                    "second_trim_calc"
                )
                context["third_trim_yearly_percentage"] = year_percentage_data.get(
                    "third_trim_calc"
                )
                context["overall_yearly_percentage"] = year_percentage_data.get(
                    "overall_yearly_percentage"
                )
                print("555555555555555555555555555555")

                # calculate the cumulative physical progress
                cumulative_physical_progress = calc_cumulative_physical_progress(yrs)
                context[
                    "cumulative_physical_progress"
                ] = calc_cumulative_physical_progress(yrs)
                print(
                    "cumulative_physical_progress******************",
                    context["cumulative_physical_progress"],
                )

        return context


class GraphView(TemplateView):
    """
    display the Annual physical progress Graph
    """

    template_name = "frontend/progress_graph.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == "GET":
            year_id = self.request.GET.get("yearId")

            if year_id is not None:
                yrs = FiscalYear.objects.get(id=year_id)
                year_name = FiscalYear.objects.get(id=yrs.id)
                context["yrs"] = yrs
                context["fiscal"] = FiscalYear.objects.all()
                total_cost = graph_calc(year_name)
                print("total_cost&&&&&&&&&&&&&&", total_cost)
                # context["total_costs"] = total_cost
                data = JsonResponse(
                    {
                        "title": None,
                        "data": {
                            "labels": [
                                "Shrawn",
                                "Bhadra",
                                "Ashoj",
                                "Kartik",
                                "Mangsir",
                                "Poush",
                                "Magh",
                                "Falgun",
                                "Chaitra",
                                "Baisakh",
                                "Jestha",
                                "Asar",
                            ],
                            "datasets": [
                                {
                                    "type": "line",
                                    "data": total_cost,
                                    "backgroundColor": "transparent",
                                    "borderColor": "#007bff",
                                    "pointBorderColor": "#007bff",
                                    "pointBackgroundColor": "#007bff",
                                }
                            ],
                        },
                    }
                )
                print("data", data)
                return data

            else:
                print("else")
                yrs = FiscalYear.objects.last()
                context["yrs"] = yrs
                context["fiscal"] = FiscalYear.objects.all()

                # get the different each month data
                year_name = FiscalYear.objects.get(id=yrs.id)
                total_cost = graph_calc(year_name)
                context["total_cost"] = total_cost
                return context


# graph ajax
def GraphAjaxView(request):
    year_id = request.GET.get("yearId")
    if year_id is not None:
        yrs = FiscalYear.objects.get(id=year_id)
        year_name = FiscalYear.objects.get(id=yrs.id)
        fiscal_year = FiscalYear.objects.all()
        total_cost = graph_calc(year_name)
        context = {"fiscal_year": fiscal_year}
        total_dict = {}
        total_dict["data"] = total_cost
        alldata = JsonResponse(
            {
                "title": None,
                "data": {
                    "labels": [
                        "Shrawn",
                        "Bhadra",
                        "Ashoj",
                        "Kartik",
                        "Mangsir",
                        "Poush",
                        "Magh",
                        "Falgun",
                        "Chaitra",
                        "Baisakh",
                        "Jestha",
                        "Asar",
                    ],
                    "datasets": [
                        {
                            "type": "line",
                            "data": list(total_cost),
                            "backgroundColor": "transparent",
                            "borderColor": "#007bff",
                            "pointBorderColor": "#007bff",
                            "pointBackgroundColor": "#007bff",
                        }
                    ],
                },
            }
        )
        return alldata
        # return render(request, 'frontend/progress_graph.html',total_dict,context)


"""
#### BACKUP CODE BASED ON THE REQUIREMENT OF CLIENT FOR FUTURE TO DISPLAY DATA BASED ON TRIMESTER###
class OverallGraphView(TemplateView):
    
    template_name = "frontend/progress_overall_graph.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == "GET":
            year_id = self.request.GET.get("yearId")

            if year_id is not None:
                yrs = FiscalYear.objects.get(id=year_id)
                year_name = FiscalYear.objects.get(id=yrs.id)
                context["yrs"] = yrs
                context["fiscal"] = FiscalYear.objects.all()
                total_cost = overall_graph_calc(year_name)
                # context["total_costs"] = total_cost
                data = JsonResponse(
                    {
                        "title": None,
                        "data": {
                            "labels": [
                                "First Trimester",
                                "Second Trimester",
                                "Third Trimester",
                            ],
                            "datasets": [
                                {
                                    "type": "line",
                                    "data": total_cost,
                                    "backgroundColor": "transparent",
                                    "borderColor": "#007bff",
                                    "pointBorderColor": "#007bff",
                                    "pointBackgroundColor": "#007bff",
                                }
                            ],
                        },
                    }
                )
                print("data", data)
                return data

            else:
                yrs = FiscalYear.objects.last()
                context["yrs"] = yrs
                context["fiscal"] = FiscalYear.objects.all()

                # get the different each month data
                year_name = FiscalYear.objects.get(id=yrs.id)
                total_cost = overall_graph_calc(year_name)
                context["total_cost"] = total_cost
                return context
"""
class OverallGraphView(TemplateView):
    """
    Overall physical progress Graph
    """

    template_name = "frontend/progress_overall_graph.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        third_trim = ThirdTrimester.objects.all().order_by("-id").values("year__year","overrall")
        year_list = [] 
        overall_list = []
        for year in third_trim:
            if year["overrall"]:
                year_list.append(str(year["year__year"]))
                overall_list.append(year["overrall"])
        context["yrs_data"] = year_list
        context["overall"] = overall_list
        return context



def OverallGraphAjaxView(request):
    year_id = request.GET.get("yearId")
    if year_id is not None:
        yrs = FiscalYear.objects.get(id=year_id)
        print("yrs*******************&&&&&&&&&&&&&&&&&777",yrs)
        year_name = FiscalYear.objects.get(id=yrs.id)
        fiscal_year = FiscalYear.objects.all()
        total_cost = overall_graph_calc(year_name)
        print("total cost in views",total_cost)

        context = {"fiscal_year": fiscal_year}
        total_dict = {}
        total_dict["data"] = total_cost
        alldata = JsonResponse(
                    {
                        "title": None,
                        "data": {
                            "labels": [
                                "First Trimester",
                                "Second Trimester",
                                "Third Trimester",
                            ],
                            "datasets": [
                                {
                                    "type": "line",
                                    "data": total_cost,
                                    "backgroundColor": "transparent",
                                    "borderColor": "#007bff",
                                    "pointBorderColor": "#007bff",
                                    "pointBackgroundColor": "#007bff",
                                }
                            ],
                        },
                    }
                )
        return alldata

class DocumentView(AllUserRequiredAndAdminstration, TemplateView):
    template_name = "frontend/document.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = Documents.objects.all()
        return context


# download
class DownloadView(ListView):
    template_name = "frontend/download.html"
    queryset = Downloads.objects.all()


# nagmati dam
class NagmatiDamView(TemplateView):
    template_name = "nagmati/nagmatidam.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            intro = IntroductionOfDam.objects.get(introduction__project_name="nagmati")
            context["intro"] = intro
        except IntroductionOfDam.DoesNotExist:
            context["intro"] = None

        return context


class NagmatiFeaturesView(TemplateView):
    template_name = "nagmati/nagmati-features.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["features"] = SalientFeatures.objects.get(
                introduction__project_name="nagmati"
            )
        except:
            context["features"] = None
        return context


class NagmatiLocationView(TemplateView):
    template_name = "nagmati/nagmati-location.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["location"] = LocationAndAccessibility.objects.get(
                introduction__project_name="nagmati"
            )

        except:
            context["location"] = None

        return context


class NagmatiMapsView(TemplateView):
    template_name = "nagmati/nagmati-maps.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            maps = Maps.objects.filter(introduction__project_name="nagmati")
            context["maps"] = maps
        except:
            context["maps"] = None
        return context


class NagmatiStatusView(TemplateView):
    template_name = "nagmati/nagmati-status.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            status_of_project = EnvironmentalAspects.objects.get(
                introduction__project_name="nagmati"
            )
            context["status_of_project"] = status_of_project
        except:
            context["status_of_project"] = None
        return context


# project map
class ProjectMapView(TemplateView):
    template_name = "frontend/projectmap.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            dhapdam_map = Maps.objects.filter(introduction__project_name="dhapdam")
            context["dhapdam_map"] = dhapdam_map
        except:
            context["dhapdam_map"] = None
        try:
            nagmati_map = Maps.objects.filter(introduction__project_name="nagmati")
            context["nagmati_map"] = nagmati_map
        except:
            context["nagmati_map"] = None
        return context


# policy
class PolicyUserView(TemplateView):
    template_name = "frontend/spp.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["policy"] = Policy.objects.filter(types=2)
        except:
            context["policy"] = None
        return context


class ActPolicyView(TemplateView):
    template_name = "frontend/actreg.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["policy"] = Policy.objects.filter(types=1)
        except:
            context["policy"] = None
        return context


##------------------------------------- construction starts -------------------------------##
"""===================================
------------ Design Drawing  starts  ---
======================================"""


class DesignDrawingView(ListView):
    model = Design
    template_name = "construction/design-drawing.html"


"""===================================
-----------Method od statement  starts  ---
======================================"""


class MethodOfStatementView(ListView):
    model = MethodOfStatements
    template_name = "construction/mos.html"


class ReportsView(ListView):
    model = Reports
    template_name = "construction/reports.html"


"""===================================
-----------Footage starts  ---
======================================"""


class TestFootageView(ListView):
    model = TestFootages

    template_name = "construction/footage-test.html"


class WorkFootageView(ListView):
    model = WorkFootages
    template_name = "construction/footage-work.html"


# Equipments
"""===================================
------------ Equipments starts  ---
======================================"""


class BrazingEquipmentView(ListView):
    model = BrazingEquipments
    template_name = "construction/equipment/eq-brazing.html"


class ConcretingEquipmentView(ListView):
    model = ConcretingEquipments
    template_name = "construction/equipment/eq-concreting.html"


class EarthEquipmentView(ListView):
    model = EarthMovingCompaction
    template_name = "construction/equipment/eq-earth.html"


class GroutingEquipmentView(ListView):
    model = GroutingEquipments
    template_name = "construction/equipment/eq-grouting.html"


class SurveyEquipmentView(ListView):
    model = SurveyEquipments
    template_name = "construction/equipment/eq-survey.html"


class LabEquipmentView(ListView):
    model = LabEquipments
    template_name = "construction/equipment/eq-lab.html"


class GeophysicalEquipmentView(ListView):
    model = GeophysicalInvestigationEquipments
    template_name = "construction/equipment/eq-geophysical.html"


# work


"""===================================
------------ work test starts  ---
======================================"""


class ConcreteTestView(ListView):
    model = ConcreteTests
    template_name = "construction/test/work/test-concrete.html"


class CompactionTestView(ListView):
    model = CompactionTests
    template_name = "construction/test/work/test-compaction.html"


class GroutingTestView(ListView):
    model = GroutingTests
    template_name = "construction/test/work/test-grouting.html"


class CopperTestView(ListView):
    model = CopperWaterStopperTests
    template_name = "construction/test/work/test-copper.html"


class PermeabilityTestView(ListView):
    model = PermeabilityTests
    template_name = "construction/test/work/test-permeability.html"


class GeophysicalTestView(ListView):
    model = Geophysical
    template_name = "construction/test/work/test-geophysical.html"


class CoreDrillTestView(ListView):
    model = CoreDrilltest
    template_name = "construction/test/work/test-core-drill.html"


"""===================================
--------- QA/QC Documentation ---------
======================================"""


class DocumentationTestView(ListView):
    model = QADocumentation
    template_name = "construction/test/test-document.html"


##------------------------------ construction section ---------------------------##
# construction/ Material Test
# material TEst
"""===================================
--------- Material tests --------------
======================================"""


class EarthFillingTestView(ListView):
    model = EarthFillingMaterial
    template_name = "construction/test/material/earth-fill.html"


class FaceSlabATestView(ListView):
    model = FaceSlabBeddingMaterial2A
    template_name = "construction/test/material/bedding.html"


class FaceSlabBTestView(ListView):
    model = FaceSlabBeddingMaterial2B
    template_name = "construction/test/material/face-slab.html"


class SmallRockTestView(ListView):
    model = SmallSizeRock300MM
    template_name = "construction/test/material/small-rock.html"


class FirstClassTestView(ListView):
    model = SmallSizeRock600MM
    template_name = "construction/test/material/first-rock.html"


class SecondClassTestView(ListView):
    model = SecondClassRock1000MM
    template_name = "construction/test/material/second-rock.html"


class RockFillTestView(ListView):
    model = RockFill
    template_name = "construction/test/material/rock-fill.html"


class ConcreteLargeTestView(ListView):
    model = ConcreteAggregate40mm
    template_name = "construction/test/material/ca-40.html"


class ConcreteMediumTestView(ListView):
    model = ConcreteAggregate20mm
    template_name = "construction/test/material/ca-20.html"


class ConcreteSmallTestView(ListView):
    model = ConcreteAggregate10mm
    template_name = "construction/test/material/ca-10.html"


class FineAggregateTestView(ListView):
    model = FineAggregate

    template_name = "construction/test/material/fine-aggregate.html"


class CementTestView(ListView):
    model = Cement
    template_name = "construction/test/material/cement.html"


class GranularTestView(ListView):
    model = GranularSubBase
    template_name = "construction/test/material/granular.html"


# admin
class UserNavigateView(LoginRequiredMixin, TemplateView):
    template_name = "admin/dashboard.html"

    def dispatch(self, request, *args, **kwargs):
        print("dispatch method")
        if self.request.user.is_authenticated:
            print("dgagag", type(self.request.user.designation))
            print("type", type(self.request.user.is_adminstration))

            designation = self.request.user
            if self.request.user.is_adminstration:
                print("administration")
                return redirect("company:darta-table")
            elif (
                self.request.user.is_unit_chief
                or self.request.user.is_engineer
                or self.request.user.is_engineer_geologist
                or self.request.user.is_admin
            ):
                print("chief")
                return redirect("company:admin-dashboard")
            elif self.request.user.is_accountant:
                print("acoountant")
                return redirect("company:file-budget")
            else:
                print("else")
                pass
        else:
            return redirect("users:login")

        return super(UserNavigateView, self).dispatch(request, *args, **kwargs)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "admin/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["darta"] = Darta.objects.all()
        context["chalani"] = Chalani.objects.all()
        context["projects"] = Contract.objects.all()
        context["users"] = EmployeeProfile.objects.filter(
            is_transferred=False, is_projecthead=False
        )

        # for graph
        try:
            year = FiscalYear.objects.last()

            overall = []

            first_trim = FirstTrimester.objects.get(year=year)
            second_trim = SecondTrimester.objects.get(year=year)
            third_trim = ThirdTrimester.objects.get(year=year)

            overall.append(first_trim.overrall)
            overall.append(second_trim.overrall)
            overall.append(third_trim.overrall)

        except:
            year = None
            overall = None
        context["year"] = year
        context["overall"] = overall

        return context


# admin activity


# admin photo
"""===================================
------ photo section  ---
======================================"""


class PhotoTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/gallery/photo-table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["photos"] = Photos.objects.all()
        context["title"] = "Photos"
        return context


class PhotoCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    # since it consists of two fields
    form_class = PhotoForm
    success_url = reverse_lazy("company:photo-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Photos"
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            category = form.cleaned_data["category"]
            title = form.cleaned_data["title"]
            image = request.FILES.getlist("image")
            print("category", category)
            print("category", category)
            print("data")
            for element in image:
                doc = Photos.objects.create(
                    category=category, image=element, title=title
                )
            return redirect(reverse("company:photo-table"))


class PhotoUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Photos
    form_class = PhotoEditForm
    success_url = reverse_lazy("company:photo-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Photos"
        return context


class PhotoDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Photos
    success_url = reverse_lazy("company:photo-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel"] = "company:photo-table"
        return context


# admin video
"""===================================
------ video section  ---
======================================"""


class VideoTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/gallery/video-table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        videos = Videos.objects.all()
        context["title"] = "Videos"

        thumbnail = []
        title = []
        links = []
        video_id = []
        for video in videos:
            link = video.link
            thumbnail.append(YouTube(link).thumbnail_url)
            title.append(YouTube(link).title)
            links.append(link)
            video_id.append(video.id)
        context["admin_video"] = zip(thumbnail, title, links, video_id)
        return context


class VideoCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    form_class = VideoForm
    success_url = reverse_lazy("company:video-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Videos"
        return context


class VideoUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Videos
    form_class = VideoForm
    success_url = reverse_lazy("company:video-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Videos"
        return context


class VideoDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Videos
    success_url = reverse_lazy("company:video-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel"] = "company:video-table"
        return context


# about block
"""===================================
------ Introduction section  ---
======================================"""


class AboutIntroView(AllUserRequiredMixin, TemplateView):
    """
    data view table
    """

    template_name = "admin/about/intro.html"

    def get_context_data(self, **kwargs):
        context = super(AboutIntroView, self).get_context_data(**kwargs)
        context["introduction"] = Introduction.objects.all()
        context["title"] = "Introduction"
        return context


class AboutCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/about/addintro.html"
    form_class = IntroductionForm
    success_url = reverse_lazy("company:about-intro")

    def get_context_data(self, **kwargs):
        context = super(AboutCreateView, self).get_context_data(**kwargs)
        context["title"] = "Introduction"
        return context


class AboutUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/about/updateintro.html"
    model = Introduction
    form_class = IntroductionForm
    success_url = reverse_lazy("company:about-intro")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Introduction"
        return context


class AboutDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Introduction
    success_url = reverse_lazy("company:about-intro")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel"] = "company:about-intro"
        return context


"""=====================================
------ Citizen charter section  --
======================================"""


class CitizenTable(AllUserRequiredMixin, TemplateView):
    """
    data view table
    """

    template_name = "admin/about/citizen-charter.html"

    def get_context_data(self, **kwargs):
        context = super(CitizenTable, self).get_context_data(**kwargs)
        context["charter"] = CitizenCharter.objects.all()
        context["title"] = "Citizen Charter"
        return context


class CitizenCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    # since it consists of two fields
    model = CitizenCharter
    fields = "__all__"
    success_url = reverse_lazy("company:citizen-table")

    def get_context_data(self, **kwargs):
        context = super(CitizenCreateView, self).get_context_data(**kwargs)
        context["title"] = "Citizen Charter"
        return context


class CitizenUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = CitizenCharter
    fields = "__all__"
    success_url = reverse_lazy("company:citizen-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Citizen Charter"
        return context


class CitizenDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = CitizenCharter
    success_url = reverse_lazy("company:citizen-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel"] = "company:citizen-table"
        return context


"""=====================================
------ organization structure section  --
======================================"""


class OrganizationTableView(AllUserRequiredMixin, TemplateView):
    """
    data view table
    """

    template_name = "admin/about/organization.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["structure"] = Structure.objects.all()
        context["title"] = "Organization Structure"
        return context


class OrganizationCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    # since it consists of two fields
    model = Structure
    fields = ("file",)
    success_url = reverse_lazy("company:organization-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Organization Structure"
        return context


class OrganizationUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Structure
    fields = ("file",)
    success_url = reverse_lazy("company:organization-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Organization Structure"
        return context


class OrganizationDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Structure
    success_url = reverse_lazy("company:organization-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel"] = "company:organization-table"
        return context


"""=====================================
-------------- Policy  -------------
======================================"""


class PolicyView(AllUserRequiredMixin, TemplateView):
    """
    data view table
    """

    template_name = "admin/document/policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["policy"] = Policy.objects.all()
        context["title"] = "Policy/Law"
        return context


class PolicyCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    form_class = PolicyForm
    success_url = reverse_lazy("company:policy")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Policy"
        return context


class PolicyUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Policy
    form_class = PolicyForm
    success_url = reverse_lazy("company:policy")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Policy"
        return context


class PolicyDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Policy
    success_url = reverse_lazy("company:policy")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel"] = "company:policy"
        return context


"""=====================================
------- Important Link  --------
======================================"""


class ImpLinkTable(AllUserRequiredMixin, TemplateView):
    """
    data view table
    """

    template_name = "admin/document/imp-link-table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["implink"] = ImportantLinks.objects.all()
        context["title"] = "Important Link"
        return context


class ImpLinkCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    # since it consists two fields
    model = ImportantLinks
    fields = (
        "title",
        "link",
    )
    success_url = reverse_lazy("company:imp-link-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Important Link"
        return context


class ImpLinkUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = ImportantLinks
    fields = (
        "title",
        "link",
    )
    success_url = reverse_lazy("company:imp-link-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Important Link"
        return context


class ImpLinkDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = ImportantLinks
    success_url = reverse_lazy("company:imp-link-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel"] = "company:imp-link-table"
        return context


"""=====================================
------- Download  --------
======================================"""


class DownloadTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/document/download-table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["downloads"] = Downloads.objects.all()
        context["title"] = "Download"
        return context


class DownloadFileCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    # since it consists two fields
    model = Downloads
    fields = (
        "name",
        "file",
        # "size",
    )
    success_url = reverse_lazy("company:download-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Download"
        return context


class DownloadLinkCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    # since it consists two fields
    model = Downloads
    fields = (
        "name",
        # "size",
        "url",
    )
    success_url = reverse_lazy("company:download-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Download"
        return context


class DownloadFileUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Downloads
    fields = (
        "name",
        "file",
        "size",
    )
    success_url = reverse_lazy("company:download-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Download"
        return context


class DownloadLinkUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Downloads
    fields = (
        "name",
        "size",
        "url",
    )
    success_url = reverse_lazy("company:download-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Download"
        return context


class DownloadDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Downloads
    success_url = reverse_lazy("company:download-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel"] = "company:download-table"
        return context


"""=====================================
------- Document category --------
======================================"""


class DocumentCategoryView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/document/document-category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = DocumentCategory.objects.all()
        context["title"] = "Document category"
        return context


class DocumentCategoryCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    # since it consists two fields
    model = DocumentCategory
    fields = ("name",)
    success_url = reverse_lazy("company:document-category")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Document category"
        return context


class DocumentCategoryUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = DocumentCategory
    fields = ("name",)
    success_url = reverse_lazy("company:document-category")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Document Category"
        return context


class DocumentCategoryDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = DocumentCategory
    success_url = reverse_lazy("company:document-category")


"""=====================================
------- Document  --------
======================================"""


class DocumentTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/document/document.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = Documents.objects.all()
        context["title"] = "Documents"
        return context


class DocumentFilterTableView(AllUserRequiredMixin, DetailView):
    model = Documents
    template_name = "admin/document/document.html"

    def get_context_data(self, **kwargs):
        context = super(DocumentFilterTableView, self).get_context_data(**kwargs)
        context["documents"] = Documents.objects.filter(category=self.kwargs.get("pk"))
        return context


class DocumentCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/document_create.html"
    # since it consists two fields
    form_class = DocumentForm
    success_url = reverse_lazy("company:document-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Documents"
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            category = form.cleaned_data["category"]
            name = form.cleaned_data["name"]
            files = request.FILES.getlist("file")
            if files:
                for element in files:
                    doc = Documents.objects.create(
                        category=category, name=name, file=element
                    )
                return redirect(reverse("company:document-table"))


class DocumentUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Documents
    fields = (
        "category",
        "name",
        "file",
    )
    success_url = reverse_lazy("company:document-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Documents"
        return context


class DocumentDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Documents
    success_url = reverse_lazy("company:document-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel"] = "company:document-table"
        return context


"""=====================================
------- Company profile  --------
======================================"""

# company profile


class CompanyProfileView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/about/company-profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comprofiles"] = CompanyProfile.objects.all()
        context["title"] = "Company Profile"
        return context


class CompanyProfileCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    # since it consists two fields
    form_class = CompanyProfileForm
    success_url = reverse_lazy("company:company-profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Company Profile"
        return context


class CompanyProfileUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = CompanyProfile
    form_class = CompanyProfileForm
    success_url = reverse_lazy("company:company-profile")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Company Profile"
        return context


# users


class UsersTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/users/users-table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = UserProfile.objects.filter(is_admin=False)
        context["title"] = "User"
        return context


class AddUserView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/users/adduser.html"
    form_class = RegisterForm
    success_url = reverse_lazy("company:users")

    def form_valid(self, form):
        form_new = form.save(commit=False)
        form_new.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = UserProfile.objects.filter(is_admin=False)
        context["title"] = "User"
        return context


class EditUserView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/users/edituser.html"
    model = UserProfile
    form_class = UpdateUserForm
    success_url = reverse_lazy("company:users")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = UserProfile.objects.filter(is_admin=False)
        context["title"] = "User"
        return context


class DeleteUserView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = UserProfile
    success_url = reverse_lazy("company:users")


# contact


class ContactTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/contact-table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = Contact.objects.all()
        context["title"] = "Contact"
        return context


class ContactDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Contact
    success_url = reverse_lazy("company:contact-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel"] = "company:contact-table"
        return context


"""=====================================
-------------- Home slider  --------
======================================"""

# Home Slider


class HomeSliderTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/homeslider.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["homeslider"] = HomepageSliderImages.objects.all()
        context["title"] = "Home Slider"
        return context


class HomesliderCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    # since it consists two fields
    model = HomepageSliderImages
    fields = ("image",)
    success_url = reverse_lazy("company:homeslider")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home slider"
        return context


class HomesliderUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = HomepageSliderImages
    fields = ("image",)
    success_url = reverse_lazy("company:homeslider")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Home Slider"
        return context


class HomesliderDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = HomepageSliderImages
    success_url = reverse_lazy("company:document-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel"] = "company:homeslider"
        return context


"""=====================================
-------- Contruction work slider  --------
======================================"""


class ConstructSliderView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/construction-work.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["construction"] = ConstructionWork.objects.all()
        context["title"] = "Construction Work"
        return context


class ConstructionCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    # since it consists two fields
    model = ConstructionWork
    fields = (
        "image1",
        "image2",
        "image3",
    )
    success_url = reverse_lazy("company:construct-slider")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Construction Work"
        return context


class ConstructionUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = ConstructionWork
    fields = (
        "image1",
        "image2",
        "image3",
    )
    success_url = reverse_lazy("company:construct-slider")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Construction Work"
        return context


class ConstructionDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = ConstructionWork
    success_url = reverse_lazy("company:construct-slider")


"""=====================================
-------- stakeholder slider  --------
======================================"""


class StakeholderSliderView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/stakeholder.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stakeHolders"] = StakeHolders.objects.all()
        context["title"] = "StakeHolders"
        return context


class StakeholderCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    # since it consists two fields
    model = StakeHolders
    fields = (
        "image",
        "link",
    )
    success_url = reverse_lazy("company:stakeholder")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "StakeHolders"
        return context


class StakeholderUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = StakeHolders
    fields = (
        "image",
        "link",
    )
    success_url = reverse_lazy("company:stakeholder")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "StakeHolders"
        return context


class StakeholderDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = StakeHolders
    success_url = reverse_lazy("company:stakeholder")


"""=====================================
-------- reservoir work slider  --------
======================================"""


class ReservoirSliderView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/reservoir.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservoir"] = Reservoir.objects.all()
        context["title"] = "Reservoir"
        return context


class ReservoirCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    # since it consists two fields
    model = Reservoir
    fields = (
        "image1",
        "image2",
        "image3",
    )
    success_url = reverse_lazy("company:reservoir")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Reservoir"
        return context


class ReservoirUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Reservoir
    fields = (
        "image1",
        "image2",
        "image3",
    )
    success_url = reverse_lazy("company:reservoir")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Reservoir"
        return context


class ReservoirDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Reservoir
    success_url = reverse_lazy("company:reservoir")


# admin contract


class ContractTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/contract/contracts.html"


class AddContractView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/contract/addcontract.html"


class EditContractView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/contract/editcontract.html"


class ContractDetailTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/contract/detail.html"


class AddContractDetailTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/contract/adddetail.html"


class EditContractDetailTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/contract/editdetail.html"


class ContractFeaturesTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/contract/features.html"


class AddContractFeaturesTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/contract/add-features.html"


class EditContractFeaturesTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/contract/edit-features.html"


class ContractProgressesTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/contract/progresses.html"


class AddContractProgressesView(TemplateView):
    template_name = "admin/contract/add-progress.html"


class EditContractProgressesView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/contract/edit-progress.html"


class ContractCompleteTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/contract/works-completed.html"


# admin progess
"""=====================================
-------- Fiscal Year   --------
======================================"""


class FiscalYearView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/progress/fiscal-year.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["years"] = FiscalYear.objects.all().order_by("-id")
        context["title"] = "Fiscal Year"
        return context


class FiscalYearCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/progress/fiscalyear.html"
    # since it consists two fields
    form_class = FiscalYearForm
    success_url = reverse_lazy("company:fiscal-year")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Fiscal Year"
        return context


class FiscalYearUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/progress/edit-fiscalyear.html"
    form_class = FiscalYearForm
    model = FiscalYear
    success_url = reverse_lazy("company:fiscal-year")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Fiscal Year"
        return context


class FiscalYearDeleteView(DeleteSuccessMixin, DeleteView):
    template_name = "admin/delete.html"
    model = FiscalYear
    success_url = reverse_lazy("company:fiscal-year")


class FirstTrimestersView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/progress/first-trimesters.html"


class SecondTrimestersView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/progress/second-trimesters.html"


class ThirdTrimestersView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/progress/third-trimesters.html"


"""=====================================
-------- All trimester calcualtion  --------
======================================"""


class TrimestersView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/progress/trimesters.html"

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(**kwargs)
        if self.request.method == "GET":
            year_id = self.request.GET.get("yearId")
            if year_id is not None:
                yrs = FiscalYear.objects.get(id=year_id)
                context["yrs"] = yrs
                context["fiscal"] = FiscalYear.objects.all()

                # first trim
                try:
                    first_trim = FirstTrimester.objects.get(year=yrs)

                except FirstTrimester.DoesNotExist:
                    first_trim = None

                try:
                    second_trim = SecondTrimester.objects.get(year=yrs)

                except SecondTrimester.DoesNotExist:
                    second_trim = None

                try:
                    third_trim = ThirdTrimester.objects.get(year=yrs)

                except ThirdTrimester.DoesNotExist:
                    third_trim = None

            else:
                yrs = FiscalYear.objects.last()
                context["yrs"] = yrs
                context["fiscal"] = FiscalYear.objects.all()

                # first trim

                try:
                    first_trim = FirstTrimester.objects.get(year=yrs)
                    print("try", first_trim.month1_periodic_amount)

                except FirstTrimester.DoesNotExist:
                    print("catch")
                    first_trim = None

                try:
                    second_trim = SecondTrimester.objects.get(year=yrs)

                except SecondTrimester.DoesNotExist:
                    second_trim = None

                try:
                    third_trim = ThirdTrimester.objects.get(year=yrs)

                except ThirdTrimester.DoesNotExist:
                    third_trim = None
            context["first_trim"] = first_trim
            print("first tro", context["first_trim"])
            context["second_trim"] = second_trim
            context["third_trim"] = third_trim
            # calculate periodic percentage of first trimester
            print("first trim", first_trim)
            if first_trim is not None:
                if first_trim.trimester_cumulative and first_trim.periodic_target:
                    periodic_first_trim = periodic_percent(
                        first_trim.trimester_cumulative, first_trim.periodic_target
                    )
                    print("periodic_first_trim", periodic_first_trim)
                    context["periodic_first_trim"] = periodic_first_trim

            if second_trim:
                if second_trim.trimester_cumulative and second_trim.periodic_target:
                    periodic_second_trim = periodic_percent(
                        second_trim.trimester_cumulative, second_trim.periodic_target
                    )
                    print("periodic_second_trim", periodic_second_trim)
                    context["periodic_second_trim"] = periodic_second_trim

            if third_trim:
                if third_trim.trimester_cumulative and third_trim.periodic_target:
                    periodic_third_trim = periodic_percent(
                        third_trim.trimester_cumulative, third_trim.periodic_target
                    )
                    print("periodic_third_trim", periodic_third_trim)
                    context["periodic_third_trim"] = periodic_third_trim

            total = calculate_total(first_trim, second_trim, third_trim)
            context["total"] = total

            # pass yealry percentage
            if yrs:
                year_percentage_data = yearly_percentage_trimester(yrs)
                print("year_percentage_data***********", year_percentage_data)
                context["first_trim_yearly_percentage"] = year_percentage_data.get(
                    "first_trim_calc"
                )
                context["second_trim_yearly_percentage"] = year_percentage_data.get(
                    "second_trim_calc"
                )
                context["third_trim_yearly_percentage"] = year_percentage_data.get(
                    "third_trim_calc"
                )
                context["overall_yearly_percentage"] = year_percentage_data.get(
                    "overall_yearly_percentage"
                )
                print("first trim", context["first_trim_yearly_percentage"])
                # calculate the cumulative physical progress
                context[
                    "cumulative_physical_progress"
                ] = calc_cumulative_physical_progress(yrs)
                print(
                    "cumulative_physical_progress",
                    context["cumulative_physical_progress"],
                )

        return context


class TrimestersYearView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/progress/display_progress_after_update.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == "GET":
            # get the first trimester

            try:

                first_trim = FirstTrimester.objects.values("year").get(
                    id=self.kwargs["pk"]
                )
                year_id = first_trim.get("year")
            except FirstTrimester.DoesNotExist:
                pass

            if year_id is not None:
                yrs = FiscalYear.objects.get(id=year_id)
                context["yrs"] = yrs
                context["fiscal"] = FiscalYear.objects.all()

                # first trim
                try:
                    first_trim = FirstTrimester.objects.get(year=yrs)

                except FirstTrimester.DoesNotExist:
                    first_trim = None

                try:
                    second_trim = SecondTrimester.objects.get(year=yrs)

                except SecondTrimester.DoesNotExist:
                    second_trim = None

                try:
                    third_trim = ThirdTrimester.objects.get(year=yrs)

                except ThirdTrimester.DoesNotExist:
                    third_trim = None

            else:
                yrs = FiscalYear.objects.last()
                context["yrs"] = yrs
                context["fiscal"] = FiscalYear.objects.all()

                # first trim

                try:
                    first_trim = FirstTrimester.objects.get(year=yrs)
                    print("try", first_trim.month1_periodic_amount)

                except FirstTrimester.DoesNotExist:
                    print("catch")
                    first_trim = None

                try:
                    second_trim = SecondTrimester.objects.get(year=yrs)

                except SecondTrimester.DoesNotExist:
                    second_trim = None

                try:
                    third_trim = ThirdTrimester.objects.get(year=yrs)

                except ThirdTrimester.DoesNotExist:
                    third_trim = None
            context["first_trim"] = first_trim
            print("first tro", context["first_trim"])
            context["second_trim"] = second_trim
            context["third_trim"] = third_trim
            # calculate periodic percentage of first trimester
            print("first trim", first_trim)
            if first_trim is not None:
                if first_trim.trimester_cumulative and first_trim.periodic_target:
                    periodic_first_trim = periodic_percent(
                        first_trim.trimester_cumulative, first_trim.periodic_target
                    )
                    print("periodic_first_trim", periodic_first_trim)
                    context["periodic_first_trim"] = periodic_first_trim

            if second_trim:
                if second_trim.trimester_cumulative and second_trim.periodic_target:
                    periodic_second_trim = periodic_percent(
                        second_trim.trimester_cumulative, second_trim.periodic_target
                    )
                    print("periodic_second_trim", periodic_second_trim)
                    context["periodic_second_trim"] = periodic_second_trim

            if third_trim:
                if third_trim.trimester_cumulative and third_trim.periodic_target:
                    periodic_third_trim = periodic_percent(
                        third_trim.trimester_cumulative, third_trim.periodic_target
                    )
                    print("periodic_third_trim", periodic_third_trim)
                    context["periodic_third_trim"] = periodic_third_trim

            total = calculate_total(first_trim, second_trim, third_trim)
            context["total"] = total

            # pass yealry percentage
            if yrs:
                year_percentage_data = yearly_percentage_trimester(yrs)
                print("year_percentage_data", year_percentage_data)
                context["first_trim_yearly_percentage"] = year_percentage_data.get(
                    "first_trim_calc"
                )
                context["second_trim_yearly_percentage"] = year_percentage_data.get(
                    "second_trim_calc"
                )
                context["third_trim_yearly_percentage"] = year_percentage_data.get(
                    "third_trim_calc"
                )
                context["overall_yearly_percentage"] = year_percentage_data.get(
                    "overall_yearly_percentage"
                )
                print("first trim", context["first_trim_yearly_percentage"])
                context[
                    "cumulative_physical_progress"
                ] = calc_cumulative_physical_progress(yrs)
                print("cumulctive", context["cumulative_physical_progress"])

        return context


"""=====================================
-------- First trimester calcualtion  --------
======================================"""


class AddTrimestersView(AllUserRequiredMixin, FormView):
    """
    all trimester cumulative,triemsters calcualtion
    """

    template_name = "admin/progress/add-firsttrimester.html"
    success_url = reverse_lazy("company:trimesters")

    # pass all the form
    def get(self, request, *args, **kwargs):
        form = TrimesterForm()
        form.prefix = "form"
        context = {
            "form": form,
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = TrimesterForm(self.request.POST, prefix="form")
        if form.is_valid():
            if form.cleaned_data["month1"] == "1":
                f_month = form.save(commit=False)
                periodic_amt = form.cleaned_data["month1_periodic_amount"]
                month_name = form.cleaned_data["month1"]
                periodic_tar = form.cleaned_data["periodic_target"]
                trim_name = form.cleaned_data["trimester_name"]
                fiscal_year = None
                cumulative_amt = calc_cumulative(
                    periodic_amt, month_name, fiscal_year, obj_id=None
                )
                f_month.month1_cumulative_amount = cumulative_amt
                f_month.name = trim_name
                f_month.periodic_target = periodic_tar
                f_month.save()
                return super().form_valid(form)
            else:
                messages.error(
                    self.request, "Invalid Month", extra_tags="shrawan_month"
                )
                return self.form_invalid(form)
        else:
            print("form errors", form.errors)
            if form.errors:
                form_errors = "".join(map(str, form.errors["__all__"]))
            else:
                form_errors = None
            return render(
                request,
                "admin/progress/add-firsttrimester.html",
                context={"form": form, "form_errors": form_errors},
            )


class FirstTrimesterBhadraUpdateView(
    AllUserRequiredMixin, UpdateSuccessMixin, UpdateView
):
    """
    bhadra month
    """

    model = FirstTrimester
    form_class = BhadraFormView
    template_name = "admin/progress/add-firsttrimester.html"
    success_url = reverse_lazy("company:trimesters")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bhadra"] = "bhadra"
        return context

    def post(self, request, *args, **kwargs):
        form2 = BhadraFormView(self.request.POST)
        instance = self.get_object()
        if form2.is_valid():
            if (
                form2.cleaned_data["month2"] == "2"
            ):  # accepts only if the provided month is bhadra
                instance = self.get_object()
                obj = form2.save(commit=False)
                periodic_amt = form2.cleaned_data["month2_periodic_amount"]
                month_name = form2.cleaned_data["month2"]
                trim_name = form2.cleaned_data["name"]
                # print("trim_name", trim_name)
                obj_id = instance.pk
                fiscal_year = None
                cumulative_amt = calc_cumulative(
                    periodic_amt, month_name, fiscal_year, obj_id
                )
                obj = FirstTrimester.objects.get(id=obj_id)  # get the existing id
                obj.month2 = month_name
                obj.month2_periodic_amount = periodic_amt
                obj.month2_cumulative_amount = cumulative_amt
                obj.save()
                return super(FirstTrimesterBhadraUpdateView, self).post(
                    request, **kwargs
                )
            else:
                messages.error(self.request, "Invalid Month", extra_tags="bhadra")
                return super(FirstTrimesterBhadraUpdateView, self).get(
                    request, **kwargs
                )


class FirstTrimesterAshojUpdateView(
    UpdateSuccessMixin, AllUserRequiredMixin, UpdateView
):
    """
    ashoj month
    """

    model = FirstTrimester
    form_class = AshojFormView
    template_name = "admin/progress/add-firsttrimester.html"
    success_url = reverse_lazy("company:trimesters")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bhadra"] = "bhadra"
        context["ashoj"] = "ashoj"
        return context

    def post(self, request, *args, **kwargs):
        form2 = AshojFormView(self.request.POST)
        instance = self.get_object()
        if form2.is_valid():
            if (
                form2.cleaned_data["month3"] == "3"
            ):  # accepts only if the provided month is bhadra
                instance = self.get_object()
                obj = form2.save(commit=False)
                periodic_amt = form2.cleaned_data["month3_periodic_amount"]
                month_name = form2.cleaned_data["month3"]
                trim_name = form2.cleaned_data["name"]
                # print("trim_name", trim_name)
                obj_id = instance.pk
                fiscal_year = None
                cumulative_amt = calc_cumulative(
                    periodic_amt, month_name, fiscal_year, obj_id
                )
                obj = FirstTrimester.objects.get(id=obj_id)  # get the existing id
                obj.month3 = month_name
                obj.month3_periodic_amount = periodic_amt
                obj.month3_cumulative_amount = cumulative_amt
                obj.save()
                return super(FirstTrimesterAshojUpdateView, self).post(
                    request, **kwargs
                )
            else:
                messages.error(self.request, "Invalid Month", extra_tags="ashoj")
                return super(FirstTrimesterAshojUpdateView, self).get(request, **kwargs)


class FirstTrimesterKartikUpdateView(
    UpdateSuccessMixin, AllUserRequiredMixin, UpdateView
):
    """
    kartik month
    """

    model = FirstTrimester
    form_class = KartikFormView
    template_name = "admin/progress/add-firsttrimester.html"
    success_url = reverse_lazy("company:trimesters")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bhadra"] = "bhadra"
        context["ashoj"] = "ashoj"
        context["kartik"] = "kartik"
        return context

    def post(self, request, *args, **kwargs):
        print("th3######################################3333333333333")
        form2 = KartikFormView(self.request.POST)
        instance = self.get_object()
        if form2.is_valid():
            print("form is valid")
            if (
                form2.cleaned_data["month4"] == "4"
            ):  # accepts only if the provided month is bhadra
                print("this is kartik")
                instance = self.get_object()
                obj = form2.save(commit=False)
                periodic_amt = form2.cleaned_data["month4_periodic_amount"]
                month_name = form2.cleaned_data["month4"]
                print("periodic_amt", periodic_amt)
                print("month_name", month_name)

                obj_id = instance.pk
                fiscal_year = None
                cumulative_amt = calc_cumulative(
                    periodic_amt, month_name, fiscal_year, obj_id
                )

                obj = FirstTrimester.objects.get(id=obj_id)  # get the existing id

                # calculation of periodic target

                periodic_tar = (
                    obj.periodic_target
                )  # get the periodic target of first trimester
                # first_trim_periodic_per = periodic_percent(cumulative_amt, periodic_tar)
                print("periodic_tar", periodic_tar)
                obj.month4 = month_name
                obj.month4_periodic_amount = periodic_amt
                obj.month4_cumulative_amount = cumulative_amt
                obj.trimester_periodic = cumulative_amt
                obj.trimester_cumulative = cumulative_amt
                # obj.periodic_percentage_financial = first_trim_periodic_per

                obj.save()
                return super(FirstTrimesterKartikUpdateView, self).post(
                    request, **kwargs
                )
            else:
                print("else statment")
                messages.error(self.request, "Invalid Month", extra_tags="kartik")
                return super(FirstTrimesterKartikUpdateView, self).get(
                    request, **kwargs
                )


class FirstTrimesterUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    """ "
    updates physical progress,cumulative progress and overall
    """

    template_name = "admin/progress/firsttrimester_update.html"
    model = FirstTrimester
    form_class = FirstTrimCalcPeriodic
    success_url = reverse_lazy("company:trimesters-year")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print("instance", self.get_object())
        instance = self.get_object()
        if instance is not None:
            if instance.trimester_cumulative and instance.periodic_target:
                periodic_percent_first_trim = periodic_percent(
                    instance.trimester_cumulative, instance.periodic_target
                )
                print("periodic_first_trim", periodic_percent_first_trim)
                context["periodic_percent_first_trim"] = periodic_percent_first_trim
        context["title"] = "First Trimester"
        yrs = instance.year
        year_percentage_data = yearly_percentage_trimester(yrs)
        context["first_trim_yearly_percentage"] = year_percentage_data.get(
            "first_trim_calc"
        )
        return context

    def form_valid(self, form):
        form_data = form.save(commit=False)
        instance = self.get_object()
        data = firsttrim_data_update(form, instance)
        yrs = instance.year
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("company:firsttrimesters-year", kwargs={"pk": pk})


"""=====================================
-------- second trimester calcualtion  ---
======================================"""


class AddSecondMangsirTrimestersView(FormView, AllUserRequiredMixin, DetailView):
    """
    mangsir
    """

    model = FirstTrimester
    form_class = MangisrSecondTrimesterForm
    template_name = "admin/progress/add-secondtrimester.html"
    success_url = reverse_lazy("company:trimesters")

    # pass all the form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        first_trim_year = FirstTrimester.objects.get(id=self.kwargs["pk"])
        context["first_form_year"] = first_trim_year.year
        context["form"] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        select_year = request.POST.get("second-trim", None)
        if form.is_valid():
            if form.cleaned_data["month1"] == "5":
                f_month = form.save(commit=False)
                periodic_amt = form.cleaned_data["month1_periodic_amount"]
                month_name = form.cleaned_data["month1"]
                periodic_tar = form.cleaned_data["periodic_target"]
                trim_name = form.cleaned_data["trimester_name"]
                print("periodic amount", periodic_amt)
                print("periodic month_name", month_name)
                print("periodic_tar", periodic_tar)
                fiscal_year = FiscalYear.objects.get(year=str(select_year))
                print("fiscal_year@@@@@@@@@@@@2", fiscal_year)
                SecondTrimester.objects.create(
                    name=trim_name,
                    year=fiscal_year,
                    month1=month_name,
                    month1_periodic_amount=periodic_amt,
                    periodic_target=periodic_tar,
                    month1_cumulative_amount=periodic_amt,
                )

                return self.form_valid(form)
            else:
                messages.error(self.request, "Invalid Month", extra_tags="mangisr")
                return self.form_invalid(form)


class SecondTrimestersPoushUpdateView(
    UpdateSuccessMixin, AllUserRequiredMixin, UpdateView
):
    """
    poush month
    """

    model = SecondTrimester
    form_class = PoushFormView
    template_name = "admin/progress/add-secondtrimester.html"
    success_url = reverse_lazy("company:trimesters")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["poush"] = "poush"
        return context

    def post(self, request, *args, **kwargs):
        print("th3secon222222222222222222222")
        form2 = PoushFormView(self.request.POST)
        print("form2 errors", form2.errors)
        instance = self.get_object()
        if form2.is_valid():
            print("form is valid")
            if (
                form2.cleaned_data["month2"] == "6"
            ):  # accepts only if the provided month is bhadra
                print("this is bhdra")
                instance = self.get_object()
                obj = form2.save(commit=False)
                periodic_amt = form2.cleaned_data["month2_periodic_amount"]
                month_name = form2.cleaned_data["month2"]
                trim_name = form2.cleaned_data["name"]
                # print("trim_name", trim_name)
                obj_id = instance.pk
                fiscal_year = None
                cumulative_amt = calc_cumulative(
                    periodic_amt, month_name, fiscal_year, obj_id
                )
                obj = SecondTrimester.objects.get(id=obj_id)  # get the existing id
                obj.month2 = month_name
                obj.month2_periodic_amount = periodic_amt
                obj.month2_cumulative_amount = cumulative_amt
                obj.save()
                return super(SecondTrimestersPoushUpdateView, self).post(
                    request, **kwargs
                )
            else:
                print("else statment")
                messages.error(self.request, "Invalid Month", extra_tags="poush")
                return super(SecondTrimestersPoushUpdateView, self).get(
                    request, **kwargs
                )


class SecondTrimestersMaghUpdateView(
    UpdateSuccessMixin, AllUserRequiredMixin, UpdateView
):
    """
    Magh month
    """

    model = SecondTrimester
    form_class = MaghFormView
    template_name = "admin/progress/add-secondtrimester.html"
    success_url = reverse_lazy("company:trimesters")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["poush"] = "poush"
        context["magh"] = "magh"

        return context

    def post(self, request, *args, **kwargs):
        form2 = MaghFormView(self.request.POST)
        if form2.is_valid():
            print("form is valid")
            if (
                form2.cleaned_data["month3"] == "7"
            ):  # accepts only if the provided month is bhadra
                print("this is bhdra")
                instance = self.get_object()
                obj = form2.save(commit=False)
                periodic_amt = form2.cleaned_data["month3_periodic_amount"]
                month_name = form2.cleaned_data["month3"]
                # print("trim_name", trim_name)
                fiscal_year = None
                obj_id = instance.pk
                cumulative_amt = calc_cumulative(
                    periodic_amt, month_name, fiscal_year, obj_id
                )
                obj = SecondTrimester.objects.get(id=obj_id)  # get the existing id
                obj.month3 = month_name
                obj.month3_periodic_amount = periodic_amt
                obj.month3_cumulative_amount = cumulative_amt
                obj.save()
                return super(SecondTrimestersMaghUpdateView, self).post(
                    request, **kwargs
                )
            else:
                print("else statment")
                messages.error(self.request, "Invalid Month", extra_tags="magh")
                return super(SecondTrimestersMaghUpdateView, self).get(
                    request, **kwargs
                )


class SecondTrimestersFalgunUpdateView(
    UpdateSuccessMixin, AllUserRequiredMixin, UpdateView
):
    """
    Falgun month
    """

    model = SecondTrimester
    form_class = FalgunFormView
    template_name = "admin/progress/add-secondtrimester.html"
    success_url = reverse_lazy("company:trimesters")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["poush"] = "poush"
        context["magh"] = "magh"
        context["falgun"] = "falgun"
        return context

    def post(self, request, *args, **kwargs):
        form2 = FalgunFormView(self.request.POST)
        if form2.is_valid():
            print("form is valid")
            if (
                form2.cleaned_data["month4"] == "8"
            ):  # accepts only if the provided month is bhadra
                print("this is falgun")
                instance = self.get_object()
                obj = form2.save(commit=False)
                periodic_amt = form2.cleaned_data["month4_periodic_amount"]
                month_name = form2.cleaned_data["month4"]
                print("periodic_amt", periodic_amt)
                print("month_name", month_name)

                obj_id = instance.pk
                fiscal_year = None
                cumulative_amt = calc_cumulative(
                    periodic_amt, month_name, fiscal_year, obj_id
                )

                obj = SecondTrimester.objects.get(id=obj_id)  # get the existing id

                # calculation of periodic target

                periodic_tar = (
                    obj.periodic_target
                )  # get the periodic target of first trimester

                first_trim_periodic_per = periodic_percent(cumulative_amt, periodic_tar)
                print("periodic_tar", periodic_tar)
                obj.month4 = month_name
                obj.month4_periodic_amount = periodic_amt
                obj.month4_cumulative_amount = cumulative_amt
                obj.periodic_percentage_financial = first_trim_periodic_per
                obj.trimester_periodic = cumulative_amt
                obj.trimester_cumulative = cumulative_amt
                obj.save()
                return super(SecondTrimestersFalgunUpdateView, self).post(
                    request, **kwargs
                )
            else:
                messages.error(self.request, "Invalid Month", extra_tags="falgun")
                return super(SecondTrimestersFalgunUpdateView, self).get(
                    request, **kwargs
                )

    # def post(self, request, *args, **kwargs):
    #     # second-trim
    #     print("this is post method")
    #     form1 = SecondTrimesterForm(self.request.POST, prefix="form")
    #     print(self.request.POST, "##################")
    #     print(form1.errors, "@@##################")
    #     if form1.is_valid():
    #         f_month = form1.save(commit=False)
    #         periodic_amt = form1.cleaned_data["month1_periodic_amount"]
    #         month_name = form1.cleaned_data["month1"]
    #         periodic_tar = form1.cleaned_data["periodic_target"]
    #         trim_name = form1.cleaned_data["trimester_name"]

    #         print("periodic amount", periodic_amt)
    #         print("periodic month_name", month_name)
    #         print("periodic_tar", periodic_tar)

    #         cumulative_amt = calc_cumulative(periodic_amt, month_name, obj_id=None)
    #         f_month.month1_cumulative_amount = cumulative_amt
    #         f_month.name = trim_name
    #         f_month.save()
    #         return super().form_valid(form1)


class SecondTrimesterUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    """ "
    updates physical progress,cumulative progress and overall
    """

    template_name = "admin/progress/second_trimester_update.html"
    model = SecondTrimester
    form_class = SecondTrimCalcPeriodic
    success_url = reverse_lazy("company:trimesters")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Second Trimester"
        instance = self.get_object()
        if instance is not None:
            if instance.trimester_cumulative and instance.periodic_target:
                periodic_percent_second_trim = periodic_percent(
                    instance.trimester_cumulative, instance.periodic_target
                )
                print("periodic_first_trim", periodic_percent_second_trim)
                context["periodic_percent_second_trim"] = periodic_percent_second_trim
        context["title"] = "First Trimester"
        yrs = instance.year
        if yrs:
            year_percentage_data = yearly_percentage_trimester(yrs)
            context["second_trim_yearly_percentage"] = year_percentage_data.get(
                "second_trim_calc"
            )
        return context

    def form_valid(self, form):
        form_data = form.save(commit=False)
        instance = self.get_object()
        data = secondtrim_data_update(form, instance)
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("company:secondtrimesters-year", kwargs={"pk": pk})


class SecondTrimesterYearView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/progress/display_progress_after_update.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == "GET":
            # get the first trimester

            try:
                second_trim = SecondTrimester.objects.values("year").get(
                    id=self.kwargs["pk"]
                )
                year_id = second_trim.get("year")
            except SecondTrimester.DoesNotExist:
                pass

            if year_id is not None:
                yrs = FiscalYear.objects.get(id=year_id)
                context["yrs"] = yrs
                context["fiscal"] = FiscalYear.objects.all()

                # first trim
                try:
                    first_trim = FirstTrimester.objects.get(year=yrs)

                except FirstTrimester.DoesNotExist:
                    first_trim = None

                try:
                    second_trim = SecondTrimester.objects.get(year=yrs)

                except SecondTrimester.DoesNotExist:
                    second_trim = None

                try:
                    third_trim = ThirdTrimester.objects.get(year=yrs)

                except ThirdTrimester.DoesNotExist:
                    third_trim = None

            else:
                yrs = FiscalYear.objects.last()
                context["yrs"] = yrs
                context["fiscal"] = FiscalYear.objects.all()

                # first trim

                try:
                    first_trim = FirstTrimester.objects.get(year=yrs)
                    print("try", first_trim.month1_periodic_amount)

                except FirstTrimester.DoesNotExist:
                    print("catch")
                    first_trim = None

                try:
                    second_trim = SecondTrimester.objects.get(year=yrs)

                except SecondTrimester.DoesNotExist:
                    second_trim = None

                try:
                    third_trim = ThirdTrimester.objects.get(year=yrs)

                except ThirdTrimester.DoesNotExist:
                    third_trim = None
            context["first_trim"] = first_trim
            print("first tro", context["first_trim"])
            context["second_trim"] = second_trim
            context["third_trim"] = third_trim
            # calculate periodic percentage of first trimester
            print("first trim", first_trim)
            if first_trim is not None:
                if first_trim.trimester_cumulative and first_trim.periodic_target:
                    periodic_first_trim = periodic_percent(
                        first_trim.trimester_cumulative, first_trim.periodic_target
                    )
                    print("periodic_first_trim", periodic_first_trim)
                    context["periodic_first_trim"] = periodic_first_trim

            if second_trim:
                if second_trim.trimester_cumulative and second_trim.periodic_target:
                    periodic_second_trim = periodic_percent(
                        second_trim.trimester_cumulative, second_trim.periodic_target
                    )
                    print("periodic_second_trim", periodic_second_trim)
                    context["periodic_second_trim"] = periodic_second_trim

            if third_trim:
                if third_trim.trimester_cumulative and third_trim.periodic_target:
                    periodic_third_trim = periodic_percent(
                        third_trim.trimester_cumulative, third_trim.periodic_target
                    )
                    print("periodic_third_trim", periodic_third_trim)
                    context["periodic_third_trim"] = periodic_third_trim

            total = calculate_total(first_trim, second_trim, third_trim)
            context["total"] = total

            # pass yealry percentage
            if yrs:
                year_percentage_data = yearly_percentage_trimester(yrs)
                print("year_percentage_data", year_percentage_data)
                context["first_trim_yearly_percentage"] = year_percentage_data.get(
                    "first_trim_calc"
                )
                context["second_trim_yearly_percentage"] = year_percentage_data.get(
                    "second_trim_calc"
                )
                context["third_trim_yearly_percentage"] = year_percentage_data.get(
                    "third_trim_calc"
                )
                context["overall_yearly_percentage"] = year_percentage_data.get(
                    "overall_yearly_percentage"
                )
                print("first trim", context["first_trim_yearly_percentage"])
                context[
                    "cumulative_physical_progress"
                ] = calc_cumulative_physical_progress(yrs)
                print("cumulctive", context["cumulative_physical_progress"])

        return context


"""=====================================
-------- Third trimester calcualtion  ---
======================================"""


class AddThirdChaitraTrimestersView(FormView, AllUserRequiredMixin, DetailView):
    """
    mangsir
    """

    model = SecondTrimester
    form_class = ChaitraThirdTrimesterForm
    template_name = "admin/progress/add-thirdtrimester.html"
    success_url = reverse_lazy("company:trimesters")

    # pass all the form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        second_trim_year = SecondTrimester.objects.get(id=self.kwargs["pk"])
        context["first_form_year"] = second_trim_year.year
        context["form"] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        select_year = request.POST.get("third-trim", None)
        if form.is_valid():
            if form.cleaned_data["month1"] == "9":
                f_month = form.save(commit=False)
                periodic_amt = form.cleaned_data["month1_periodic_amount"]
                month_name = form.cleaned_data["month1"]
                periodic_tar = form.cleaned_data["periodic_target"]
                trim_name = form.cleaned_data["trimester_name"]
                print("periodic amount", periodic_amt)
                print("periodic month_name", month_name)
                print("periodic_tar", periodic_tar)
                fiscal_year = FiscalYear.objects.get(year=str(select_year))
                print("fiscal_year@@@@@@@@@@@@2", fiscal_year)
                ThirdTrimester.objects.create(
                    name=trim_name,
                    year=fiscal_year,
                    month1=month_name,
                    month1_periodic_amount=periodic_amt,
                    periodic_target=periodic_tar,
                    month1_cumulative_amount=periodic_amt,
                )

                return self.form_valid(form)
            else:
                messages.error(self.request, "Invalid Month", extra_tags="chaitra")
                return self.form_invalid(form)


class ThirdTrimestersBaisakhUpdateView(
    UpdateSuccessMixin, AllUserRequiredMixin, UpdateView
):
    """
    baisakh
    """

    model = ThirdTrimester
    form_class = BaisakhFormView
    template_name = "admin/progress/add-thirdtrimester.html"
    success_url = reverse_lazy("company:trimesters")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["baisakh"] = "baisakh"
        return context

    def post(self, request, *args, **kwargs):
        print("th3secon222222222222222222222")
        form2 = BaisakhFormView(self.request.POST)
        print("form2 errors", form2.errors)
        instance = self.get_object()
        if form2.is_valid():
            print("form is valid")
            if (
                form2.cleaned_data["month2"] == "10"
            ):  # accepts only if the provided month is bhadra
                print("this is bhdra")
                instance = self.get_object()
                obj = form2.save(commit=False)
                periodic_amt = form2.cleaned_data["month2_periodic_amount"]
                month_name = form2.cleaned_data["month2"]
                trim_name = form2.cleaned_data["name"]
                # print("trim_name", trim_name)
                obj_id = instance.pk
                fiscal_year = None
                cumulative_amt = calc_cumulative(
                    periodic_amt, month_name, fiscal_year, obj_id
                )
                obj = ThirdTrimester.objects.get(id=obj_id)  # get the existing id
                obj.month2 = month_name
                obj.month2_periodic_amount = periodic_amt
                obj.month2_cumulative_amount = cumulative_amt
                obj.save()
                return super(ThirdTrimestersBaisakhUpdateView, self).post(
                    request, **kwargs
                )
            else:
                print("else statment")
                messages.error(self.request, "Invalid Month", extra_tags="baisakh")
                return super(ThirdTrimestersBaisakhUpdateView, self).get(
                    request, **kwargs
                )


class ThirdTrimestersJesthaUpdateView(
    UpdateSuccessMixin, AllUserRequiredMixin, UpdateView
):
    """
    jestha
    """

    model = ThirdTrimester
    form_class = JesthaFormView
    template_name = "admin/progress/add-thirdtrimester.html"
    success_url = reverse_lazy("company:trimesters")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["baisakh"] = "baisakh"
        context["jestha"] = "jestha"
        return context

    def post(self, request, *args, **kwargs):
        print("th3secon222222222222222222222")
        form2 = JesthaFormView(self.request.POST)
        print("form2 errors", form2.errors)
        instance = self.get_object()
        if form2.is_valid():
            if (
                form2.cleaned_data["month3"] == "11"
            ):  # accepts only if the provided month is bhadra
                print("this is bhdra")
                instance = self.get_object()
                obj = form2.save(commit=False)
                periodic_amt = form2.cleaned_data["month3_periodic_amount"]
                month_name = form2.cleaned_data["month3"]
                obj_id = instance.pk
                fiscal_year = None
                cumulative_amt = calc_cumulative(
                    periodic_amt, month_name, fiscal_year, obj_id
                )
                obj = ThirdTrimester.objects.get(id=obj_id)  # get the existing id
                obj.month3 = month_name
                obj.month3_periodic_amount = periodic_amt
                obj.month3_cumulative_amount = cumulative_amt
                obj.save()
                return super(ThirdTrimestersJesthaUpdateView, self).post(
                    request, **kwargs
                )
            else:
                print("else statment")
                messages.error(self.request, "Invalid Month", extra_tags="jestha")
                return super(ThirdTrimestersJesthaUpdateView, self).get(
                    request, **kwargs
                )


class ThirdTrimestersAsarUpdateView(
    UpdateSuccessMixin, AllUserRequiredMixin, UpdateView
):
    """
    asar month
    """

    model = ThirdTrimester
    form_class = AsarFormView
    template_name = "admin/progress/add-thirdtrimester.html"
    success_url = reverse_lazy("company:trimesters")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["baisakh"] = "baisakh"
        context["jestha"] = "jestha"
        context["asar"] = "asar"
        return context

    def post(self, request, *args, **kwargs):
        form2 = AsarFormView(self.request.POST)
        if form2.is_valid():
            print("form is valid")
            if (
                form2.cleaned_data["month4"] == "12"
            ):  # accepts only if the provided month is bhadra
                print("this is falgun")
                instance = self.get_object()
                obj = form2.save(commit=False)
                periodic_amt = form2.cleaned_data["month4_periodic_amount"]
                month_name = form2.cleaned_data["month4"]
                print("periodic_amt", periodic_amt)
                print("month_name", month_name)

                obj_id = instance.pk
                fiscal_year = None
                cumulative_amt = calc_cumulative(
                    periodic_amt, month_name, fiscal_year, obj_id
                )

                obj = ThirdTrimester.objects.get(id=obj_id)  # get the existing id

                # calculation of periodic target
                periodic_tar = (
                    obj.periodic_target
                )  # get the periodic target of first trimester
                third_trim_periodic_per = periodic_percent(cumulative_amt, periodic_tar)
                print("periodic_tar", periodic_tar)

                obj.month4 = month_name
                obj.month4_periodic_amount = periodic_amt
                obj.month4_cumulative_amount = cumulative_amt
                obj.periodic_percentage_financial = third_trim_periodic_per
                obj.trimester_periodic = cumulative_amt
                obj.trimester_cumulative = cumulative_amt
                obj.save()

                # calcualtion of yearly percentage (physical progress)
                final_year = obj.year
                print(final_year, "*************************")

                yealry_per = yearly_percentage(final_year)
                return super().post(request, **kwargs)
            else:
                messages.error(self.request, "Invalid Month", extra_tags="asar")
                return super().get(request, **kwargs)


class ThirdTrimesterUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    """ "
    updates physical progress,cumulative progress and overall
    """

    template_name = "admin/progress/third_trimester_update.html"
    model = ThirdTrimester
    form_class = ThirdTrimCalcPeriodic
    success_url = reverse_lazy("company:trimesters")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Third Trimester"
        instance = self.get_object()
        if instance is not None:
            if instance.trimester_cumulative and instance.periodic_target:
                periodic_percent_second_trim = periodic_percent(
                    instance.trimester_cumulative, instance.periodic_target
                )
                print("periodic_first_trim", periodic_percent_second_trim)
                context["periodic_percent_second_trim"] = periodic_percent_second_trim
        context["title"] = "First Trimester"
        yrs = instance.year
        if yrs:
            year_percentage_data = yearly_percentage_trimester(yrs)
            context["third_trim_yearly_percentage"] = year_percentage_data.get(
                "third_trim_calc"
            )
            print("third", context["third_trim_yearly_percentage"])
        return context

    def form_valid(self, form):
        form_data = form.save(commit=False)
        instance = self.get_object()
        data = thirdtrim_data_update(form, instance)
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("company:thirdtrimesters-year", kwargs={"pk": pk})


class ThirdTrimesterYearView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/progress/display_progress_after_update.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == "GET":
            # get the first trimester

            try:

                third_trim = ThirdTrimester.objects.values("year").get(
                    id=self.kwargs["pk"]
                )
                year_id = third_trim.get("year")
            except ThirdTrimester.DoesNotExist:
                pass

            if year_id is not None:
                yrs = FiscalYear.objects.get(id=year_id)
                context["yrs"] = yrs
                context["fiscal"] = FiscalYear.objects.all()

                # first trim
                try:
                    first_trim = FirstTrimester.objects.get(year=yrs)

                except FirstTrimester.DoesNotExist:
                    first_trim = None

                try:
                    second_trim = SecondTrimester.objects.get(year=yrs)

                except SecondTrimester.DoesNotExist:
                    second_trim = None

                try:
                    third_trim = ThirdTrimester.objects.get(year=yrs)

                except ThirdTrimester.DoesNotExist:
                    third_trim = None

            else:
                yrs = FiscalYear.objects.last()
                context["yrs"] = yrs
                context["fiscal"] = FiscalYear.objects.all()

                # first trim

                try:
                    first_trim = FirstTrimester.objects.get(year=yrs)
                    print("try", first_trim.month1_periodic_amount)

                except FirstTrimester.DoesNotExist:
                    print("catch")
                    first_trim = None

                try:
                    second_trim = SecondTrimester.objects.get(year=yrs)

                except SecondTrimester.DoesNotExist:
                    second_trim = None

                try:
                    third_trim = ThirdTrimester.objects.get(year=yrs)

                except ThirdTrimester.DoesNotExist:
                    third_trim = None
            context["first_trim"] = first_trim
            print("first tro", context["first_trim"])
            context["second_trim"] = second_trim
            context["third_trim"] = third_trim
            # calculate periodic percentage of first trimester
            print("first trim", first_trim)
            if first_trim is not None:
                if first_trim.trimester_cumulative and first_trim.periodic_target:
                    periodic_first_trim = periodic_percent(
                        first_trim.trimester_cumulative, first_trim.periodic_target
                    )
                    print("periodic_first_trim", periodic_first_trim)
                    context["periodic_first_trim"] = periodic_first_trim

            if second_trim:
                if second_trim.trimester_cumulative and second_trim.periodic_target:
                    periodic_second_trim = periodic_percent(
                        second_trim.trimester_cumulative, second_trim.periodic_target
                    )
                    print("periodic_second_trim", periodic_second_trim)
                    context["periodic_second_trim"] = periodic_second_trim

            if third_trim:
                if third_trim.trimester_cumulative and third_trim.periodic_target:
                    periodic_third_trim = periodic_percent(
                        third_trim.trimester_cumulative, third_trim.periodic_target
                    )
                    print("periodic_third_trim", periodic_third_trim)
                    context["periodic_third_trim"] = periodic_third_trim

            total = calculate_total(first_trim, second_trim, third_trim)
            context["total"] = total

            # pass yealry percentage
            if yrs:
                year_percentage_data = yearly_percentage_trimester(yrs)
                print("year_percentage_data", year_percentage_data)
                context["first_trim_yearly_percentage"] = year_percentage_data.get(
                    "first_trim_calc"
                )
                context["second_trim_yearly_percentage"] = year_percentage_data.get(
                    "second_trim_calc"
                )
                context["third_trim_yearly_percentage"] = year_percentage_data.get(
                    "third_trim_calc"
                )
                context["overall_yearly_percentage"] = year_percentage_data.get(
                    "overall_yearly_percentage"
                )
                print("first trim", context["first_trim_yearly_percentage"])
                context[
                    "cumulative_physical_progress"
                ] = calc_cumulative_physical_progress(yrs)
                print("cumulctive", context["cumulative_physical_progress"])

        return context


#
# admin darta chalani


class DartaTableView(AllUserRequiredAndAdminstration, TemplateView):
    template_name = "admin/administration/darta.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["darta"] = Darta.objects.all().order_by("-id")
        print("darta", context["darta"])
        return context


class ChalaniTableView(AllUserRequiredAndAdminstration, ListView):
    template_name = "admin/administration/chalani.html"
    model = Chalani
    context_object_name = "chalani"


# employee
"""=====================================
-------- employee section---
======================================"""


class EmployeeTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/employee/employee-table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employee"
        context["employees"] = EmployeeProfile.objects.filter(
            is_transferred=False, is_projecthead=False
        ).order_by("-id")
        return context


#
# class AddEmployeeView(AddSuccessMixin, CreateView):
#     print("lslslslsl")
#     template_name = "admin/employee/add-employee.html"
#     form_class = EmployeeForm
#     success_url = reverse_lazy("company:employee-list")

#     def form_valid(self, form):
#         print("hshhs",form.errors)
#         form_new = form.save(commit=False)
#         print("form_new",form_new.errors)

#         form_new.save()
#         return super().form_valid(form)


class AddEmployeeView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/employee/add-employee.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("company:employee-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employee"
        return context


class EmployeeDeleteView(AllUserRequiredMixin, DeleteSuccessMixin, DeleteView):
    template_name = "admin/delete.html"
    model = EmployeeProfile
    success_url = reverse_lazy("company:employee-list")


class EditEmployeeView(AllUserRequiredMixin, UpdateSuccessMixin, UpdateView):
    template_name = "admin/employee/edit-employee.html"
    model = EmployeeProfile
    form_class = EmployeeForm
    success_url = reverse_lazy("company:employee-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Employee"
        return context


"""=====================================
-------- ex employee section---
======================================"""


class ExEmployeeTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/employee/exemp-table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ex_employees"
        context["ex_employees"] = EmployeeProfile.objects.filter(
            is_transferred=True
        ).order_by("-id")
        return context


class AddExEmployeeView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/employee/addexemployee.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("company:ex-employee-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ex_employees"
        return context

    def form_valid(self, form):
        get_field = self.request.POST
        form_new = form.save(commit=False)
        form_new.is_transferred = True
        form_new.save()
        return super().form_valid(form)


class EditExEmployeeTableView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/employee/edit-exemp.html"
    model = EmployeeProfile
    form_class = EmployeeForm
    success_url = reverse_lazy("company:ex-employee-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ex_employees"
        return context

    def form_valid(self, form):
        form_new = form.save(commit=False)
        form_new.is_transferred = True
        form_new.save()
        return super().form_valid(form)


class ExEmployeeDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = EmployeeProfile
    success_url = reverse_lazy("company:ex-employee-list")


"""=====================================
-------- ex project head section---
======================================"""


class ExProjectHeadTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/employee/exproject-table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Ex-Project"
        context["ex_projecthead"] = EmployeeProfile.objects.filter(
            is_projecthead=True
        ).order_by("-id")
        return context


class AddExProjectHeadView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/employee/addexproject.html"
    form_class = EmployeeForm
    success_url = reverse_lazy("company:ex-project-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Ex-Project"
        return context

    def form_valid(self, form):
        form_new = form.save(commit=False)
        form_new.is_projecthead = True
        form_new.save()
        return super().form_valid(form)


class EditExProjectHeadTableView(UpdateSuccessMixin, UpdateView):
    template_name = "admin/employee/edit-ex-project.html"
    model = EmployeeProfile
    form_class = EmployeeForm
    success_url = reverse_lazy("company:ex-project-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Ex-Project"
        return context

    def form_valid(self, form):
        form_new = form.save(commit=False)
        form_new.is_projecthead = True
        form_new.save()
        return super().form_valid(form)


class ExprojectHeadDeleteView(DeleteSuccessMixin, DeleteView):
    template_name = "admin/delete.html"
    model = EmployeeProfile
    success_url = reverse_lazy("company:ex-project-list")


"""============================================
-------- adminstration section file upload -----
=============================================="""


class AdministrationFileUploadView(AllUserRequiredAndAdminstration, TemplateView):
    template_name = "admin/administration/upload-file.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "administration_file_upload"
        context["files"] = AdminstrationUploadFile.objects.all().order_by("-id")
        print("files", context["files"])
        return context


class AdministrationFileUploadCreateView(
    AddSuccessMixin, AllUserRequiredAndAdminstration, CreateView
):
    template_name = "admin/create.html"
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
                return redirect(reverse("company:administration-file"))


class AdministrationFileUploadUpdateView(
    UpdateSuccessMixin, AllUserRequiredAndAdminstration, UpdateView
):
    template_name = "admin/update.html"
    model = AdminstrationUploadFile
    fields = [
        "fiscal_year",
        "title",
        "files",
    ]
    success_url = reverse_lazy("company:administration-file")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "administration-file"
        return context


class AdministrationFileUploadDeleteView(
    DeleteSuccessMixin, AllUserRequiredAndAdminstration, DeleteView
):
    template_name = "admin/delete.html"
    model = AdminstrationUploadFile
    success_url = reverse_lazy("company:administration-file")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "administration-file"
        return context


"""============================================
-------- account section file upload -----
=============================================="""
# accountant
class FileBudgetView(AllUserRequiredAndAccounant, TemplateView):
    template_name = "admin/accountant/file-budget.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "file_budget"
        context["files"] = AccountUploadFile.objects.all().order_by("-id")
        return context


class FileBudgetCreateView(AddSuccessMixin, AllUserRequiredAndAccounant, CreateView):
    template_name = "admin/create.html"
    form_class = AccountUploadFileForm
    success_url = reverse_lazy("company:file-budget")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Budget File"
        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            fiscal_year = form.cleaned_data["fiscal_year"]
            title = form.cleaned_data["title"]
            files = request.FILES.getlist("files")
            types = form.cleaned_data["types"]
            print("types", types)
            if files:
                bulk_file_upload = []
                for element in files:
                    upload_file = AccountUploadFile(
                        fiscal_year=fiscal_year,
                        title=title,
                        files=element,
                        types=types,
                    )
                    bulk_file_upload.append(upload_file)
                AccountUploadFile.objects.bulk_create(bulk_file_upload)
                # doc = Documents.objects.create(
                #     category=category, name=name, file=element
                # )
                return redirect(reverse("company:file-budget"))


class FileBudgetUpdateView(UpdateSuccessMixin, AllUserRequiredAndAccounant, UpdateView):
    template_name = "admin/update.html"
    model = AccountUploadFile
    fields = ["fiscal_year", "title", "files", "types"]
    success_url = reverse_lazy("company:file-budget")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Budget File"
        return context


class FileBudgetDeleteView(DeleteSuccessMixin, AllUserRequiredAndAccounant, DeleteView):
    template_name = "admin/delete.html"
    model = AccountUploadFile
    success_url = reverse_lazy("company:file-budget")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Budget File"
        return context


"""============================================
--------------- current budget -----------------
=============================================="""


class CurrentBudgetView(AllUserRequiredAndAccounant, TemplateView):
    template_name = "admin/accountant/current-budget.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "current_budget"
        context["current_budget"] = CurrentBudget.objects.all().order_by("-id")
        return context


class CurrentBudgetCreateView(AddSuccessMixin, AllUserRequiredAndAccounant, CreateView):
    template_name = "admin/create.html"
    model = CurrentBudget
    fields = ["fiscal_year", "annual_budget", "expenditure", "remaining"]
    success_url = reverse_lazy("company:current-budget")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Current Budget"
        return context


class CurrentBudgetUpdateView(
    UpdateSuccessMixin, AllUserRequiredAndAccounant, UpdateView
):
    template_name = "admin/update.html"
    model = CurrentBudget
    fields = ["fiscal_year", "annual_budget", "expenditure", "remaining"]
    success_url = reverse_lazy("company:current-budget")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Current Budget"
        return context


class CurrentBudgetDeleteView(
    DeleteSuccessMixin, AllUserRequiredAndAccounant, DeleteView
):
    template_name = "admin/delete.html"
    model = CurrentBudget
    success_url = reverse_lazy("company:current-budget")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Current Budget"
        return context


"""============================================
--------------- capital budget -----------------
=============================================="""


class CapitalBudgetView(AllUserRequiredAndAccounant, TemplateView):
    template_name = "admin/accountant/capital-budget.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "capital_budget"
        context["capital_budget"] = CapitalBudget.objects.all().order_by("-id")
        return context


class CapitalBudgetCreateView(AddSuccessMixin, AllUserRequiredAndAccounant, CreateView):
    template_name = "admin/create.html"
    model = CapitalBudget
    fields = ["fiscal_year", "annual_budget", "expenditure", "remaining"]
    success_url = reverse_lazy("company:current-budget")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "capital-budget"
        return context


class CapitalBudgetUpdateView(
    UpdateSuccessMixin, AllUserRequiredAndAccounant, UpdateView
):
    template_name = "admin/update.html"
    model = CapitalBudget
    fields = ["fiscal_year", "annual_budget", "expenditure", "remaining"]
    success_url = reverse_lazy("company:current-budget")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Capital Budget"
        return context


class CapitalBudgetDeleteView(
    DeleteSuccessMixin, AllUserRequiredAndAccounant, DeleteView
):
    template_name = "admin/delete.html"
    model = CapitalBudget
    success_url = reverse_lazy("company:current-budget")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Capital Budget"
        return context


# live data
class AwsView(TemplateView):
    template_name = "live-data/aws.html"

# main dam
class InstrumentationView(TemplateView):
    template_name = "live-data/instrumentation.html"

class sdOneView(TemplateView):
    template_name = "live-data/sd-1.html"

class sdTwoView(TemplateView):
    template_name = "live-data/sd-2.html"

class sdThreeView(TemplateView):
    template_name = "live-data/sd-3.html"

class HydroView(TemplateView):
    template_name = "live-data/hydro.html"


class ComingSooonView(TemplateView):
    template_name = "coming-soon.html"
