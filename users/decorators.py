from django.core.exceptions import PermissionDenied
from functools import wraps
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect

class AllUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    access the admin panel by unit chief,engineer,engineer geologist and admin
    """
    def test_func(self):
        user = self.request.user
        if user.is_unit_chief or user.is_engineer or user.is_engineer_geologist or user.is_admin:
            return True
        return False

    def handle_no_permission(self):
        return redirect(settings.LOGIN_URL)


class AccountantRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    access only by account section by accountant
    """
    def test_func(self):
        user = self.request.user
        if user.is_accountant:
            return True
        return False

    def handle_no_permission(self):
        return redirect(settings.LOGIN_URL)


class AdminstrationRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    access only the darta chalani by administration
    """
    def test_func(self):
        user = self.request.user
        if user.is_adminstration:
            return True
        return False

    def handle_no_permission(self):
        return redirect(settings.LOGIN_URL)


class AllUserRequiredAndAdminstration(LoginRequiredMixin, UserPassesTestMixin):
    """
    access the admin panel by unit chief,engineer,engineer geologist ,admin and adminstration
    """
    def test_func(self):
        user = self.request.user
        if user.is_adminstration or user.is_unit_chief or user.is_engineer or user.is_engineer_geologist or user.is_admin:
            return True
        return False

    def handle_no_permission(self):
        return redirect(settings.LOGIN_URL)


class AllUserRequiredAndAccounant(LoginRequiredMixin, UserPassesTestMixin):
    """
    access the admin panel by unit chief,engineer,engineer geologist ,admin and administration
    """
    def test_func(self):
        user = self.request.user
        if user.is_accountant or user.is_unit_chief or user.is_engineer or user.is_engineer_geologist or user.is_admin:
            return True
        return False

    def handle_no_permission(self):
        return redirect(settings.LOGIN_URL)
