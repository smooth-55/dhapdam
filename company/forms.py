from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext as _
from .models import (
    FiscalYear,
    FirstTrimester,
    SecondTrimester,
    ThirdTrimester,
    Structure,
    Policy,
    Contact,
    Darta,
    Chalani,
    Videos,
    CompanyProfile,
    Documents,
    Introduction,
    Photos,
    AdminstrationUploadFile,
    AccountUploadFile
)
from users.models import UserProfile
from django.core.exceptions import ValidationError
from ckeditor.widgets import CKEditorWidget



class PolicyForm(ModelForm):
    # self.fields['verb'].empty_label = "Select a Verb"
    name = forms.CharField(
        max_length=50,
        required=True,
        error_messages={"required": "Please enter contract ID!"},
    )

    class Meta:
        model = Policy
        fields = (
            "name",
            "file",
            "types",
        )


class DocumentForm(ModelForm):
    class Meta:
        model = Documents
        fields = (
            "category",
            "name",
            "file",
        )
        widgets = {
            "file": forms.FileInput(attrs={'multiple': True}),
        }

class PhotoForm(ModelForm):
    class Meta:
        model = Photos
        fields = (
            "category",
            "title",
            "image"
        )
        widgets = {
            "image": forms.FileInput(attrs={'multiple': True}),
        }

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['category'].label = "Album"

class PhotoEditForm(ModelForm):
    class Meta:
        model = Photos
        fields = (
            "category",
            "title",
            "image"
        )
    def __init__(self, *args, **kwargs):
        super(PhotoEditForm, self).__init__(*args, **kwargs)
        self.fields['category'].label = "Album"




class VideoForm(ModelForm):
    # self.fields['verb'].empty_label = "Select a Verb"

    class Meta:
        model = Videos
        fields = (
            "link",
        )


class FiscalYearForm(forms.ModelForm):
    class Meta:
        model = FiscalYear
        fields = "__all__"


    def clean_year(self):
        year = self.cleaned_data["year"]
        if self.instance.year:
            if FiscalYear.objects.filter(year=year).exclude(year=self.instance.year).exists():
                raise forms.ValidationError("Same fiscal year cannot be added")
        else:
            if FiscalYear.objects.filter(year=year).exists():
                raise forms.ValidationError("Same fiscal year cannot be added")

        return year

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
    
    def clean_phone(self):
        phone = self.cleaned_data["phone"]
        if len(phone) < 7 or len(phone) > 14:
            raise forms.ValidationError(
                "Invalid phone number"
            )
        
        return phone




class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = "__all__"



class AdminstrationUploadFileForm(ModelForm):
    class Meta:
        model = AdminstrationUploadFile
        fields = (
            "fiscal_year",
            "title",
            "files",
        )
        widgets = {
            "files": forms.FileInput(attrs={'multiple': True}),
        }


class AccountUploadFileForm(ModelForm):
    class Meta:
        model = AccountUploadFile
        fields = (
            "fiscal_year",
            "title",
            "files",
            "types",

        )
        widgets = {
            "files": forms.FileInput(attrs={'multiple': True}),
        }


"""===================================
---------  trimester forms starts --------
======================================"""


