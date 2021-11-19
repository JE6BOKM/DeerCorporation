from django.db import models


class DistrictFee(models.Model):
    basic_fee = models.IntegerField()
    fee_per_min = models.IntegerField()
    over_district_fee = models.IntegerField(default=200)
    district = models.OneToOneField("areas.District", on_delete=models.CASCADE)
