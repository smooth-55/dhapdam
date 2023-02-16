from django.contrib import admin

from .models import Contract, ContractProgress, ContractFeature,ContractDetail

# Register your models here.

admin.site.register(Contract)
admin.site.register(ContractProgress)
admin.site.register(ContractFeature)
admin.site.register(ContractDetail)