class Edittrimester(forms.ModelForm):
    """
    created to inherit in all trimester while updating the physical progress 
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = getattr(self, "instance", None)
        if instance:
            self.fields["year"]
            self.fields["name"].disabled = True
            self.fields["month1"].disabled = True
            self.fields["month1_periodic_amount"]
            self.fields["periodic_target"]
            # month 2
            self.fields["month2"].disabled = True
            self.fields["month2_periodic_amount"]
            # month3
            self.fields["month3"].disabled = True
            self.fields["month3_periodic_amount"]
            # month4
            self.fields["month4"].disabled = True
            self.fields["month4_periodic_amount"]
            self.fields["month1_cumulative_amount"].disabled = True
            self.fields["month2_cumulative_amount"].disabled = True
            self.fields["month3_cumulative_amount"].disabled = True
            self.fields["month4_cumulative_amount"].disabled = True

            self.fields["trimester_periodic"]
            self.fields["trimester_cumulative"].disabled = True

            self.fields["periodic_percentage_financial"].disabled = True
            self.fields["yearly_percentage_financial"].disabled = True


"""===================================
--------- First trimester forms --------
======================================"""


class TrimesterForm(forms.ModelForm):
    TRIMESTER_NAME = (("First Trimester", "First Trimester"),)
    trimester_name = forms.ChoiceField(
        choices=TRIMESTER_NAME, required=True,
    )  # this is extra fields passed to get name of trimester from forms(firsttrimester or secondtrimester or thirdtrimester)

    month1_periodic_amount = forms.DecimalField(required=True)
    periodic_target = forms.DecimalField(required=True)

    class Meta:
        model = FirstTrimester
        fields = (
            "name",
            "year",
            "month1",
            "month1_periodic_amount",
            "periodic_target",
            "trimester_name",  # extra fields
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call to ModelForm constructor
        for fields in self.fields:
            self.fields[fields].widget.attrs["style"] = "width:321px;height:39px;"

    

    def clean(self):
        trimester_name = self.cleaned_data["trimester_name"]
        year = self.cleaned_data["year"]
        month1 = self.cleaned_data["month1"]
        if FirstTrimester.objects.filter(name=trimester_name,year=year,month1=month1):
            raise forms.ValidationError("First Trimester with this year already exist")


class TrimesterUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrimesterUpdateForm, self).__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs["style"] = "width:321px;height:39px;"
        instance = getattr(self, "instance", None)
        if instance:
            if instance.year is not None:
                self.fields["year"].disabled = True
                # self.fields["year"].widget.attrs["style"] = "width:375px;height:40px;"

            if instance.name is not None:
                self.fields["name"].disabled = True
                # self.fields["year"].widget.attrs["style"] = "width:375px;height:40px;"

            if instance.month1 is not None:
                self.fields["month1"].disabled = True
            if instance.month1_periodic_amount is not None:
                self.fields["month1_periodic_amount"].disabled = True
            if instance.periodic_target is not None:
                self.fields["periodic_target"].disabled = True
            # month 2
            if instance.month2 is not None:
                self.fields["month2"].disabled = True
            if instance.month2_periodic_amount is not None:
                self.fields["month2_periodic_amount"].disabled = True
            # month3
            if instance.month3 is not None:
                self.fields["month3"].disabled = True
            if instance.month3_periodic_amount is not None:
                self.fields["month3_periodic_amount"].disabled = True
            # month4
            if instance.month4 is not None:
                self.fields["month4"].disabled = True
            if instance.month4_periodic_amount is not None:
                self.fields["month4_periodic_amount"].disabled = True

            if instance.periodic_physical_progress is not None:
                self.fields["periodic_physical_progress"].disabled = True
            if instance.cumulative_physical_progress is not None:
                self.fields["cumulative_physical_progress"].disabled = True
        else:
            pass

    TRIMESTER_NAME = (("First Trimester", "First Trimester"),)
    trimester_name = forms.ChoiceField(
        choices=TRIMESTER_NAME, required=False
    )  # this is extra fields passed to get name of trimester from forms(firsttrimester or secondtrimester or thirdtrimester)

    class Meta:
        model = FirstTrimester
        fields = (
            "name",
            "year",
            "month1",
            "month1_periodic_amount",
            "month2",
            "month2_periodic_amount",
            "month3",
            "month3_periodic_amount",
            "month4",
            "month4_periodic_amount",
            "periodic_target",
            "trimester_name",  # extra fields
            "periodic_physical_progress",
            "cumulative_physical_progress",
        )


class BhadraFormView(TrimesterUpdateForm):
    month2_periodic_amount = forms.DecimalField(required=True)

    class Meta(TrimesterUpdateForm.Meta):
        model = FirstTrimester


class AshojFormView(TrimesterUpdateForm):
    month3_periodic_amount = forms.DecimalField(required=True)

    class Meta(TrimesterUpdateForm.Meta):
        model = FirstTrimester


class KartikFormView(TrimesterUpdateForm):
    month4_periodic_amount = forms.DecimalField(required=True)

    class Meta(TrimesterUpdateForm.Meta):
        model = FirstTrimester


class FirstTrimCalcPeriodic(Edittrimester):
    class Meta:
        model = FirstTrimester
        fields = "__all__"


"""===================================
--------- second trimester forms --------
======================================"""


class MangisrSecondTrimesterForm(forms.ModelForm):
    TRIMESTER_NAME = (("Second Trimester", "Second Trimester"),)
    trimester_name = forms.ChoiceField(
        choices=TRIMESTER_NAME, required=False
    )  # this is extra fields passed to get name of trimester from forms(firsttrimester or secondtrimester or thirdtrimester)
    month1_periodic_amount = forms.DecimalField(required=True,)
    periodic_target = forms.DecimalField(required=True,)

    class Meta:
        model = SecondTrimester
        fields = (
            "name",
            "year",
            "month1",
            "month1_periodic_amount",
            "periodic_target",
            "trimester_name",  # extra fields
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call to ModelForm constructor
        for fields in self.fields:
            self.fields[fields].widget.attrs["style"] = "width:321px;height:40px;"


class SecondTrimesterUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SecondTrimesterUpdateForm, self).__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs["style"] = "width:321px;height:40px;"
        instance = getattr(self, "instance", None)
        if instance:
            if instance.year is not None:
                self.fields["year"].disabled = True
            if instance.name is not None:
                self.fields["name"].disabled = True
            if instance.month1 is not None:
                self.fields["month1"].disabled = True
            if instance.month1_periodic_amount is not None:
                self.fields["month1_periodic_amount"].disabled = True
            if instance.periodic_target is not None:
                self.fields["periodic_target"].disabled = True
            # month 2
            if instance.month2 is not None:
                self.fields["month2"].disabled = True
            if instance.month2_periodic_amount is not None:
                self.fields["month2_periodic_amount"].disabled = True
            # month3
            if instance.month3 is not None:
                self.fields["month3"].disabled = True
            if instance.month3_periodic_amount is not None:
                self.fields["month3_periodic_amount"].disabled = True
            # month4
            if instance.month4 is not None:
                self.fields["month4"].disabled = True
            if instance.month4_periodic_amount is not None:
                self.fields["month4_periodic_amount"].disabled = True
        else:
            pass

    TRIMESTER_NAME = (
        ("Select", "Select"),
        ("First Trimester", "First Trimester"),
        ("Second Trimester", "Second Trimester"),
        ("Third Trimester", "Third Trimester"),
    )
    trimester_name = forms.ChoiceField(
        choices=TRIMESTER_NAME, required=False
    )  # this is extra fields passed to get name of trimester from forms(firsttrimester or secondtrimester or thirdtrimester)
    month2_periodic_amount = forms.CharField(max_length=50, required=True,)

    class Meta:
        model = SecondTrimester
        fields = (
            "name",
            "year",
            "month1",
            "month1_periodic_amount",
            "month2",
            "month2_periodic_amount",
            "month3",
            "month3_periodic_amount",
            "month4",
            "month4_periodic_amount",
            "periodic_target",
            "trimester_name",  # extra fields
        )


class PoushFormView(SecondTrimesterUpdateForm):
    month2_periodic_amount = forms.DecimalField(required=True)

    class Meta(SecondTrimesterUpdateForm.Meta):
        model = SecondTrimester


class MaghFormView(SecondTrimesterUpdateForm):
    month3_periodic_amount = forms.DecimalField(required=True)

    class Meta(SecondTrimesterUpdateForm.Meta):
        model = SecondTrimester


class FalgunFormView(SecondTrimesterUpdateForm):
    month4_periodic_amount = forms.DecimalField(required=True)

    class Meta(SecondTrimesterUpdateForm.Meta):
        model = SecondTrimester


class SecondTrimCalcPeriodic(Edittrimester):
    class Meta:
        model = SecondTrimester
        fields = "__all__"


"""===================================
--------- Third trimester forms --------
======================================"""


class ChaitraThirdTrimesterForm(forms.ModelForm):
    TRIMESTER_NAME = (("Third Trimester", "Third Trimester"),)
    trimester_name = forms.ChoiceField(
        choices=TRIMESTER_NAME, required=False
    )  # this is extra fields passed to get name of trimester from forms(firsttrimester or secondtrimester or thirdtrimester)
    month1_periodic_amount = forms.DecimalField(required=True,)
    periodic_target = forms.DecimalField(required=True,)

    class Meta:
        model = ThirdTrimester
        fields = (
            "name",
            "year",
            "month1",
            "month1_periodic_amount",
            "periodic_target",
            "trimester_name",  # extra fields
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Call to ModelForm constructor
        for fields in self.fields:
            self.fields[fields].widget.attrs["style"] = "width:321px;height:40px;"


class ThirdTrimesterUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ThirdTrimesterUpdateForm, self).__init__(*args, **kwargs)
        for fields in self.fields:
            self.fields[fields].widget.attrs["style"] = "width:321px;height:40px;"
        instance = getattr(self, "instance", None)
        if instance:
            if instance.year is not None:
                self.fields["year"].disabled = True
            if instance.name is not None:
                self.fields["name"].disabled = True
            if instance.month1 is not None:
                self.fields["month1"].disabled = True
            if instance.month1_periodic_amount is not None:
                self.fields["month1_periodic_amount"].disabled = True
            if instance.periodic_target is not None:
                self.fields["periodic_target"].disabled = True
            # month 2
            if instance.month2 is not None:
                self.fields["month2"].disabled = True
            if instance.month2_periodic_amount is not None:
                self.fields["month2_periodic_amount"].disabled = True
            # month3
            if instance.month3 is not None:
                self.fields["month3"].disabled = True
            if instance.month3_periodic_amount is not None:
                self.fields["month3_periodic_amount"].disabled = True
            # month4
            if instance.month4 is not None:
                self.fields["month4"].disabled = True
            if instance.month4_periodic_amount is not None:
                self.fields["month4_periodic_amount"].disabled = True
        else:
            pass

    class Meta:
        model = ThirdTrimester
        fields = (
            "name",
            "year",
            "month1",
            "month1_periodic_amount",
            "month2",
            "month2_periodic_amount",
            "month3",
            "month3_periodic_amount",
            "month4",
            "month4_periodic_amount",
            "periodic_target",
        )


class BaisakhFormView(ThirdTrimesterUpdateForm):
    month2_periodic_amount = forms.DecimalField(required=True)

    class Meta(ThirdTrimesterUpdateForm.Meta):
        model = ThirdTrimester


class JesthaFormView(ThirdTrimesterUpdateForm):
    month3_periodic_amount = forms.DecimalField(required=True)

    class Meta(ThirdTrimesterUpdateForm.Meta):
        model = ThirdTrimester


class AsarFormView(ThirdTrimesterUpdateForm):
    month4_periodic_amount = forms.DecimalField(required=True)

    class Meta(ThirdTrimesterUpdateForm.Meta):
        model = ThirdTrimester


class ThirdTrimCalcPeriodic(Edittrimester):
    class Meta:
        model = ThirdTrimester
        fields = "__all__"


# ---------------Darta and Chalani form-------------------


class DateInput(forms.DateInput):
    input_type = "date"

class DartaForm(forms.ModelForm):
    class Meta:
        model = Darta
        fields = ("darta_no","date","patra_no","cha_no","patra_received_date","sender","address","subject","medium","remark","image")
    # widgets = {
    #     "date": DateInput,
    #     "patra_received_date": DateInput,
    # }


class ChalaniForm(forms.ModelForm):
    class Meta:
        model = Chalani
        fields = "__all__"
    widgets = {
        "date": DateInput,
    }



class IntroductionForm(forms.ModelForm):
    """
    Intoduction form
    """

    class Meta:
        model = Introduction
        fields = ("content_upload","image")
    

