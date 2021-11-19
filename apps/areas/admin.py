from django.contrib import admin

from apps.areas.models import District, ForbiddenArea, ParkingZone


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    pass


@admin.register(ParkingZone)
class ParkingZoneAdmin(admin.ModelAdmin):
    pass


@admin.register(ForbiddenArea)
class ForbiddenAreaAdmin(admin.ModelAdmin):
    pass
