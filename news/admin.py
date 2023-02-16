from django.contrib import admin
from .models import Category, News,RecentActivities,HomeNotice,Message

# Register your models here.

admin.site.register([Category, News,RecentActivities,HomeNotice,Message])
