from django.contrib import admin

from apps.fees.models import DistrictFee


@admin.register(DistrictFee)
class DistrictFeeAdmin(admin.ModelAdmin):
    """"""
