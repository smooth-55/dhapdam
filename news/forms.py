from django import forms
from .models import News, RecentActivities, HomeNotice, Message
from bootstrap_modal_forms.forms import BSModalModelForm
from company.models import Darta, Chalani
from ckeditor.widgets import CKEditorWidget


class NewsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        exclude = ("views",)


class RecentActivitiesForm(forms.ModelForm):
    title = forms.CharField(required=True)
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = RecentActivities
        exclude = ("views",)
        required_css_class = "required"


class HomeNoticeForm(forms.ModelForm):
    display = forms.CheckboxInput(attrs={"style": "width:500px;height:500px;margin-left:0px;padding-left:0px;"})

    class Meta:
        model = HomeNotice
        fields = ("image", "content", "files", "display")
       

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("name", "content", "designation", "image")


class DateInput(forms.DateInput):
    input_type = "date"


class DartaForm(forms.ModelForm):
    class Meta:
        model = Darta
        fields = ('darta_no', 'date', 'patra_no', 'cha_no', 'patra_received_date', 'sender', 'address', 'subject',
         'medium', 'remark', 'image', 'eng_date')
        widgets = {
                "image": forms.FileInput(attrs={'multiple': True}),
        }



class ChalaniForm(forms.ModelForm):

    class Meta:
        model = Chalani
        fields = ("chalani_no","date","patra_no","chalani_perform_date","sender","address","subject","remark","image")

        widgets = {
                "image": forms.FileInput(attrs={'multiple': True}),
        }

