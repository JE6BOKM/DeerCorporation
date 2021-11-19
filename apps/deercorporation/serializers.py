from math import ceil

from geopy.distance import distance as geopy_distance
from rest_framework.serializers import ModelSerializer, SerializerMethodField

# from apps.areas.models import ForbiddenArea, ParkingZone
from apps.deercorporation.models import RideHistory
from apps.fees.models import DistrictFee


class RideHistroySerializer(ModelSerializer):

    district_fee = SerializerMethodField()
    in_district = SerializerMethodField()
    in_parkingzone = SerializerMethodField()
    over_district_fee = SerializerMethodField()

    class Meta:
        model = RideHistory
        fields = (
            "use_start_at",
            "use_end_at",
            "usage_time",
            "district_fee",
            "in_district",
            "over_district_fee",
            "in_parkingzone",
        )

    def get_district_fee(self, obj):
        district_fee = DistrictFee.objects.get(district=obj.use_deer.area)
        basic_fee = district_fee.basic_fee
        fee_per_min = district_fee.fee_per_min
        return (obj.usage_time - 10) * fee_per_min + basic_fee

    def get_in_district(self, obj):
        return obj.use_deer.area.district_boundary.contains(obj.end_point)

    def get_over_district_fee(self, obj):
        if obj.use_deer.area.district_boundary.contains(obj.end_point):
            return 0
        end_point = (obj.use_end_lat, obj.use_end_lng)
        center = (
            obj.use_deer.area.district_center.y,
            obj.use_deer.area.district_center.x,
        )
        distance = geopy_distance(end_point, center)
        district_fee = DistrictFee.objects.get(district=obj.use_deer.area)
        return ceil(distance.meters / 100) * district_fee.over_district_fee

    def get_in_parkingzone(self, obj):

        return False
