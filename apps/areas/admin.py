from django.contrib.gis import admin

from apps.areas.models import District, ForbiddenArea, ParkingZone


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    """"""

    list_display = (
        "district_id",
        "district_boundary",
        "district_center",
        "district_coords",
    )


@admin.register(ParkingZone)
class ParkingZoneAdmin(admin.ModelAdmin):
    """"""

    list_display = (
        "parkingzone_id",
        "parkingzone_center",
        "parkingzone_radius",
    )


@admin.register(ForbiddenArea)
class ForbiddenAreaAdmin(admin.ModelAdmin):
    """"""

    list_display = (
        "forbidden_area_id",
        "forbidden_area_boundary",
        "forbidden_area_coords",
    )
