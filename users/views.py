from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.http import HttpResponse

from django.views.generic import TemplateView, FormView, UpdateView, View
from .models import UserProfile,EmployeeProfile

from .admin import UserCreationForm
from .forms import (
    LoginForm,
    RegisterForm,
    ResetPasswordForm,
    SuperUserForm,
    UserPasswordResetConfirmForm,
)
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetConfirmView

User = get_user_model()
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetView,
    PasswordResetCompleteView,
)

from users.decorators import (
    AllUserRequiredMixin,
    AccountantRequiredMixin,
    AdminstrationRequiredMixin
)

# Create your views here.

"""
Login View
"""


class LoginView(FormView):
    template_name = "administration/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        print("hshshshshsh@@@@@@@@@@@@")
        email = self.request.POST["email"]
        pword = self.request.POST["password"]
        print("email##############################", email)
        print("password", pword)

        user = authenticate(email=email, password=pword)

        if user is not None:
            print("**************************************",user.is_accountant)
            print("##########################",user.is_admin)

            login(self.request, user)
            if user.is_admin:
                return HttpResponseRedirect(reverse("company:admin-dashboard"))
            else:
                return HttpResponseRedirect(reverse("index"))
            # login(self.request, user)
        else:
            return render(
                self.request,
                self.template_name,
                {"error": "Invalid credential", "form": form},
            )
        return super().form_valid(form)


"""
Register View

"""


def register_view(request):
    context = {}
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

        else:
            return HttpResponse("Form is not valid")
    else:
        context["form"] = UserCreationForm
        return render(request, "registration/register.html", context)


"""
Logout View
"""


def logout_view(request):
    logout(request)
    return redirect("/")


"""
List of Employee
"""


class EmployeeDetailView(TemplateView):
    template_name = "aboutus/employee-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["employees"] = EmployeeProfile.objects.filter(is_transferred=False,is_projecthead=False)
        return context


"""
List of Ex-Employee
"""


class ExEmployeeView(TemplateView):
    template_name = "aboutus/ex-employee.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ex_employees"] = EmployeeProfile.objects.filter(is_transferred=True)
        return context


"""
List of Ex-Project heads
"""


class ExProjectheadView(TemplateView):
    template_name = "aboutus/ex-projecthead.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ex_projectheads"] = EmployeeProfile.objects.filter(is_projecthead=True)
        return context


def admin_profiles(request):
    """
    admin profile
    """
    try:
        single_superuser = UserProfile.objects.get(id=request.user.id,is_admin=True)
        print("single_superuser",single_superuser)

    except:
        single_superuser = None
    if request.method == "POST":
        print("get the password")
        form1 = ResetPasswordForm(request.user, request.POST)
        form_error = False

        if form1.is_valid():
            user = form1.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, "Your password was successfully updated!")
            return redirect("users:admin-profile")
        else:
            form_error = form1.errors
            context = {
                "form1": form1,
                "superusers": single_superuser,
            }
        # return render(request, "admin/password-test/change_password.html", context)
        return render(request, "admin/administration/admin-profile.html", context)

    else:

        context = {
            "form1": ResetPasswordForm(request.user),
            "superusers": single_superuser,
            "form_error": False,
        }
        # form = ResetPasswordForm(request.user)
        # return render(request, "admin/password-test/change_password.html", context)
        return render(request, "admin/administration/admin-profile.html", context)


def change_password(request):
    """
    set a new password
    """
    if request.method == "POST":
        print("get the password")
        form1 = ResetPasswordForm(request.user, request.POST)
        form_error = False

        if form1.is_valid():
            user = form1.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, "Your password was successfully updated!")
            return redirect("users:admin-profile")
        else:
            form_error = form1.errors
            context = {
                "form1": form1,
            }
        # return render(request, "admin/password-test/change_password.html", context)
        return render(request, "admin/administration/change-password.html", context)

    else:

        context = {
            "form1": ResetPasswordForm(request.user),
            "form_error": False,
        }
        # form = ResetPasswordForm(request.user)
        # return render(request, "admin/password-test/change_password.html", context)
        return render(request, "admin/administration/change-password.html", context)


class AdminProfileView(AllUserRequiredMixin,TemplateView):
    """
    Admin profile 
    """

    template_name = "admin/administration/admin-profile.html"
    form_class = None
    success_url = reverse_lazy("users:admin-profile")

    def post(self, request, *args, **kwargs):
        form1 = ResetPasswordForm(request.user, request.POST)
        if form1.is_valid():
            user = form1.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, "Your password was successfully updated!")
            return HttpResponseRedirect(reverse("users:admin-profile"))
            # save your model
            # redirect
        else:
            form_error = True
            messages.error(request, "Please correct the error below.")
            return HttpResponseRedirect(reverse("users:admin-profile"))

        return super(TemplateView, self).render_to_response(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        superuser = User.objects.filter(is_admin=True)
        print("superuser",superuser)
        single_superuser = superuser.reverse()[0]
        context["superusers"] = single_superuser
        context["form1"] = ResetPasswordForm(self.request.user)  # instance= None

        return context


class AdminProfileEditView(SuccessMessageMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = User
    form_class = SuperUserForm
    success_url = reverse_lazy("users:admin-profile")
    success_message = "Profile updated successfully"


class AdminImageEditView(SuccessMessageMixin,AllUserRequiredMixin, UpdateView):
    template_name = "admin/update.html"
    model = User
    fields = ["image"]
    success_url = reverse_lazy("users:admin-profile")
    success_message = "Image updated successfully"


"""=============================================
--------- forgot password section --------------
==============================================="""


class ForgotPasswordView(TemplateView):
    template_name = "registration/forgot-password.html"


class ResetPasswordView(TemplateView):
    template_name = "registration/reset-password.html"


"""=============================================
--------- password reset  --------------
==============================================="""


class PasswordResetDoneView(PasswordResetDoneView):
    template_name = "registration/forgot_password/password_reset_done.html"


class PasswordResetView(PasswordResetView):
    success_url = "/user/password-reset/done/"


def redirect_view(request):
    """
    logout user
    """
    logout(request)
    return redirect("/user/login/")


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = UserPasswordResetConfirmForm
    success_url = reverse_lazy("users:login")
    template_name = "registration/reset-password.html"
    success_url = "/user/redirect/user/"
