from django.shortcuts import render
from django.views.generic import TemplateView, ListView, View, DetailView
from django.http import JsonResponse, HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect
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
from django.http import JsonResponse, HttpResponseRedirect, Http404, HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy
import json
from django.contrib import messages
from .models import Contract, ContractDetail, ContractFeature, ContractProgress
from .forms import (
    ContractForm,
    ContractDetailForm,
    ContractProgressForm,
    ContractFeatureForm,
    ContractUpdateForm,
)
from django.db import transaction
from django.utils.decorators import method_decorator
from .calculations import (
    calculate_time_extended,
    calculate_time_elapsed,
    calculate_time_remaining,
    calculate_financial_progress,
    calculate_progress_status,
)


from company.views import AddSuccessMixin, UpdateSuccessMixin, DeleteSuccessMixin

from django.utils.decorators import method_decorator
from users.decorators import (
    AllUserRequiredMixin,
    AccountantRequiredMixin,
    AdminstrationRequiredMixin,
)
from dam.models import (
    IntroductionOfDam,
    DamIntroduction,
    SalientFeatures,
    LocationAndAccessibility,
    MajorWorkComponents,
    ContractDetail,
    DesignAndQualityAspects,
    EnvironmentalAspects,
    Maps,
    MajorWorkComponentsDhapDam,
)
from django.http import JsonResponse

#---------------- static views---------------------

class ClientContractCompletedView(TemplateView):
    template_name = "contract/completed-contract.html"
class ClientContractProgressView(TemplateView):
    template_name = "contract/progress-contract.html"

#---------------- static views---------------------
# list all the contracts and Detail Contract
"""
class ContractView(TemplateView):
    # template_name = "registration/help.html"
    template_name = "frontend/contract.html"
    model = Contract

    def get(self, request, **kwargs):
        context = super(ContractView, self).get_context_data(**kwargs)
        context["completed-contracts"] = Contract.objects.filter(current_status="C")
        context["ongoing-contracts"] = Contract.objects.filter(current_status="O")

        # try except block to get Specific completed contract
        try:
            if self.kwargs.get("pk") == None:
                completed_contract = Contract.objects.get(current_status="C")
                print("cc", completed_contract)

            else:
                completed_contract = Contract.objects.get(
                    id=self.kwargs.get("pk"), current_status="C"
                )

            context["completed_contract"] = completed_contract

            # getting completed works on  completed contract
            # works_completed = completed_contract.works_completed
            # print("wc: ",json.loads(works_completed))

        except:
            context["completed_contract"] = None

        print("completed contract", context["completed_contract"])

        # try except block to get Specific ongoing contract

        try:
            if self.kwargs.get("pk") == None:
                ongoing_contract = Contract.objects.get(current_status="O")
            else:
                ongoing_contract = Contract.objects.get(
                    id=self.kwargs.get("pk"), current_status="O"
                )
            context["ongoing_contract"] = ongoing_contract
        except:
            context["ongoing_contract"] = None

        print("ongoing contract", context["ongoing_contract"])

        try:
            if self.kwargs.get("pk") == None:
                contract_progress = ContractProgress.objects.get(contract__status="O")
            else:
                contract_progress = ContractProgress.objects.get(
                    contract=self.kwargs.get("pk")
                )
            context["contract_progress"] = contract_progress
        except:
            context["contract_progress"] = None

        print("contract progress", context["contract_progress"])

        return render(request, self.template_name, context)

"""


