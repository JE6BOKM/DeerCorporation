from django.contrib.gis.db import models


class District(models.Model):

    district_id = models.CharField(max_length=30, primary_key=True)
    district_boundary = models.PolygonField()
    district_center = models.PointField()
    district_coords = models.MultiPointField()


class ParkingZone(models.Model):

    parkingzone_id = models.IntegerField(primary_key=True)
    parkingzone_center = models.PointField()
    parkingzone_radius = models.IntegerField()


class ForbiddenArea(models.Model):

    forbidden_area_id = models.IntegerField(primary_key=True)
    forbidden_area_boundary = models.PolygonField()
    forbidden_area_coords = models.MultiPointField()
