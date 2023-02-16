from django.shortcuts import render
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
from django.views.generic import TemplateView, CreateView, UpdateView,DeleteView
from company.views import AddSuccessMixin, UpdateSuccessMixin, DeleteSuccessMixin
from .models import (
    DamLiteraures,
    DamSalientFeatures,
    StorageProjectInPipeline,
    NameOfDam,
    Lake,
)
from .forms import DamLiterauresLinkForm,DamSalientFeaturesForm,StorageProjectInPipelineForm,NameOfDamForm,LakeForm,DamLiterauresFileForm,DamLiterauresForm
from django.urls import reverse_lazy

# Create your views here.
"""===================================
------ DamLiteraures------------------  
======================================"""


class DamLiteratureTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/dam-knowledge/dam-literature.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dam_literatures"] = DamLiteraures.objects.all()
        context["title"] = "Dam Literatures"
        return context


class DamLiteratureLinkCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    form_class = DamLiterauresLinkForm
    success_url = reverse_lazy("damknowledge:dam-literature-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Dam Literatures"
        return context


class DamLiteratureFileCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    form_class = DamLiterauresFileForm
    success_url = reverse_lazy("damknowledge:dam-literature-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Dam Literatures"
        return context


class DamLiteratureUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = DamLiteraures
    form_class = DamLiterauresForm
    success_url = reverse_lazy("damknowledge:dam-literature-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Dam Literatures"
        return context


class DamLiteratureDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = DamLiteraures
    success_url = reverse_lazy("damknowledge:dam-literature-table")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel"] = "company:video-table"
        return context


"""===================================
------ salient features------------------  
======================================"""


class SalientFeaturesTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/dam-knowledge/feature-table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dam_salient_features"] = DamSalientFeatures.objects.all()
        print("dam",context["dam_salient_features"])
        context["title"] = "Salient Features"
        return context


class SalientFeaturesCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/dam-knowledge/add-feature.html"
    form_class = DamSalientFeaturesForm
    success_url = reverse_lazy("damknowledge:salient-features-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Salient Features"
        return context


class SalientFeaturesUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/dam-knowledge/edit-feature.html"
    model = DamSalientFeatures
    form_class = DamSalientFeaturesForm
    success_url = reverse_lazy("damknowledge:salient-features-table")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Salient Features"
        return context


class SalientFeaturesDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = DamSalientFeatures
    success_url = reverse_lazy("damknowledge:salient-features-table")




"""===================================
------ storage projects------------------  
======================================"""


class StorageProjectsTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/dam-knowledge/pipeline-table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["storage_project_pipeline"] = StorageProjectInPipeline.objects.all()
        context["title"] = "Storage ProjectIn Pipeline"
        return context


class StorageProjectCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/dam-knowledge/add-storage-pipeline.html"
    form_class = StorageProjectInPipelineForm
    success_url = reverse_lazy("damknowledge:storage-projects-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Salient Features"
        return context


class StorageProjectUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/dam-knowledge/edit-storage-pipeline.html"
    model = StorageProjectInPipeline
    form_class = StorageProjectInPipelineForm
    success_url = reverse_lazy("damknowledge:storage-projects-table")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Storage ProjectInPipeline"
        return context


class StorageProjectDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = StorageProjectInPipeline
    success_url = reverse_lazy("damknowledge:storage-projects-table")

"""===================================
------- name of dam -------  
======================================"""


class NameOfDamTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/dam-knowledge/dam-name-table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name_of_dam"] = NameOfDam.objects.all()
        context["title"] = "Name of Dam"
        return context


class NameOfDamCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    form_class = NameOfDamForm
    success_url = reverse_lazy("damknowledge:name-of-dam-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Name of Dam"
        return context


class NameOfDamUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = NameOfDam
    form_class = NameOfDamForm
    success_url = reverse_lazy("damknowledge:name-of-dam-table")


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Name of Dam"
        return context


class NameOfDamDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = NameOfDam
    success_url = reverse_lazy("damknowledge:name-of-dam-table")



    


"""===================================
------- lakes -------  
======================================"""


class LakesTableView(AllUserRequiredMixin, TemplateView):
    template_name = "admin/dam-knowledge/lake-table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lakes"] = Lake.objects.all()
        print("lakes",context["lakes"])
        context["title"] = "Lakes in Nepal"
        return context


class LakesCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    form_class = LakeForm
    success_url = reverse_lazy("damknowledge:lakes-table")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Lakes in Nepal"
        return context


class LakesUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Lake
    form_class = LakeForm
    success_url = reverse_lazy("damknowledge:lakes-table")



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Lakes in Nepal"
        return context


class LakesDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Lake
    success_url = reverse_lazy("damknowledge:lakes-table")
