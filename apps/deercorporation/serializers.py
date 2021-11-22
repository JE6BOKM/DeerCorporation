from math import ceil

from geopy.distance import distance as geopy_distance
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)

from apps.areas.models import ForbiddenArea, ParkingZone
from apps.deercorporation.models import RideHistory
from apps.fees.models import DistrictFee, ParkingZoneDiscount


class RideHistroySerializer(ModelSerializer):

    district_fee = SerializerMethodField()
    over_district_fee = SerializerMethodField()
    forbidden_penalty = SerializerMethodField()
    total_fee = SerializerMethodField()
    in_district = SerializerMethodField()
    in_parkingzone_discount = SerializerMethodField()
    in_forbidden_area = SerializerMethodField()

    class Meta:
        model = RideHistory
        fields = (
            "use_start_at",
            "use_end_at",
            "use_end_lng",
            "use_end_lat",
            "user",
            "use_deer",
            "usage_time",
            "in_district",
            "in_parkingzone_discount",
            "in_forbidden_area",
            "district_fee",
            "over_district_fee",
            "forbidden_penalty",
            "total_fee",
        )
        read_only_fields = (
            "user",
            "usage_time",
            "in_district",
            "in_parkingzone_discount",
            "in_forbidden_area",
            "district_fee",
            "over_district_fee",
            "forbidden_penalty",
            "total_fee",
        )

    def validate(self, attrs):
        start_at = attrs.get("use_start_at")
        end_at = attrs.get("use_end_at")
        end_lng = attrs.get("use_end_lng")
        end_lat = attrs.get("use_end_lat")
        if start_at >= end_at:
            raise ValidationError("End time cannot be less than start time.")
        if not 124 <= end_lng <= 132:
            raise ValidationError(
                "Longitude cannot be smaller than 124 and bigger than 132."
            )
        if not 33 <= end_lat <= 43:
            raise ValidationError(
                "Latitude cannot be smaller than 33 and bigger than 43."
            )
        return super().validate(attrs)

    def get_in_district(self, obj):
        return obj.use_deer.area.boundary.intersects(obj.end_point)

    def get_in_parkingzone_discount(self, obj):
        zones = ParkingZone.objects.all()
        zone = [zone for zone in zones if zone.parkingzone.intersects(obj.end_point)]
        if len(zone) == 1:
            discount_rate = ParkingZoneDiscount.objects.get(
                parkingzone=zone[0]
            ).discount_rate
            return discount_rate
        else:
            return 0

    def get_in_forbidden_area(self, obj):
        zones = ForbiddenArea.objects.filter(boundary__intersects=obj.end_point)
        if len(zones) == 1:
            return True
        else:
            return False

    def is_continuous_use(self, obj):
        last_use_end_at = (
            RideHistory.objects.filter(user=obj.user)
            .order_by("-use_start_at")
            .first()
            .use_end_at
        )
        if ceil((last_use_end_at - obj.use_start_at).seconds / 60) < 30:
            return True
        return False

    def get_district_fee(self, obj):
        district_fee = DistrictFee.objects.get(district=obj.use_deer.area)
        basic_fee = 0 if self.is_continuous_use(obj) else district_fee.basic_fee
        fee_per_min = district_fee.fee_per_min
        return (obj.usage_time - 10) * fee_per_min + basic_fee

    def get_over_district_fee(self, obj):
        if self.get_in_district(obj):
            return 0
        end_point = (obj.use_end_lat, obj.use_end_lng)
        center = (
            obj.use_deer.area.center.y,
            obj.use_deer.area.center.x,
        )
        distance = geopy_distance(end_point, center)
        district_fee = DistrictFee.objects.get(district=obj.use_deer.area)
        return ceil(distance.meters / 100) * district_fee.over_district_fee

    def get_forbidden_penalty(self, obj):
        return 6000

    def get_total_fee(self, obj):
        district_fee = self.get_district_fee(obj)
        total_fee = district_fee
        if not self.get_in_district(obj):
            total_fee += self.get_over_district_fee(obj)
        if self.get_in_parkingzone_discount(obj):
            total_fee *= 1 - self.get_in_parkingzone_discount(obj)
        if self.get_in_forbidden_area(obj):
            total_fee += self.get_forbidden_penalty(obj)
        return total_fee
