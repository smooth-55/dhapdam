from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile,EmployeeProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model
User = get_user_model()

class LoginForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    # def clean(self):
    #     if self.is_valid():
    #         email = self.cleaned_data["email"]
    #         password = self.cleaned_data["password"]

    #         if not authenticate(email=email, password=password):
    #             raise forms.ValidationError("Invalid credential")


class DateInput(forms.DateInput):
    input_type = "date"


class RegisterForm(UserCreationForm):
    phone = forms.CharField(
        max_length=50,
        required=True,
        error_messages={"required": "Please enter phone number!"},
    )
    full_name = forms.CharField(
        max_length=50,
        required=True,
        error_messages={"required": "Please enter your name!"},
    )
    id_number = forms.CharField(
        max_length=50,
        required=False,
        error_messages={"required": "Please enter id number!"}

    )
    class Meta:
        model = UserProfile
        fields = [
            "email",
            "full_name",
            "designation",
            "phone",
            "dob",
            "identification",
            "id_number",
            "password1",
            "password2",
            "image",
            "username",
        
        ]
        widgets = {"dob": DateInput,}

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        password_len = len(password1)
        if password_len > 20:
            raise forms.ValidationError("Invalid password, 20 characters exceeded")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("password does not match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError("Email already exists")
        return email

    

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["designation"].error_messages = {
            "required": "This field is required"
        }


class UpdateUserForm(forms.ModelForm):
    password1 = forms.CharField(required=False)
    password2 = forms.CharField(required=False)
    id_number = forms.CharField(required=False)
    phone = forms.CharField(
        max_length=50,
        required=True,
        error_messages={"required": "Please enter phone number!"},
    )
    full_name = forms.CharField(
        max_length=50,
        required=True,
        error_messages={"required": "Please enter your name!"},
    )

    dob = forms.DateField(required=True)
    class Meta:
        model = UserProfile
        fields = [
            "email",
            "full_name",
            "designation",
            "phone",
            "dob",
            "identification",
            "id_number",
            "password1",
            "image",
            "password2",
            "username",
        ]
        widgets = {"dob": DateInput, "date_joined": DateInput, "leave_date": DateInput}


class EmployeeForm(forms.ModelForm):
    # leave_date = forms.DateField(required=True)
    permanent_address = forms.CharField(
        max_length=150,
        required=True,
        error_messages={"required": "Please enter your permanent address!"},
    )
    designation = forms.CharField(
        max_length=150,
        required=True,
        error_messages={"required": "Please enter your  designation!"},
    )
    class Meta:
        model = EmployeeProfile
        fields = [
            "email",
            "username",
            "full_name",
            "designation",
            "phone",
            "image",
            "date_joined",
            "is_transferred",
            "is_projecthead",
            "none",
            "leave_date",
            "temporary_address",
            "permanent_address"
        ]
        
# class="form-control bsa-input nepali-datepickers ndp-nepali-calendar"

    def clean(self):
        data = self.cleaned_data
        date_joined = data["date_joined"]
        leave_date = data["leave_date"]
        if date_joined and leave_date:
            if leave_date < date_joined:
                raise forms.ValidationError("Leave date should not be less than joined date.Please enter it again")
        return data
    
    def clean_email(self):
        email = self.cleaned_data["email"]
        if self.instance.email:
            if EmployeeProfile.objects.filter(email=email).exclude(email=self.instance.email).exists():
                raise forms.ValidationError("Email already exists")

        else:
            if EmployeeProfile.objects.filter(email=email).exists():
                raise forms.ValidationError("Email already exists")
        return email

class ResetPasswordForm(PasswordChangeForm):
    """
    password reset form
    """

    class Meta:
        fields = ("new_password1", "new_password2", "old_password")
        model = User
        help_texts = {"old_password": "", "new_password1": "", "new_password2": ""}


class SuperUserForm(forms.ModelForm):
    full_name = forms.CharField(required=False)
    email = forms.CharField(required=False)

    class Meta:
        model = UserProfile
        fields = ("full_name", "email", "designation", "image")



class UserPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput()
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput()
    )