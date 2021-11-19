import json

from django.contrib.gis.db import models


class District(models.Model):
    sig_cd = models.IntegerField(primary_key=True, help_text="시구군코드")
    name = models.CharField(max_length=30)
    boundary = models.MultiPolygonField()
    center = models.PointField(null=True)

    def __str__(self) -> str:
        return self.name

    @property
    def coords(self):
        obj = json.loads(self.boundary.geojson)
        coordinates = obj["coordinates"]
        return coordinates


class ParkingZone(models.Model):
    id = models.IntegerField(primary_key=True)
    center = models.PointField()
    radius = models.IntegerField()

    @property
    def parkingzone(self):
        return self.center.buffer(self.radius)


class ForbiddenArea(models.Model):
    id = models.IntegerField(primary_key=True)
    boundary = models.PolygonField()
    coords = models.MultiPointField()
