from django import forms
from django.forms import ModelForm
from .models import Contract, ContractDetail, ContractProgress, ContractFeature


# Form class for Contract


class DateInput(forms.DateInput):
    input_type = "date"
    
class ContractForm(ModelForm):
    contract_id = forms.CharField(
        max_length=50,
        required=True,
        error_messages={"required": "Please enter contract ID!"},
    )
    project_name = forms.CharField(
        max_length=100,
        required=True,
        error_messages={"required": "Please enter Project Nmae!"},
    )
    work_name = forms.CharField(
        max_length=100,
        required=True,
        error_messages={"required": "Please enter Work Name!"},
    )
    contractor_detail = forms.CharField(
        max_length=50,
        required=True,
        error_messages={"required": "Please enter Contractor Detail !"},
    )
    amount = forms.DecimalField(
        max_digits=50,
        decimal_places=5,
        required=True,
        error_messages={"required": "Please enter Agreement Amount !"},
    )
    date_of_agreement = forms.DateField(
        required=True, error_messages={"required": "Please enter date of agreement !"}
    )
    date_of_completion = forms.DateField(
        required=True, error_messages={"required": "Please enter date of completion!"}
    )
    complete_revised_date = forms.DateField(
        required=False, error_messages={"required": "Please enter date of completion!"}
    )
    actual_expenditure = forms.DecimalField(
        max_digits=50,
        decimal_places=5,
        required=True,
        error_messages={"required": "Please enter Actual Expenditure!"},
    )
    current_status = forms.CharField(
        max_length=50,
        required=True,
        error_messages={"required": "Please enter Current Project Status !"},
    )
    contractor_liability_status = forms.CharField(
        max_length=50,
        required=True,
        error_messages={"required": "Please enter contractor liability response!"},
    )
    works_completed = forms.CharField(
        max_length=5000,
        required=True,
        error_messages={"required": "Please enter Works Completed!"},
    )

    class Meta:
        model = Contract
        fields = [
            "contract_id",
            "project_name",
            "work_name",
            "contractor_detail",
            "amount",
            "date_of_agreement",
            "date_of_completion",
            "actual_expenditure",
            "current_status",
            "contractor_liability_status",
            "works_completed",
            "complete_revised_date",
            "date_of_completion_revised"
        ]
    widgets = {
        "date_of_agreement": DateInput,"date_of_completion":DateInput,"date_of_completion_revised":DateInput,
    }



class DateInputField(forms.DateInput):
    input_type = "date"


class ContractUpdateForm(ModelForm):
    class Meta:
        model = Contract
        fields = [
            "contract_id",
            "project_name",
            "work_name",
            "contractor_detail",
            "amount",
            "date_of_agreement",
            "date_of_completion",
            "actual_expenditure",
            "current_status",
            "contractor_liability_status",
            "works_completed",
            "date_of_completion_revised"
        ]
        widgets = {"date_of_agreement": DateInputField,"date_of_completion": DateInputField,"date_of_completion_revised": DateInputField,}


    



class ContractDetailForm(ModelForm):
    introduction = forms.CharField(
        required=False,
        widget=forms.Textarea,
        error_messages={"required": "Please Enter introduction!"},
    )
    location_and_accessibility = forms.CharField(
        required=False,
        widget=forms.Textarea,
        error_messages={"required": "Please Enter location_and_accessibility!"},
    )
    work_component = forms.CharField(
        required=False,
        widget=forms.Textarea,
        error_messages={"required": "Please Enter work_component!"},
    )
    design_and_quality = forms.CharField(
        required=False,
        widget=forms.Textarea,
        error_messages={"required": "Please Enter design_and_quality!"},
    )
    environmental_aspects = forms.CharField(
        required=False,
        widget=forms.Textarea,
        error_messages={"required": "Please Enter environmental_aspects!"},
    )

    class Meta:
        model = ContractDetail
        fields = [
            "contract",
            "introduction",
            "location_and_accessibility",
            "work_component",
            "design_and_quality",
            "environmental_aspects",
        ]





class ContractProgressForm(ModelForm):
    class Meta:
        model = ContractProgress
        fields = [
            "contract",
            "time_extended_on_original_schedule",
            "time_elapsed_on_revise_schedule",
            "time_remaining_on_extended_schedule",
            "financial_progress_amount",
            "financial_progress_date",
            "financial_percent_amount",
            "physical_percent_amount",
            "physical_progress_date",
            "progress_status",
            "remarks",
        ]
        widgets = {"financial_progress_date": DateInputField,"physical_progress_date": DateInputField,}

        
    def clean(self):
        contract = self.cleaned_data["contract"]
        print("contract",contract)
        print("contract",contract.date_of_completion_revised)
        # if self.instance.year:
        #     if FiscalYear.objects.filter(year=year).exclude(year=self.instance.year).exists():
        #         raise forms.ValidationError("Same fiscal year cannot be added")
        if contract.date_of_completion_revised is None:
            raise forms.ValidationError("Please enter the complete revised date from first")

        return self.cleaned_data


class ContractFeatureForm(ModelForm):
    class Meta:
        model = ContractFeature
        fields = "__all__"
