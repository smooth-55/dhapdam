from django.shortcuts import render
from company.views import AddSuccessMixin, UpdateSuccessMixin, DeleteSuccessMixin

# Create your views here.
# dhapdam view____________==+++++++==============
# class DhapIntroView (TemplateView):
#     template_name = "admin/dhapdam/intro.html"

# class DhapFeaturesView(TemplateView):
#     template_name = "admin/dhapdam/feature.html"
# # add featute
# class DhapAddFeatures(TemplateView):
#     template_name= "admin/dhapdam/add-features.html"
# #edit feature
# class DhapEditFeatures(TemplateView):
#     template_name= "admin/dhapdam/edit-features.html"
from django.views.generic import (
    TemplateView,
    CreateView,
    FormView,
    DeleteView,
    UpdateView,
)
from .forms import *
from users.decorators import (
    AllUserRequiredMixin,
    AccountantRequiredMixin,
    AdminstrationRequiredMixin,
    AllUserRequiredAndAdminstration,
    AllUserRequiredAndAccounant,
)
from django.urls import reverse_lazy
from .models import *

"""===================================
----- dhapdam introduction  starts  ---
======================================"""


class DhapIntroView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/dhapdam/intro.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["intro"] = IntroductionOfDam.objects.get(
                introduction__project_name="dhapdam"
            )
            print("context", context["intro"])
        except:
            context["intro"] = None
        return context


class AddDhapIntroCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/dhapdam/dhapdam-intro-create.html"
    form_class = IntroductionOfDamForm
    success_url = reverse_lazy("dam:dadmin-intro")

    def form_valid(self, form):
        form_new = form.save(commit=False)
        try:
            intro, created = DamIntroduction.objects.get_or_create(
                project_name="dhapdam"
            )
            print("intro", intro)
            form_new.introduction = intro
            return super().form_valid(form)
        except DamIntroduction.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, "Please enter the introduction form"
            )
            return render(
                request,
                template_name=self.template_name,
                context=self.get_context_data(),
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DhapIntroUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/dhapdam/dhapdam-intro-update.html"
    form_class = IntroductionOfDamForm
    model = IntroductionOfDam
    success_url = reverse_lazy("dam:dadmin-intro")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DhapIntroDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = IntroductionOfDam
    success_url = reverse_lazy("dam:dadmin-intro")


"""===================================
----- salient features starts  ---
======================================"""


class DhapFeaturesView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/dhapdam/feature.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["features"] = SalientFeatures.objects.get(
                introduction__project_name="dhapdam"
            )
            print("features", context["features"])
        except:
            context["features"] = None
        return context


# add featute
class DhapAddFeatures(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/dhapdam/add-features.html"
    form_class = SalientFeaturesForm
    success_url = reverse_lazy("dam:dadmin-features")

    def form_valid(self, form):
        form_new = form.save(commit=False)
        try:
            intro, created = DamIntroduction.objects.get_or_create(
                project_name="dhapdam"
            )
            print("intro", intro)
            form_new.introduction = intro
            return super().form_valid(form)
        except DamIntroduction.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, "Please enter the introduction form"
            )
            return render(
                request,
                template_name=self.template_name,
                context=self.get_context_data(),
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "dhap-add"
        return context


# edit feature
class DhapEditFeatures(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/dhapdam/edit-features.html"
    model = SalientFeatures
    form_class = SalientFeaturesForm
    success_url = reverse_lazy("dam:dadmin-features")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "dhap-add"
        return context


"""===================================
----- dhap location starts  ---
======================================"""


class DhapLocationView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/dhapdam/location-and-accessibility/location.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["locations"] = LocationAndAccessibility.objects.get(
                introduction__project_name="dhapdam"
            )
            print("locations", context["locations"])
        except:
            context["locations"] = None
        return context


class DhapLocationCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/dhapdam/location-and-accessibility/locationadd.html"

    # template_name = "admin/dhapdam/location-and-accessibility/location-and-accessibility-add.html"
    form_class = LocationAndAccessibilityForm
    success_url = reverse_lazy("dam:dadmin-location")

    def form_valid(self, form):
        form_new = form.save(commit=False)
        try:
            intro, created = DamIntroduction.objects.get_or_create(
                project_name="dhapdam"
            )
            print("intro", intro)
            form_new.introduction = intro
            form_new.save()
            return super().form_valid(form)
        except DamIntroduction.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, "Please enter the introduction form"
            )
            return render(
                request,
                template_name=self.template_name,
                context=self.get_context_data(),
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Location"
        return context


class DhapLocationUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/dhapdam/location-and-accessibility/locationupdate.html"
    form_class = LocationAndAccessibilityForm
    model = LocationAndAccessibility
    success_url = reverse_lazy("dam:dadmin-location")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Location"
        return context


"""===================================
----- dhap main work components starts  ---
======================================"""


class DhapWorkComponentView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/dhapdam/work-component.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            major_work_components = MajorWorkComponentsDhapDam.objects.filter(
                introduction__project_name="dhapdam"
            )
            context["major_work_components"] = major_work_components
            print("major_work_components", context["major_work_components"])
        except:
            context["major_work_components"] = None
        return context


class DhapWorkComponentCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/dhapdam/work-components-create.html"
    form_class = MajorWorkComponentsDhapdamForm
    success_url = reverse_lazy("dam:dadmin-work-components")

    def form_valid(self, form):
        print("work components")
        form_new = form.save(commit=False)
        try:
            intro, created = DamIntroduction.objects.get_or_create(
                project_name="dhapdam"
            )
            form_new.introduction = intro
            form_new.save()
            return super().form_valid(form)
        except DamIntroduction.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, "Please enter the introduction form"
            )
            return render(
                request,
                template_name=self.template_name,
                context=self.get_context_data(),
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work Components"
        return context


class DhapWorkComponentUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/dhapdam/work-components-update.html"
    form_class = MajorWorkComponentsDhapdamForm
    model = MajorWorkComponentsDhapDam
    success_url = reverse_lazy("dam:dadmin-work-components")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Work Components"
        return context

class DhapWorkComponentDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = MajorWorkComponentsDhapDam
    success_url = reverse_lazy("dam:dadmin-work-components")



"""===================================
----- dhap sub work components starts  ---
======================================"""


class DhapSubWorkComponentView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/dhapdam/sub-work.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            sub_major_work_components = SubMajorWorkComponents.objects.filter(
                major_work_components__introduction__project_name="dhapdam"
            )
            context["sub_major_work_components"] = sub_major_work_components
            print("major_work_components", context["major_work_components"])
        except:
            context["major_work_components"] = None
        return context


class DhapSubWorkComponentCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    form_class = SubMajorWorkComponentsForm
    success_url = reverse_lazy("dam:dadmin-sub-subwork")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sub Work"
        return context


class DhapSubWorkComponentUpdateView(
    UpdateSuccessMixin, AllUserRequiredMixin, UpdateView
):
    template_name = "admin/update.html"
    form_class = SubMajorWorkComponentsForm
    model = SubMajorWorkComponents
    success_url = reverse_lazy("dam:dadmin-sub-subwork")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sub Work Components"
        return context


class DhapSubWorkComponentDeleteView(
    DeleteSuccessMixin, AllUserRequiredMixin, DeleteView
):
    template_name = "admin/delete.html"
    model = SubMajorWorkComponents
    success_url = reverse_lazy("dam:dadmin-sub-subwork")


"""===================================
----- dhap contract components starts  ---
======================================"""


class DhapContractDetailView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/dhapdam/contract-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            contract_detail = ContractDetail.objects.get(
                introduction__project_name="dhapdam"
            )
            context["contract_detail"] = contract_detail
            print("major_work_components", context["contract_detail"])
        except:
            context["contract_detail"] = None
        return context


class DhapAddContractDetail(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/dhapdam/add-contract-detail.html"
    form_class = ContractDetailForm
    success_url = reverse_lazy("dam:dadmin-contract-detail")

    def form_valid(self, form):
        form_new = form.save(commit=False)
        try:
            intro, created = DamIntroduction.objects.get_or_create(
                project_name="dhapdam"
            )
            print("intro", intro)
            form_new.introduction = intro
            return super().form_valid(form)
        except DamIntroduction.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, "Please enter the introduction form"
            )
            return render(
                request,
                template_name=self.template_name,
                context=self.get_context_data(),
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contract"
        return context


class DhapEditContractDetail(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/dhapdam/edit-contract-detail.html"
    form_class = ContractDetailForm
    model = ContractDetail
    success_url = reverse_lazy("dam:dadmin-contract-detail")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contract"
        return context


"""=================================================
----- Design and Quality Aspects components starts  ---
====================================================="""


class DhapDesignQualityView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/dhapdam/design-quality.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            design_quality_aspects = DesignAndQualityAspects.objects.get(
                introduction__project_name="dhapdam"
            )
            context["design_quality_aspects"] = design_quality_aspects
        except:
            context["design_quality_aspects"] = None
        return context


class DhapDesignQualityCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/dhapdam/add-design-quality.html"
    form_class = DesignAndQualityAspectsForm
    success_url = reverse_lazy("dam:dadmin-design-quality")

    def form_valid(self, form):
        form_new = form.save(commit=False)
        try:
            intro = DamIntroduction.objects.get(
                project_name="dhapdam"
            )
            print("intro@@@@@@@@@@@@@@@@@@@@", intro)
            form_new.introduction = intro
            return super().form_valid(form)
        except DamIntroduction.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, "Please enter the introduction form"
            )
            return render(
                request,
                template_name=self.template_name,
                context=self.get_context_data(),
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Design and Quality Aspects"
        return context

class DhapDesignQualityUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/dhapdam/edit-design-quality.html"
    form_class = DesignAndQualityAspectsForm
    model = DesignAndQualityAspects
    success_url = reverse_lazy("dam:dadmin-design-quality")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Design and Quality Aspects"
        return context

"""=================================================
----- sub Design and Quality Aspects components starts  ---
====================================================="""


class DhapSubDesignQualityView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/dhapdam/sub-design.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            sub_design_quality_aspects = SubDesignAndQualityAspects.objects.filter(
                design_and_quality_aspects__introduction__project_name="dhapdam"
            )
            context["sub_design_quality_aspects"] = sub_design_quality_aspects
            print("major_work_components", context["sub_design_quality_aspects"])
        except:
            context["sub_design_quality_aspects"] = None
        return context


class DhapSubDesignQualityCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    form_class = SubDesignAndQualityAspectsForm
    success_url = reverse_lazy("dam:dadmin-sub-design-quality")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sub Design Quality"
        return context


class DhapSubDesignQualityUpdateView(
    UpdateSuccessMixin, AllUserRequiredMixin, UpdateView
):
    template_name = "admin/update.html"
    form_class = SubDesignAndQualityAspectsForm
    model = SubDesignAndQualityAspects
    success_url = reverse_lazy("dam:dadmin-sub-design-quality")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Sub Design Quality"
        return context


class DhapSubDesignQualityDeleteView(
    DeleteSuccessMixin, AllUserRequiredMixin, DeleteView
):
    template_name = "admin/delete.html"
    model = SubDesignAndQualityAspects
    success_url = reverse_lazy("dam:dadmin-sub-design-quality")


"""=================================================
----- environmental Aspects components starts  ---
====================================================="""


class DhapEnvironmentalAspectsView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/dhapdam/environmental.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            environmental_aspects = EnvironmentalAspects.objects.get(
                introduction__project_name="dhapdam"
            )
            context["environmental_aspects"] = environmental_aspects
            print("major_work_components", context["environmental_aspects"])
        except:
            context["environmental_aspects"] = None
        return context


class DhapEnvironmentalAspectsCreateView(
    AddSuccessMixin, AllUserRequiredMixin, CreateView
):
    template_name = "admin/dhapdam/environmental/add-env.html"
    form_class = DhapEnvironmentalAspectsForm
    success_url = reverse_lazy("dam:dadmin-environmental-aspects")

    def form_valid(self, form):
        form_new = form.save(commit=False)
        try:
            intro, created = DamIntroduction.objects.get_or_create(
                project_name="dhapdam"
            )
            print("intro", intro)
            form_new.introduction = intro
            return super().form_valid(form)
        except DamIntroduction.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, "Please enter the introduction form"
            )
            return render(
                request,
                template_name=self.template_name,
                context=self.get_context_data(),
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Environmental Aspects"
        return context


class DhapEnvironmentalAspectsUpdateView(
    UpdateSuccessMixin, AllUserRequiredMixin, UpdateView
):
    template_name = "admin/dhapdam/environmental/edit-env.html"
    model = EnvironmentalAspects
    form_class = DhapEnvironmentalAspectsForm
    success_url = reverse_lazy("dam:dadmin-environmental-aspects")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Environmental Aspects"
        return context

"""=================================================
----- maps starts  ---
====================================================="""


class DhapMapsView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/dhapdam/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            maps = Maps.objects.filter(introduction__project_name="dhapdam")
            context["maps"] = maps
            print("maps", context["maps"])
        except:
            context["maps"] = None
        return context


class MapsCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    model = Maps
    fields = ("title", "image")
    success_url = reverse_lazy("dam:dadmin-maps")

    def form_valid(self, form):
        form_new = form.save(commit=False)
        try:
            intro, created = DamIntroduction.objects.get_or_create(
                project_name="dhapdam"
            )
            print("intro", intro)
            form_new.introduction = intro
            return super().form_valid(form)
        except DamIntroduction.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, "Please enter the introduction form"
            )
            return render(
                request,
                template_name=self.template_name,
                context=self.get_context_data(),
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Maps"
        return context


class MapsUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Maps
    fields = ("title", "image")
    success_url = reverse_lazy("dam:dadmin-maps")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Maps"
        return context


class MapsDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Maps
    success_url = reverse_lazy("dam:dadmin-maps")


# nagmati dam

"""=================================================
----- nagmati introduction starts  ---
====================================================="""


class NagmatiIntroView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/nagmati/intro.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["intro"] = IntroductionOfDam.objects.get(
                introduction__project_name="nagmati"
            )
            print("context", context["intro"])
        except IntroductionOfDam.DoesNotExist:
            context["intro"] = None
        return context


class AddNagmatiIntroCreateView(AllUserRequiredMixin, FormView):
    template_name = "admin/nagmati/nagmati-add.html"
    form_class = IntroductionOfDamForm
    success_url = reverse_lazy("dam:nadmin-intro")

    def form_valid(self, form):
        form_new = form.save(commit=False)
        try:
            intro, created = DamIntroduction.objects.get_or_create(
                project_name="nagmati"
            )
            print("intro", intro)
            form_new.introduction = intro
            form_new.save()
            return super().form_valid(form)
        except DamIntroduction.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, "Please enter the introduction form"
            )
            return render(
                request,
                template_name=self.template_name,
                context=self.get_context_data(),
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NagmatiIntroUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/nagmati/nagmati-update.html"
    form_class = IntroductionOfDamForm
    model = IntroductionOfDam
    success_url = reverse_lazy("dam:nadmin-intro")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


"""=================================================
----- nagmati location starts  ---
====================================================="""


class NagmatiLocationView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/nagmati/location-and-accessibility/location.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            locations = LocationAndAccessibility.objects.get(
                introduction__project_name="nagmati"
            )
            context["locations"] = locations
            print("nagmati", locations)
        except:
            context["locations"] = None
        return context


class NagmatiLocationCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/nagmati/location-and-accessibility/locationadd.html"
    form_class = LocationAndAccessibilityForm
    success_url = reverse_lazy("dam:nadmin-location")

    def form_valid(self, form):
        form_new = form.save(commit=False)
        try:
            intro, created = DamIntroduction.objects.get_or_create(
                project_name="nagmati"
            )
            print("intro", intro)
            form_new.introduction = intro
            form_new.save()
            return super().form_valid(form)
        except DamIntroduction.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, "Please enter the introduction form"
            )
            return render(
                request,
                template_name=self.template_name,
                context=self.get_context_data(),
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Location"
        return context


class NagmatiLocationUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/nagmati/location-and-accessibility/locationupdate.html"
    form_class = LocationAndAccessibilityForm
    model = LocationAndAccessibility
    success_url = reverse_lazy("dam:nadmin-location")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Location"
        return context


"""=================================================
----- nagmati status of project starts  ---
====================================================="""


class NagmatiProjectStatusView(TemplateView):
    template_name = "admin/nagmati/status-project.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            environmental_aspects = EnvironmentalAspects.objects.get(
                introduction__project_name="nagmati"
            )
            context["environmental_aspects"] = environmental_aspects
            print("major_work_components", context["environmental_aspects"])
        except:
            context["environmental_aspects"] = None
        return context


class NagmatiProjectStatusCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/nagmati/status-project/add-status.html"
    form_class = DhapEnvironmentalAspectsForm
    success_url = reverse_lazy("dam:nadmin-project-status")

    def form_valid(self, form):
        form_new = form.save(commit=False)
        try:
            intro, created = DamIntroduction.objects.get_or_create(
                project_name="nagmati"
            )
            print("intro", intro)
            form_new.introduction = intro
            form_new.save()
            return super().form_valid(form)
        except DamIntroduction.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, "Please enter the introduction form"
            )
            return render(
                request,
                template_name=self.template_name,
                context=self.get_context_data(),
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Status of Project"
        return context


class NagmatiProjectStatusUpdateView(
    UpdateSuccessMixin, AllUserRequiredMixin, UpdateView
):
    template_name = "admin/nagmati/status-project/edit-status.html"
    form_class = DhapEnvironmentalAspectsForm
    model = EnvironmentalAspects
    success_url = reverse_lazy("dam:nadmin-project-status")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Status of Project"
        return context


"""=================================================
----- nagmati maps starts  ---
====================================================="""


class NagmatiMapsView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/nagmati/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            maps = Maps.objects.filter(introduction__project_name="nagmati")
            context["maps"] = maps
            print("maps", context["maps"])
        except:
            context["maps"] = None
        return context


class NagmatiMapsCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    model = Maps
    fields = ("title", "image")
    success_url = reverse_lazy("dam:nadmin-maps")

    def form_valid(self, form):
        form_new = form.save(commit=False)
        try:
            intro, created = DamIntroduction.objects.get_or_create(
                project_name="nagmati"
            )
            print("intro", intro)
            form_new.introduction = intro
            form_new.save()
            form_new.save()
            return super().form_valid(form)
        except DamIntroduction.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, "Please enter the introduction form"
            )
            return render(
                request,
                template_name=self.template_name,
                context=self.get_context_data(),
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Maps"
        return context


class NagmatiMapsUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Maps
    fields = ("title", "image")
    success_url = reverse_lazy("dam:nadmin-maps")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Maps"
        return context


class NagmatiMapsDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Maps
    success_url = reverse_lazy("dam:nadmin-maps")


"""=================================================
----- nagmati salient features starts  ---
====================================================="""


class NagmatiFeaturesView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/nagmati/feature.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["features"] = SalientFeatures.objects.get(
                introduction__project_name="nagmati"
            )
            print("features", context["features"])
        except:
            context["features"] = None
        return context


# add featute
class NagmatiAddFeatures(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/nagmati/add-features.html"
    form_class = SalientFeaturesNagmatiForm
    success_url = reverse_lazy("dam:nadmin-features")

    def form_valid(self, form):
        form_new = form.save(commit=False)
        try:
            intro, created = DamIntroduction.objects.get_or_create(
                project_name="nagmati"
            )
            print("intro", intro)
            form_new.introduction = intro
            form_new.save()
            return super().form_valid(form)
        except Introduction.DoesNotExist:
            messages.add_message(
                request, messages.ERROR, "Please enter the introduction form"
            )
            return render(
                request,
                template_name=self.template_name,
                context=self.get_context_data(),
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nagmati"
        return context


class NagmatiEditFeatures(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/nagmati/edit-features.html"
    model = SalientFeatures
    form_class = SalientFeaturesNagmatiForm
    success_url = reverse_lazy("dam:nadmin-features")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Nagmati"
        return context