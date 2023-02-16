from django.urls import path
from .views import (
    LoginView,
    register_view,
    logout_view,
    EmployeeDetailView,
    ExEmployeeView,
    ExProjectheadView,
    admin_profiles,
    ForgotPasswordView,
    ResetPasswordView,
    AdminProfileView,
    AdminProfileEditView,
    AdminImageEditView,
    change_password,
)
from django.contrib.auth import views as auth_views
from .views import (
    PasswordResetDoneView,
    PasswordResetView,
    PasswordResetConfirmView,
    UserPasswordResetConfirmView,
    redirect_view,
)


app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("redirect/user/", redirect_view, name="logout-user"),

    path("register/", register_view, name="register"),
    path("employee-detail/", EmployeeDetailView.as_view(), name="employee-detail"),
    path("ex-employee/", ExEmployeeView.as_view(), name="ex-employee"),
    path("ex-projecthead/", ExProjectheadView.as_view(), name="ex-projecthead"),
    # admin profile
    path("admin/profile/", AdminProfileView.as_view(), name="admin-profile"),
    path(
        "edit/profile/<int:pk>/",
        AdminProfileEditView.as_view(),
        name="admin-profile-edit",
    ),
    # path("edit/image/<int:pk>/", AdminImageEditView.as_view(), name="admin-image-edit"),
    # admin profile
    path("admin-profiles/", admin_profiles, name="admin-profile"),
    # change password
    path("change-password/", change_password, name="change_passwords"),
    # forgot password
    # 1st step
    path(
        "password-reset/",
        PasswordResetView.as_view(
            template_name="registration/forgot-password.html",
            subject_template_name="registration/forgot_password/password_reset_subject.txt",
            html_email_template_name="registration/forgot_password/password_reset_email.html"
            # success_url='/login/'
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    # path(
    #     "password-reset-confirm/<uidb64>/<token>/",
    #     PasswordResetConfirmView.as_view(
    #         template_name="registration/reset-password.html"
    #     ),
    #     name="password_reset_confirm",
    # ),
    path(
        "passwords-reset-confirm/<uidb64>/<token>/",
        UserPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="registration/login.html"
        ),
        name="password_reset_complete",
    ),
    path("forgot-password/", ForgotPasswordView.as_view(), name="forgot-password"),
    path("reset-password/", ResetPasswordView.as_view(), name="reset-password"),
]