class ContractCompletedView(TemplateView):
    # template_name = "registration/help.html"
    template_name = "frontend/contract.html"
    model = Contract

    def get(self, request, **kwargs):

        context = super().get_context_data(**kwargs)
        context["com_contracts"] = Contract.objects.filter(current_status="C").order_by("-id")
        context["on_contracts"] = Contract.objects.filter(current_status="O").order_by("-id")
        # progress
        context["pro_contracts"] = ContractProgress.objects.filter(
            contract__current_status="O"
        ).order_by("-id")

        context["contract"] = Contract.objects.all()

        # get the selected project name as per ajax call
        contract_id = self.request.GET.get("contractId", None)
        print("com contracts ###########", context["com_contracts"])
        print("on contracts ###########", context["on_contracts"])
        print("pro_contracts ###########", context["pro_contracts"])


        # try except block to get Specific completed contract
        try:
            if contract_id is None:
                # pass the latest default object if not selected
                completed_contract = Contract.objects.filter(
                    current_status="C"
                ).order_by("-id")[0]

            else:
                # execute when user selects a particualr projects
                completed_contract = Contract.objects.get(id=contract_id)
            
            context["completed_contract"] = completed_contract

            # getting completed works on  completed contract
            # works_completed = completed_contract.works_completed
            # print("wc: ",json.loads(works_completed))

        except:
            context["completed_contract"] = None
        print("complted contarct",context["completed_contract"])

        # try except block to get Specific ongoing contract
        try:
            if contract_id is None:
                ongoing_contract = Contract.objects.filter(current_status="O").order_by(
                    "-id"
                ).order_by("-id")[0]
                # ongoing_contract = Contract.objects.get(current_status="O")
            else:
                ongoing_contract = Contract.objects.get(id=contract_id)
            context["ongoing_contract"] = ongoing_contract
        except:
            context["ongoing_contract"] = None

        # try except block to get Specific progress
        try:
            if contract_id is None:
                contract_progress = ContractProgress.objects.filter(
                    contract__current_status="O"
                ).order_by("-id")[0]
                # contract_progress = ContractProgress.objects.get(contract__status="O")
            else:
                get_contract = Contract.objects.get(id=contract_id)
                contract_progress = ContractProgress.objects.get(contract=get_contract)

            if contract_progress:

                contract = contract_progress.contract
                if contract_progress.financial_progress_amount:
                    financial_progress_amount = contract_progress.financial_progress_amount
                calc_time_extend = calculate_time_extended(contract)
                calc_time_elapsed = calculate_time_elapsed(contract)
                time_remaining_on_extended_schedule = calculate_time_remaining(
                    contract
                )
                financial_percent_amount = calculate_financial_progress(
                    contract, financial_progress_amount
                )

                contract_progress_obj = ContractProgress(
                    contract=contract_progress.contract,
                    financial_progress_date=contract_progress.financial_progress_date,
                    financial_progress_amount=contract_progress.financial_progress_amount,
                    physical_progress_date=contract_progress.physical_progress_date,
                    physical_percent_amount=contract_progress.physical_percent_amount,
                    remarks=contract_progress.remarks,
                    # calcaultion part
                    time_extended_on_original_schedule=calc_time_extend,
                    time_elapsed_on_revise_schedule=calc_time_elapsed,
                    time_remaining_on_extended_schedule=time_remaining_on_extended_schedule,
                    financial_percent_amount=financial_percent_amount,
                )
                print("contract progress obj",contract_progress_obj)
                context["contract_progress"] = contract_progress_obj

            # context["contract_progress"] = contract_progress
        except:
            context["contract_progress"] = None

        return render(request, self.template_name, context)

        # contract = ContractProgress.objects.all()
        # print("contract", contract)
        # if contract:
        #     contract_progress = []
        #     for item in contract:
        #         contract = item.contract
        #         print("contract##", item.financial_progress_amount)
        #         if item.financial_progress_amount:
        #             print("financial amount",item.financial_progress_amount)
        #             financial_progress_amount = item.financial_progress_amount
        #         calc_time_extend = calculate_time_extended(contract)
        #         calc_time_elapsed = calculate_time_elapsed(contract)
        #         time_remaining_on_extended_schedule = calculate_time_remaining(contract)
        #         financial_percent_amount = calculate_financial_progress(contract,financial_progress_amount)

        #         contract_progress_obj = ContractProgress(
        #             pk = item.id,
        #             contract=item.contract,
        #             financial_progress_date = item.financial_progress_date,
        #             financial_progress_amount = item.financial_progress_amount,
        #             physical_progress_date = item.physical_progress_date,
        #             physical_percent_amount = item.physical_percent_amount,
        #             remarks=item.remarks,

        #             #calcaultion part
        #             time_extended_on_original_schedule=calc_time_extend,
        #             time_elapsed_on_revise_schedule=calc_time_elapsed,
        #             time_remaining_on_extended_schedule=time_remaining_on_extended_schedule,
        #             financial_percent_amount = financial_percent_amount,
        #         )
        #         contract_progress.append(contract_progress_obj)
        #     context["contract_progress"] = contract_progress
        #     print("contract progressssss", context["contract_progress"])



