from django.contrib import admin

from apps.fees.models import DistrictFee, ParkingZoneDiscount


@admin.register(DistrictFee)
class DistrictFeeAdmin(admin.ModelAdmin):
    """"""

    list_display = (
        "id",
        "basic_fee",
        "fee_per_min",
        "over_district_fee",
        "district",
    )


@admin.register(ParkingZoneDiscount)
class ParkingZoneDiscountAdmin(admin.ModelAdmin):
    """"""

    list_display = (
        "id",
        "discount_rate",
        "parkingzone",
    )
