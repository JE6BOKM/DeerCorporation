from django.contrib.gis import admin

from apps.areas.models import District, ForbiddenArea, ParkingZone


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass

    list_display = (
        "sig_cd",
        "name",
        "boundary",
        "center",
    )


@admin.register(ParkingZone)
class ParkingZoneAdmin(admin.ModelAdmin):
    pass

    list_display = (
        "id",
        "center",
        "radius",
    )


@admin.register(ForbiddenArea)
class ForbiddenAreaAdmin(admin.ModelAdmin):

    """"""

    list_display = (
        "id",
        "boundary",
        "coords",
    )