class ClientContractOngoingView (TemplateView):
    """
    View to get all ongoing contract
    """
    template_name = "contract/ongoing-contract.html"
    model = Contract

    def get(self, request, **kwargs):

        context = super().get_context_data(**kwargs)
        context["on_contracts"] = Contract.objects.filter(current_status="O").order_by("-id")

        # get the selected project name as per ajax call
        contract_id = self.request.GET.get("contractId", None)

        # try except block to get Specific ongoing contract
        try:
            if contract_id is None:
                ongoing_contract = Contract.objects.filter(current_status="O").order_by(
                    "-id"
                ).order_by("-id")[0]
                # ongoing_contract = Contract.objects.get(current_status="O")
            else:
                ongoing_contract = Contract.objects.get(id=contract_id)
            context["ongoing_contract"] = ongoing_contract
        except:
            context["ongoing_contract"] = None

        return render(request, self.template_name, context)



class ClientContractCompletedView (TemplateView):
    """
    View to get all completed contract
    """
    template_name = "contract/completed-contract.html"
    model = Contract

    def get(self, request, **kwargs):

        context = super().get_context_data(**kwargs)
        context["com_contracts"] = Contract.objects.filter(current_status="C").order_by("-id")
        # get the selected project name as per ajax call
        contract_id = self.request.GET.get("contractId", None)
        print("completed_contract@@",contract_id)


        try:
            if contract_id is None:
                # pass the latest default object if not selected
                completed_contract = Contract.objects.filter(
                    current_status="C"
                ).order_by("-id")[0]
                print("contract_id12",contract_id)
            else:
                # execute when user selects a particualr projects
                completed_contract = Contract.objects.get(id=contract_id)
                print("completed_contract@@",completed_contract)

            context["completed_contract"] = completed_contract
        except:
            context["completed_contract"] = None

        return render(request, self.template_name, context)



class ClientContractProgressView(TemplateView):
    template_name = "contract/progress-contract.html"
    model = Contract

    def get(self, request, **kwargs):

        context = super().get_context_data(**kwargs)
        # progress
        context["pro_contracts"] = ContractProgress.objects.filter(
            contract__current_status="O"
        ).order_by("-id")

        context["contract"] = Contract.objects.all()

        # get the selected project name as per ajax call
        contract_id = self.request.GET.get("contractId", None)

        # try except block to get Specific progress
        try:
            if contract_id is None:
                contract_progress = ContractProgress.objects.filter(
                    contract__current_status="O"
                ).order_by("-id")[0]
                # contract_progress = ContractProgress.objects.get(contract__status="O")
            else:
                get_contract = Contract.objects.get(id=contract_id)
                contract_progress = ContractProgress.objects.get(contract=get_contract)

            if contract_progress:

                contract = contract_progress.contract
                if contract_progress.financial_progress_amount:
                    financial_progress_amount = contract_progress.financial_progress_amount
                calc_time_extend = calculate_time_extended(contract)
                calc_time_elapsed = calculate_time_elapsed(contract)
                time_remaining_on_extended_schedule = calculate_time_remaining(
                    contract
                )
                financial_percent_amount = calculate_financial_progress(
                    contract, financial_progress_amount
                )

                contract_progress_obj = ContractProgress(
                    contract=contract_progress.contract,
                    financial_progress_date=contract_progress.financial_progress_date,
                    financial_progress_amount=contract_progress.financial_progress_amount,
                    physical_progress_date=contract_progress.physical_progress_date,
                    physical_percent_amount=contract_progress.physical_percent_amount,
                    remarks=contract_progress.remarks,
                    # calcaultion part
                    time_extended_on_original_schedule=calc_time_extend,
                    time_elapsed_on_revise_schedule=calc_time_elapsed,
                    time_remaining_on_extended_schedule=time_remaining_on_extended_schedule,
                    financial_percent_amount=financial_percent_amount,
                )
                print("contract progress obj",contract_progress_obj)
                context["contract_progress"] = contract_progress_obj

            # context["contract_progress"] = contract_progress
        except:
            context["contract_progress"] = None

        return render(request, self.template_name, context)




