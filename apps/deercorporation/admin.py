from django.contrib import admin

from apps.deercorporation.models import Area, Deer, RideHistory


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    """"""


@admin.register(Deer)
class DeerAdmin(admin.ModelAdmin):
    """"""


@admin.register(RideHistory)
class RideHistoryAdmin(admin.ModelAdmin):
    """"""
