from django.contrib import admin

from apps.deercorporation.models import Deer, RideHistory


@admin.register(Deer)
class DeerAdmin(admin.ModelAdmin):
    """"""


@admin.register(RideHistory)
class RideHistoryAdmin(admin.ModelAdmin):
    """"""