class ContractOngoingView(TemplateView):
    # template_name = "registration/help.html"
    template_name = "frontend/contract_ongoing.html"
    model = Contract


class ContractProgressView(TemplateView):
    # template_name = "registration/help.html"
    template_name = "frontend/contract_progress.html"
    model = Contract


# -------------------------Done above for the get component--------------------------------


# ------------contract admin section--------------------------#


class ContractCreateView(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    model = Contract
    form_class = ContractForm
    template_name = "admin/contract/addcontract.html"

    # above view is not used right now


def addContract(request):
    form = ContractForm
    if request.method == "POST":
        form = ContractForm(request.POST)
        print("form", form.errors)
        if form.is_valid():
            form.save()
            return redirect("/contract-list")

        else:
            return render(request, "admin/contract/addcontract.html", {"form": form})

    else:
        return render(request, "admin/contract/addcontract.html", {"form": form})


class ContractListView(AllUserRequiredMixin, ListView):
    model = Contract
    form_class = ContractForm
    context_object_name = "contracts"
    template_name = "admin/contract/contracts.html"

    def get_queryset(self):
        return Contract.objects.all()


class ContractDetailView(AllUserRequiredMixin, DetailView):
    model = Contract
    form_class = ContractForm
    context_object_name = "contract"
    template_name = "registration/help.html"


class ContractUpdateView(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    model = Contract
    form_class = ContractUpdateForm
    template_name = "admin/contract/editcontract.html"
    context_object_name = "contract"
    success_url = "/contract-list"

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     instance.date_of_completion_revised = self.request.user
    #     super(ContractUpdateView, self).save(form)

    # def get_context_data(self, **kwargs):
    #     if "form" not in kwargs:
    #         kwargs["form"] = self.get_form()
    #     return super().get_context_data(**kwargs)

    # def post(self, request, *args, **kwargs):
    #     print("hello corona", self.request.POST)
    #     _mutable = self.request.POST._mutable
    #     self.request.POST._mutable = True
    #     # date_of_comp_rev = self.request.POST.pop("date_of_completion_revised")
    #     form = ContractForm(self.request.POST)
    #     print("form data",form.data["date_of_completion_revised"])
    #     print("errors", form.errors)
    #     instance = self.get_object()
    #     # form = self.get_form()
    #     if form.is_valid():
    #         with transaction.atomic():
    #             form.save()
    #             instance.save()
    #             return redirect("/contract-list")
    #     else:
    #         return render(request, "admin/contract/editcontract.html", {"form": form})


class ContractDeleteView(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    template_name = "admin/delete.html"
    model = Contract
    success_url = reverse_lazy("contracts:contract-list")


# --------------- Done for the contracts-----------------------------------------


# --------------- Done for the contracts-----------------------------------------


# --------------views for Contract Detail create and Update view-----------------


class ContractDetailList(AllUserRequiredMixin, ListView):
    model = ContractDetail
    form_class = ContractDetailForm
    context_object_name = "contract_details"
    template_name = "admin/contract/detail.html"


class ContractDetailAdd(AddSuccessMixin, AllUserRequiredMixin, CreateView):
    model = ContractDetail
    form_class = ContractDetailForm
    template_name = "admin/contract/adddetail.html"

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        context = {}
        context["contracts"] = Contract.objects.all()
        context["form"] = form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            contract_detail = ContractDetail.objects.filter(
                contract=form.cleaned_data["contract"]
            )
            if contract_detail:
                messages.error(
                    request, "Already existing contract detail. Please update!"
                )
                return redirect("/contract-detail")
            else:
                form.save()
                messages.success(request, "Detail Added Successfully")
                return redirect("/contract-detail")
        else:
            messages.error(request, "Form is not valid")
            return redirect("/contract-detail")


class ContractDetailDetailView(AllUserRequiredMixin, DetailView):
    model = ContractDetail
    form_class = ContractDetail
    context_object_name = "contract-detail"
    template_name = "registration/help.html"


class ContractDetailUpdate(UpdateSuccessMixin, AllUserRequiredMixin, UpdateView):
    model = ContractDetail
    form_class = ContractDetailForm
    context_object_name = "contract"
    template_name = "admin/contract/editdetail.html"
    success_url = "/contract-detail"

    def get_context_data(self, **kwargs):
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
            kwargs["contract_list"] = Contract.objects.all()
        return super().get_context_data(**kwargs)

    def put(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            messages.success(request, "Contract Detail Updated successfully !")
            return redirect("/contract-detail")
        else:
            messages.error(request, "Contract Detail Updated Failed !")
            return HttpResponse("Invalid form")


class ContractDetailDelete(DeleteSuccessMixin, AllUserRequiredMixin, DeleteView):
    model = ContractDetail
    template_name = "admin/delete.html"
    success_url = reverse_lazy("contracts:contract-detail-list")


# ---------------------views for contract Progress page----------------------------------


class ContractProgressGet(AllUserRequiredMixin, TemplateView):
    template_name = "admin/contract/progresses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contracts"] = ContractProgress.objects.all()
        contract = ContractProgress.objects.all()
        print("contract", contract)
        if contract:
            contract_progress = []
            for item in contract:
                contract = item.contract
                print("contract##", item.financial_progress_amount)
                if item.financial_progress_amount:
                    print("financial amount", item.financial_progress_amount)
                    financial_progress_amount = item.financial_progress_amount
                calc_time_extend = calculate_time_extended(contract)
                calc_time_elapsed = calculate_time_elapsed(contract)
                time_remaining_on_extended_schedule = calculate_time_remaining(contract)
                financial_percent_amount = calculate_financial_progress(
                    contract, financial_progress_amount
                )

                contract_progress_obj = ContractProgress(
                    pk=item.id,
                    contract=item.contract,
                    financial_progress_date=item.financial_progress_date,
                    financial_progress_amount=item.financial_progress_amount,
                    physical_progress_date=item.physical_progress_date,
                    physical_percent_amount=item.physical_percent_amount,
                    remarks=item.remarks,
                    # calcaultion part
                    time_extended_on_original_schedule=calc_time_extend,
                    time_elapsed_on_revise_schedule=calc_time_elapsed,
                    time_remaining_on_extended_schedule=time_remaining_on_extended_schedule,
                    financial_percent_amount=financial_percent_amount,
                )
                contract_progress.append(contract_progress_obj)
            context["contract_progress"] = contract_progress
            print("contract progressssss", context["contract_progress"])

        # progress_status = calculate_progress_status(
        #         data["physical_percent_amount"],
        #         data["contract"],
        #         data["financial_progress_date"],
        #     )
        # time_extended_on_original_schedule = (
        #     calculate_time_extended(data["contract"]),
        # )
        # time_elapsed_on_revise_schedule = (
        #     calculate_time_elapsed(
        #         data["contract"], data["financial_progress_date"]
        #     ),
        # )
        # time_remaining_on_extended_schedule = (
        #     calculate_time_remaining(data["contract"]),
        # )
        # financial_percent_amount = (
        #     calculate_financial_progress(
        #         data["contract"], data["financial_progress_amount"]
        #     ),
        # )

        print("progress", context["contracts"])
        return context


class ContractProgressAdd(AllUserRequiredMixin, CreateView):
    template_name = "admin/contract/add-progress.html"
    form_class = ContractProgressForm
    success_url = reverse_lazy("contracts:contract-progress")

    # def get(self, request, *args, **kwargs):
    #     form = ContractProgressForm
    #     context = {}
    #     context["form"] = form
    #     context["contract_list"] = Contract.objects.all()
    #     return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ContractProgressForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            contract_progress = ContractProgress.objects.create(
                contract=data["contract"],
                financial_progress_amount=data["financial_progress_amount"],
                financial_progress_date=data["financial_progress_date"],
                physical_percent_amount=data["physical_percent_amount"],
                physical_progress_date=data["physical_progress_date"],
                remarks=data["remarks"],
            )
            return redirect("/contract-progress")
        else:
            if form.errors:
                error = "".join(map(str, form.errors["__all__"]))
            return render(
                request,
                "admin/contract/add-progress.html",
                {"form_errors": error, "form": form},
            )

            # return HttpResponse("form invalid")


class ContractProgressUpdate(AllUserRequiredMixin, UpdateSuccessMixin, UpdateView):
    model = ContractProgress
    form_class = ContractProgressForm
    template_name = "admin/contract/edit-progress.html"
    success_url = reverse_lazy("contracts:contract-progress")


class ContractProgressDelete(AllUserRequiredMixin, DeleteSuccessMixin, DeleteView):
    template_name = "admin/delete.html"
    model = ContractProgress
    success_url = reverse_lazy("contracts:contract-progress")


# ------------------views for Contract Feature ------------------------


class ContractFeatureList(AllUserRequiredMixin, ListView):
    model = ContractFeature
    context_object_name = "contract_features"
    template_name = "admin/contract/features.html"


class ContractFeatureDetail(AllUserRequiredMixin, DetailView):
    model = ContractFeature
    form_class = ContractDetailForm
    context_object_name = "contract_feature"
    template_name = "admin/contract/editdetail.html"


class ContractFeatureCreate(AllUserRequiredMixin, AddSuccessMixin, CreateView):
    model = ContractFeature
    form_class = ContractFeatureForm
    template_name = "admin/contract/add-features.html"

    def get_context_data(self, **kwargs):
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
            kwargs["contract_list"] = Contract.objects.all()
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            contract_feature = ContractFeature.objects.filter(
                contract=form.cleaned_data["contract"]
            )
            if contract_feature:
                messages.error(
                    request, "Already existing contract detail. Please update!"
                )
                return redirect("/contract-feature")
            else:
                form.save()
                messages.success(request, "Detail Added Successfully")
                return redirect("/contract-feature")
        else:
            messages.error(request, "Form is not valid")
            return redirect("/contract-feature")


class ContractFeatureUpdate(AllUserRequiredMixin, UpdateSuccessMixin, UpdateView):
    model = ContractFeature
    form_class = ContractFeatureForm
    context_object_name = "contract"
    template_name = "admin/contract/edit-features.html"
    success_url = "/contract-feature"

    def get_context_data(self, **kwargs):
        if "form" not in kwargs:
            kwargs["form"] = self.get_form()
            kwargs["contract_list"] = Contract.objects.all()
        return super().get_context_data(**kwargs)

    def put(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            messages.success(request, "Contract Feature Updated successfully !")
            return redirect("/contract-feature")
        else:
            messages.error(request, "Contract Feature Updated Failed !")
            return HttpResponse("Invalid form")


class ContractFeatureDelete(AllUserRequiredMixin, DeleteSuccessMixin, DeleteView):
    model = ContractFeature


# ------------------------views for contract details page only GET----------------------------------------


class ContractIntroductionView(AllUserRequiredMixin, TemplateView):
    template_name = "dhapdam/dhapdam.html"
    model = ContractDetail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            contract = ContractDetail.objects.get(contract=self.kwargs.get("pk"))

            context["introduction"] = contract.introduction
        except:
            context["introduction"] = None

        print("introducttion", context["introduction"])
        return context


class ContractFeatureView(AllUserRequiredMixin, TemplateView):
    # template_name = "dhapdam/dhapdam.html"
    model = ContractDetail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            contract = ContractFeature.objects.get(contract=self.kwargs.get("pk"))

            context["feature"] = contract.feature
        except:
            context["feature"] = None

        return context


class ContractLocationView(TemplateView):
    # template_name = "dhapdam/dhapdam.html"
    model = ContractDetail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            contract = ContractDetail.objects.get(contract=self.kwargs.get("pk"))

            context["location"] = contract.location_and_accessibility

        except:
            context["location"] = None

        return context


class ContractWorkComponentView(TemplateView):
    # template_name = "dhapdam/dhapdam.html"
    model = ContractDetail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            contract = ContractDetail.objects.get(contract=self.kwargs.get("pk"))

            context["work_component"] = contract.work_component
        except:
            context["work_component"] = None

        return context


class ContractDesignQualityView(TemplateView):
    # template_name = "dhapdam/dhapdam.html"
    model = ContractDetail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            contract = ContractDetail.objects.get(contract=self.kwargs.get("pk"))

            context["design_quality"] = contract.design_quality
        except:
            context["design_quality"] = None

        return context


class ContractEnviromentalAspects(TemplateView):
    # template_name = "dhapdam/dhapdam.html"
    model = ContractDetail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            contract = ContractDetail.objects.get(contract=self.kwargs.get("pk"))

            context["environmental_aspects"] = contract.environmental_aspects
        except:
            context["environmental_aspects"] = None

        return context


# Views for contract Detail page complete----------------------------------


# user side view
class DhapdamView(TemplateView):
    template_name = "dhapdam/dhapdam.html"

    def get_context_data(self, **kwargs):
        print("test")
        context = super().get_context_data(**kwargs)
        try:
            context["intro"] = IntroductionOfDam.objects.get(
                introduction__project_name="dhapdam"
            )
            print("context", context["intro"])

        except:
            context["intro"] = None

        return context


class DhapFeaturesView(TemplateView):
    template_name = "dhapdam/dhap-feature.html"

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


class DhapLocationView(TemplateView):
    template_name = "dhapdam/dhap-location.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["location"] = LocationAndAccessibility.objects.get(
                introduction__project_name="dhapdam"
            )

        except:
            context["location"] = None

        return context


class DhapWorkComponentsView(TemplateView):
    template_name = "dhapdam/dhap-comp.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["work_components"] = MajorWorkComponentsDhapDam.objects.filter(
        #     introduction__project_name="dhapdam"
        # )
        context["work_components_main_dam"] = MajorWorkComponentsDhapDam.objects.filter(
            introduction__project_name="dhapdam",sub_dam="M"
        ).values("title","id")
        context["work_components_saddle_dam"] = MajorWorkComponentsDhapDam.objects.filter(
            introduction__project_name="dhapdam",sub_dam="S"
        ).values("title","id")
        return context

class DhapWorkComponentsDetailView(DetailView):
    model = MajorWorkComponentsDhapDam
    template_name = "dhapdam/major-work-detail.html"



class DhapContractDetailView(TemplateView):
    template_name = "dhapdam/dhap-contract.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["contract_details"] = ContractDetail.objects.get(
                introduction__project_name="dhapdam"
            )
            print("contract_details", context["contract_details"])
        except:
            context["contract_details"] = None
        return context


class DhapDesignView(TemplateView):
    template_name = "dhapdam/dhap-quality.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["design_quality"] = DesignAndQualityAspects.objects.get(
                introduction__project_name="dhapdam"
            )
            print("design_quality", context["design_quality"])
        except:
            context["design_quality"] = None
        return context


class DhapEnvironmentalView(TemplateView):
    template_name = "dhapdam/dhap-env.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            environmental_aspects = EnvironmentalAspects.objects.get(
                introduction__project_name="dhapdam"
            )
            print("design_quality", environmental_aspects)
            context["environmental_aspects"] = environmental_aspects
        except:
            context["environmental_aspects"] = None
        return context


class DhapMapsView(TemplateView):
    template_name = "dhapdam/dhap-maps.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            maps = Maps.objects.filter(introduction__project_name="dhapdam")
            print("maps", maps)
            context["maps"] = maps
        except:
            context["maps"] = None
        return context
