from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse, HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    View,
    DetailView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from company.views import AddSuccessMixin, UpdateSuccessMixin, DeleteSuccessMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from users.decorators import (
    AllUserRequiredMixin,
    AccountantRequiredMixin,
    AdminstrationRequiredMixin
)


# Create your views here.
# material TEst
# class EarthFillingListView(TemplateView):
#     template_name = "admin/construction/test/material/earth-filling.html"



class EarthFillingListView(FormMixin,AllUserRequiredMixin, ListView):
    model = EarthFillingMaterial
    form_class = CommonMaterialTestForm
    context_object_name = "tests"
    template_name = "admin/construction/test/material/earth-filling.html"



class EarthFillingAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    model = EarthFillingMaterial
    form_class = CommonMaterialTestForm
    template_name = "admin/construction/test/material/earth-filling.html"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            messages.success(request, "Added Successfully")
            return redirect("earth-filling-list")
        else:
            messages.error(request, "Form is not valid")
            return HttpResponse("Form is not valid")



class EarthFillingUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    model = EarthFillingMaterial
    form_class = CommonMaterialTestForm
    context_object_name = "testup"
    template_name = "admin/update.html"
    success_url = "/admin/construction/material/earth-filling"

    def get_context_data(self, **kwargs):
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
            kwargs["title"] = "Earth Filling"
        return super().get_context_data(**kwargs)



class EarthFillingDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    model = EarthFillingMaterial
    success_url = reverse_lazy("earth-filling-list")
    template_name = "admin/delete.html"


# --------------------- Earth Filling View Completed---------------------



class FaceSlabATestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/material/bedding.html"
    model = FaceSlabBeddingMaterial2A
    context_object_name = "tests"



class FaceSlabATestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/material/bedding.html"
    model = FaceSlabBeddingMaterial2A

    form_class = FaceSlab2AForm
    success_url = reverse_lazy("face-slab-2a-list")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():

            form.save()
            messages.success(request, "Added Successfully")
            return redirect("face-slab-2a-list")
        else:
            messages.error(request, "Form is not valid")
            return HttpResponse("Form is not valid")



class FaceSlabATestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = FaceSlabBeddingMaterial2A
    form_class = FaceSlab2AForm

    success_url = reverse_lazy("face-slab-2a-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Face Slab 2A"
        return context



class FaceSlabATestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = FaceSlabBeddingMaterial2A

    success_url = reverse_lazy("face-slab-2a-list")


# ------------------- FaceSlab 2A completed -------------------------



class FaceSlabBTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/material/face-slab.html"
    model = FaceSlabBeddingMaterial2B
    context_object_name = "tests"



class FaceSlabBTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/material/face-slab.html"
    model = FaceSlabBeddingMaterial2B

    form_class = FaceSlab2BForm
    success_url = reverse_lazy("face-slab-2b-list")



class FaceSlabBTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = FaceSlabBeddingMaterial2B
    form_class = FaceSlab2BForm

    success_url = reverse_lazy("face-slab-2b-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Face Slab 2B"
        return context



class FaceSlabBTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = FaceSlabBeddingMaterial2B
    success_url = reverse_lazy("face-slab-2b-list")


# ---------------------- Face Slab 2B Done ----------------



class SmallRockTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/material/small-rock.html"
    model = SmallSizeRock300MM
    context_object_name = "tests"



class SmallRockTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/material/small-rock.html"
    model = SmallSizeRock300MM
    fields = "__all__"
    success_url = reverse_lazy("small-size-rock-list")



class SmallRockTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = SmallSizeRock300MM
    fields = "__all__"
    success_url = reverse_lazy("small-size-rock-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Small Size Rock"
        return context



class SmallRockTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = SmallSizeRock300MM
    success_url = reverse_lazy("small-size-rock-list")


# ---------------------Small Rock test view Done ----------------------

class FirstClassTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/material/first-rock.html"
    model = SmallSizeRock600MM
    context_object_name = "tests"



class FirstClassTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/material/small-rock.html"
    model = SmallSizeRock600MM
    form_class = SmallSizeRock600MMForm
    success_url = reverse_lazy("first-class-rock-list")



class FirstClassTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = SmallSizeRock600MM
    form_class = SmallSizeRock600MMForm
    success_url = reverse_lazy("first-class-rock-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "First Class Rock Fill"
        return context



class FirstClassTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = SmallSizeRock600MM
    success_url = reverse_lazy("first-class-rock-list")


# -----------------------First Class Test view Done --------------



class SecondClassTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/material/second-rock.html"
    model = SecondClassRock1000MM
    context_object_name = "tests"



class SecondClassTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/material/small-rock.html"
    model = SecondClassRock1000MM
    form_class = SecondClassRock1000MMForm
    success_url = reverse_lazy("second-class-rock-list")



class SecondClassTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = SecondClassRock1000MM
    form_class = SecondClassRock1000MMForm
    success_url = reverse_lazy("second-class-rock-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Second Class Rock Fill"
        return context



class SecondClassTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = SecondClassRock1000MM
    success_url = reverse_lazy("second-class-rock-list")


# --------------------------Second Class Test View Done -----------------



class RockFillTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/material/rock-fill.html"
    model = RockFill
    context_object_name = "tests"



class RockFillTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/material/rock-fill.html"
    model = RockFill

    form_class = RockFillForm
    success_url = reverse_lazy("rock-fill-list")



class RockFillTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = RockFill
    form_class = RockFillForm

    success_url = reverse_lazy("rock-fill-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Rock Fill"
        return context



class RockFillTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = RockFill

    success_url = reverse_lazy("rock-fill-list")


# -----------------------Rock Fill test view done --------------------

class ConcreteLargeTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/material/ca-40.html"
    model = ConcreteAggregate40mm
    context_object_name = "tests"



class ConcreteLargeTestAddView(AddSuccessMixin, CreateView):
    template_name = "admin/construction/test/material/ca-40.html"
    model = ConcreteAggregate40mm

    form_class = ConcreteAggregate40mmForm
    success_url = reverse_lazy("concrete-aggregate-40mm-list")



class ConcreteLargeTestUpdateView(AllUserRequiredMixin,UpdateSuccessMixin, UpdateView):
    template_name = "admin/update.html"
    model = ConcreteAggregate40mm
    form_class = ConcreteAggregate40mmForm

    success_url = reverse_lazy("concrete-aggregate-40mm-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Concrete Large Test"
        return context



class ConcreteLargeTestDeleteView(AllUserRequiredMixin,DeleteSuccessMixin, DeleteView):
    template_name = "admin/delete.html"
    model = ConcreteAggregate40mm

    success_url = reverse_lazy("concrete-aggregate-40mm-list")


# -----------------Concreate Large 40MM Test view Done ----------------------



class ConcreteMediumTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/material/ca-20.html"
    model = ConcreteAggregate20mm
    context_object_name = "tests"



class ConcreteMediumTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/material/ca-20.html"
    model = ConcreteAggregate20mm

    form_class = ConcreteAggregate20mmForm
    success_url = reverse_lazy("concrete-aggregate-20mm-list")



class ConcreteMediumTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = ConcreteAggregate20mm
    form_class = ConcreteAggregate20mmForm

    success_url = reverse_lazy("concrete-aggregate-20mm-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Concrete Large Test"
        return context



class ConcreteMediumTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = ConcreteAggregate20mm

    success_url = reverse_lazy("concrete-aggregate-20mm-list")


# -----------------Concreate Medium 20MM Test view Done ----------------------



class ConcreteSmallTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/material/ca-10.html"
    model = ConcreteAggregate10mm
    context_object_name = "tests"



class ConcreteSmallTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/material/ca-10.html"
    model = ConcreteAggregate10mm
    form_class = ConcreteAggregate10mmForm
    success_url = reverse_lazy("concrete-aggregate-10mm-list")



class ConcreteSmallTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = ConcreteAggregate10mm
    form_class = ConcreteAggregate10mmForm

    success_url = reverse_lazy("concrete-aggregate-10mm-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Concrete Small Test"
        return context



class ConcreteSmallTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = ConcreteAggregate10mm

    success_url = reverse_lazy("concrete-aggregate-10mm-list")


# -----------------Concreate Small 10MM Test view Done ----------------------



class FineAggregateTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/material/fine-aggregate.html"
    model = FineAggregate
    context_object_name = "tests"



class FineAggregateTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/material/fine-aggregate.html"
    model = FineAggregate

    form_class = FineAggregateForm
    success_url = reverse_lazy("fine-aggregate-list")



class FineAggregateTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = FineAggregate
    form_class = FineAggregateForm

    success_url = reverse_lazy("fine-aggregate-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Fine Aggregate Test"
        return context



class FineAggregateTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = FineAggregate

    success_url = reverse_lazy("fine-aggregate-list")


# ----------------- Fine Aggregate View DOne ----------------------------------

class CementTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/material/cement.html"
    model = Cement
    context_object_name = "tests"



class CementTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/material/cement.html"
    model = Cement

    form_class = CementForm
    success_url = reverse_lazy("cement-list")



class CementTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Cement
    form_class = CementForm

    success_url = reverse_lazy("cement-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Cement Test"
        return context



class CementTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Cement

    success_url = reverse_lazy("cement-list")


# ----------------Cement View Done-------------------------------------

class GranularTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/material/granular.html"
    model = GranularSubBase
    context_object_name = "tests"



class GranularTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/material/granular.html"
    model = GranularSubBase

    form_class = GranularSubBaseForm
    success_url = reverse_lazy("granular-list")



class GranularTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = GranularSubBase
    form_class = GranularSubBaseForm

    success_url = reverse_lazy("granular-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Granular Base Test"
        return context



class GranularTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = GranularSubBase

    success_url = reverse_lazy("granular-list")


# ----------------Granular Sub Base View Done-------------------------------------



class ConcreteTestView(AllUserRequiredMixin,ListView):
    model = ConcreteTests
    template_name = "admin/construction/test/work/test-concrete.html"
    context_object_name = "tests"



class ConcreteTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/work/test-concrete.html"
    model = ConcreteTests

    form_class = ConcreteTestsForm
    success_url = reverse_lazy("concrete-test-list")



class ConcreteTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = ConcreteTests
    form_class = ConcreteTestsForm

    success_url = reverse_lazy("concrete-test-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Concrete Test"
        return context



class ConcreteTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = ConcreteTests

    success_url = reverse_lazy("concrete-test-list")


# ---------------------- Concreate Test View Done ---------------------


# ----------------------Compaction Test Start -----------------------

class CompactionTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/work/test-compaction.html"
    model = CompactionTests
    context_object_name = "tests"



class CompactionTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/work/test-compaction.html"
    model = CompactionTests

    form_class = CompactionTestsForm
    success_url = reverse_lazy("compaction-test-list")



class CompactionTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = CompactionTests
    form_class = CompactionTestsForm

    success_url = reverse_lazy("compaction-test-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Concrete Test"
        return context



class CompactionTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = CompactionTests

    success_url = reverse_lazy("compaction-test-list")


# ----------------------Compaction Test End -----------------------
# ----------------------Grouting Test Start -----------------------

class GroutingTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/work/test-grouting.html"
    model = GroutingTests
    context_object_name = "tests"



class GroutingTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/work/test-grouting.html"
    model = GroutingTests

    form_class = GroutingTestsForm
    success_url = reverse_lazy("grouting-test-list")



class GroutingTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = GroutingTests
    form_class = GroutingTestsForm

    success_url = reverse_lazy("grouting-test-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Grouting Test"
        return context



class GroutingTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = GroutingTests

    success_url = reverse_lazy("grouting-test-list")


# ----------------------Grouting Test End -----------------------

class CopperTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/work/test-copper.html"
    model = CopperWaterStopperTests
    context_object_name = "tests"



class CopperTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/work/test-copper.html"
    model = CopperWaterStopperTests

    form_class = CopperWaterStopperTestsForm
    success_url = reverse_lazy("copper-test-list")



class CopperTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = CopperWaterStopperTests
    form_class = CopperWaterStopperTestsForm

    success_url = reverse_lazy("copper-test-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Copper Water Stopper Test"
        return context



class CopperTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = CopperWaterStopperTests

    success_url = reverse_lazy("copper-test-list")


# ----------------------Copper Test End -----------------------

class PermeabilityTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/work/test-permeability.html"
    model = PermeabilityTests
    context_object_name = "tests"



class PermeabilityTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/work/test-permeability.html"
    model = PermeabilityTests

    form_class = PermeabilityTestsForm
    success_url = reverse_lazy("permeability-test-list")



class PermeabilityTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = PermeabilityTests
    form_class = PermeabilityTestsForm

    success_url = reverse_lazy("permeability-test-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Permeability Test"
        return context



class PermeabilityTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = PermeabilityTests

    success_url = reverse_lazy("permeability-test-list")


# ----------------------Permeability Test End -----------------------



class GeophysicalTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/work/test-geophysical.html"
    model = Geophysical
    context_object_name = "tests"



class GeophysicalTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/work/test-geophysical.html"
    model = Geophysical

    form_class = GeophysicalForm
    success_url = reverse_lazy("geophysical-test-list")



class GeophysicalTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Geophysical
    form_class = GeophysicalForm

    success_url = reverse_lazy("geophysical-test-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Geophyisical Investigation"
        return context



class GeophysicalTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Geophysical

    success_url = reverse_lazy("geophysical-test-list")


# ----------------------Geophysical Test End -----------------------



class CoreDrillTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/work/test-core-drill.html"
    model = CoreDrilltest
    context_object_name = "tests"



class CoreDrillTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/work/test-core-drill.html"
    model = CoreDrilltest

    form_class = CoreDrilltestForm
    success_url = reverse_lazy("core-drill-list")



class CoreDrillTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = CoreDrilltest
    form_class = CoreDrilltestForm

    success_url = reverse_lazy("core-drill-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Core Drill Test"
        return context



class CoreDrillTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = CoreDrilltest

    success_url = reverse_lazy("core-drill-list")


# ----------------------Core Drill Test End -----------------------



class DocumentationTestListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/test/test-document.html"
    model = QADocumentation
    context_object_name = "tests"



class DocumentationTestAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/test/test-document.html"
    model = QADocumentation

    form_class = QADocumentationForm
    success_url = reverse_lazy("documentation-test-list")



class DocumentationTestUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = QADocumentation
    form_class = QADocumentationForm

    success_url = reverse_lazy("documentation-test-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Documentation Test"
        return context



class DocumentationTestDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = QADocumentation

    success_url = reverse_lazy("documentation-test-list")


# ----------------------Documentation Test End -----------------------


# ----------------------------------Earth Equipment View -------------------------



class EarthEquipmentListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/equipment/eq-earth.html"
    model = EarthMovingCompaction
    context_object_name = "tests"



class EarthEquipmentAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/equipment/eq-earth.html"
    model = EarthMovingCompaction
    form_class = EarthMovingCompactionForm
    success_url = reverse_lazy("earth-equipment-list")



class EarthEquipmentUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = EarthMovingCompaction
    form_class = EarthMovingCompactionForm
    success_url = reverse_lazy("earth-equipment-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Earth Moving and Compaction"
        return context



class EarthEquipmentDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = EarthMovingCompaction
    success_url = reverse_lazy("earth-equipment-list")


# ----------------------------------Earth Equipment View Done -------------------------

# ----------------------------------Concreting Equipment View  -------------------------

class ConcretingEquipmentListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/equipment/eq-concreting.html"
    model = ConcretingEquipments
    context_object_name = "tests"



class ConcretingEquipmentAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/equipment/eq-concreting.html"
    model = ConcretingEquipments
    form_class = ConcretingEquipmentsForm
    success_url = reverse_lazy("concreting-equipment-list")



class ConcretingEquipmentUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = ConcretingEquipments
    form_class = ConcretingEquipmentsForm
    success_url = reverse_lazy("concreting-equipment-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Concreting Equipment"
        return context



class ConcretingEquipmentDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = ConcretingEquipments
    success_url = reverse_lazy("concreting-equipment-list")


# ----------------------------------Concreting Equipment View Done -------------------------
# ----------------------------------Grouting Equipment View  -------------------------



class GroutingEquipmentListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/equipment/eq-grouting.html"
    model = GroutingEquipments
    context_object_name = "tests"



class GroutingEquipmentAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/equipment/eq-grouting.html"
    model = GroutingEquipments
    form_class = GroutingEquipmentsForm
    success_url = reverse_lazy("grouting-equipment-list")



class GroutingEquipmentUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = GroutingEquipments
    form_class = GroutingEquipmentsForm
    success_url = reverse_lazy("grouting-equipment-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Concreting Equipment"
        return context



class GroutingEquipmentDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = GroutingEquipments
    success_url = reverse_lazy("grouting-equipment-list")


# ----------------------------------Grouting Equipment View Done -------------------------
# ----------------------------------Brazing Equipment View  -------------------------



class BrazingEquipmentListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/equipment/eq-brazing.html"
    model = BrazingEquipments
    context_object_name = "tests"



class BrazingEquipmentAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/equipment/eq-brazing.html"
    model = BrazingEquipments
    form_class = BrazingEquipmentsForm
    success_url = reverse_lazy("brazing-equipment-list")



class BrazingEquipmentUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = BrazingEquipments
    form_class = BrazingEquipmentsForm
    success_url = reverse_lazy("brazing-equipment-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Brazing Equipment"
        return context



class BrazingEquipmentDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = BrazingEquipments
    success_url = reverse_lazy("brazing-equipment-list")


# ----------------------------------Brazing Equipment View Done -------------------------

# ---------------------------------- Design drawing start -------------------------



class DesignDrawingListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/design-drawing.html"
    model = Design
    context_object_name = "design"



class DesignDrawingAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    model = Design
    fields = "__all__"
    success_url = reverse_lazy("design-drawing-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Design/Drawing"
        return context



class DesignDrawingUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Design
    fields = "__all__"
    success_url = reverse_lazy("design-drawing-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Design/drawing"
        return context


class DesignDrawingDeleteView(DeleteSuccessMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Design
    success_url = reverse_lazy("design-drawing-list")


# ---------------------------------- Design drawing end -------------------------

# ----------------------------------Survey Equipment test---------------------

class SurveyEquipmentListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/equipment/eq-survey.html"
    model = SurveyEquipments
    context_object_name = "tests"



class SurveyEquipmentAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/equipment/eq-survey.html"
    model = SurveyEquipments

    form_class = SurveyEquipmentsForm
    success_url = reverse_lazy("survey-equipment-list")



class SurveyEquipmentUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = SurveyEquipments
    form_class = SurveyEquipmentsForm

    success_url = reverse_lazy("survey-equipment-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Survey Equiment Test"
        return context



class SurveyEquipmentDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = SurveyEquipments

    success_url = reverse_lazy("survey-equipment-list")


# -------------------------------------- Survey Equipments test done--------------------------
# -------------------------------------- Lab Equipments test --------------------------

class LabEquipmentListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/equipment/eq-lab.html"
    model = LabEquipments
    context_object_name = "tests"



class LabEquipmentAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/equipment/eq-lab.html"
    model = LabEquipments
    form_class = LabEquipmentsForm
    success_url = reverse_lazy("lab-equipment-list")



class LabEquipmentUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = LabEquipments
    form_class = LabEquipmentsForm
    success_url = reverse_lazy("lab-equipment-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Lab Equipment Test"
        return context



class LabEquipmentDeleteView(DeleteSuccessMixin,AllUserRequiredMixin,DeleteView):
    template_name = "admin/delete.html"
    model = LabEquipments
    success_url = reverse_lazy("lab-equipment-list")


# -------------------------------------- Lab Equipments test done--------------------------
# -------------------------------------- Geophysical Investigation test \--------------------------



class GeophysicalEquipmentListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/equipment/eq-geophysical.html"
    model = GeophysicalInvestigationEquipments
    context_object_name = "tests"



class GeophysicalEquipmentAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/construction/equipment/eq-geophysical.html"
    model = GeophysicalInvestigationEquipments
    form_class = GeophysicalInvestigationEquipmentsForm
    success_url = reverse_lazy("geophysical-equipment-list")



class GeophysicalEquipmentUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = GeophysicalInvestigationEquipments
    form_class = GeophysicalInvestigationEquipmentsForm
    success_url = reverse_lazy("geophysical-equipment-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Geophysical Investigation Equipment"
        return context



class GeophysicalEquipmentDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = GeophysicalInvestigationEquipments
    success_url = reverse_lazy("geophysical-equipment-list")


# -------------------------------------- Geophysical Investigation test done--------------------------


# ---------------------------------- mos start -------------------------



class MethodOfStatementListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/mos.html"
    model = MethodOfStatements
    context_object_name = "mos"



class MethodOfStatementAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    model = MethodOfStatements
    fields = "__all__"
    success_url = reverse_lazy("mos-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Method of Statments"
        return context



class MethodOfStatementUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = MethodOfStatements
    fields = "__all__"
    success_url = reverse_lazy("mos-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Method of Statments"
        return context



class MethodOfStatementDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = MethodOfStatements
    success_url = reverse_lazy("mos-list")


# ---------------------------------- mos end -------------------------

# ---------------------------------- report start -------------------------



class ReportsListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/reports.html"
    model = Reports
    context_object_name = "reports"



class ReportAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    model = Reports
    fields = "__all__"
    success_url = reverse_lazy("reports-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Reports"
        return context



class ReportUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = Reports
    fields = "__all__"
    success_url = reverse_lazy("reports-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "Reports"
        return context



class ReportDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Reports
    success_url = reverse_lazy("reports-list")


# ---------------------------------- report end -------------------------
# ---------------------------------- workfootages start -------------------------



class WorkFootageListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/footage-work.html"
    model = WorkFootages
    context_object_name = "workfootages"



class WorkFootageAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    model = WorkFootages
    fields = "__all__"
    success_url = reverse_lazy("work-footage-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "WorkFootages"
        return context



class WorkFootageUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = WorkFootages
    fields = "__all__"
    success_url = reverse_lazy("work-footage-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "WorkFootages"
        return context



class WorkFootageDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = WorkFootages
    success_url = reverse_lazy("work-footage-list")


# ---------------------------------- testfootages start -------------------------



class TestFootageListView(AllUserRequiredMixin,ListView):
    template_name = "admin/construction/footage-test.html"
    model = TestFootages
    context_object_name = "testfootages"



class TestFootageAddView(AddSuccessMixin,AllUserRequiredMixin, CreateView):
    template_name = "admin/create.html"
    model = TestFootages
    fields = "__all__"
    success_url = reverse_lazy("test-footage-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "TestFootages"
        return context



class TestFootageUpdateView(UpdateSuccessMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = TestFootages
    fields = "__all__"
    success_url = reverse_lazy("test-footage-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["title"] = "TestFootages"
        return context



class TestFootageDeleteView(DeleteSuccessMixin,AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = TestFootages
    success_url = reverse_lazy("test-footage-list")


# ---------------------------------- testfootages end -------------------------


# work
