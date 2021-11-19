from django.db import models


class DistrictFee(models.Model):
    basic_fee = models.IntegerField()
    fee_per_min = models.IntegerField()
    district = models.OneToOneField("areas.District", on_delete=models.CASCADE)
