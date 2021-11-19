from django.contrib.gis.db import models


class District(models.Model):

    district_id = models.CharField(max_length=30, primary_key=True)
    district_boundary = models.PolygonField(srid=4326)
    district_center = models.PointField(srid=4326)
    district_coords = models.MultiPointField(srid=4326)


class ParkingZone(models.Model):

    parkingzone_id = models.IntegerField(primary_key=True)
    parkingzone_center = models.PointField(srid=4326)
    parkingzone_radius = models.FloatField()

    @property
    def parkingzone(self):
        return self.parkingzone_center.buffer(self.parkingzone_radius)


class ForbiddenArea(models.Model):

    forbidden_area_id = models.IntegerField(primary_key=True)
    forbidden_area_boundary = models.PolygonField(srid=4326)
    forbidden_area_coords = models.MultiPointField(srid=4326)
