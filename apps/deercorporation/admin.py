from django.contrib import admin

from apps.deercorporation.models import Deer, RideHistory


@admin.register(Deer)
class DeerAdmin(admin.ModelAdmin):
    """"""

    list_display = (
        "name",
        "area",
    )


@admin.register(RideHistory)
class RideHistoryAdmin(admin.ModelAdmin):
    """"""

    list_display = (
        "id",
        "use_start_at",
        "use_end_at",
        "use_end_lat",
        "use_end_lng",
        "user",
        "use_deer",
        "usage_time",
        "end_point",
    )
