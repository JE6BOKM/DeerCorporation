import math

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class RideHistory(models.Model):

    use_start_at = models.DateTimeField()
    use_end_at = models.DateTimeField()
    use_end_lng = models.FloatField()
    use_end_lat = models.FloatField()
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    use_deer = models.ForeignKey("Deer", on_delete=models.SET_NULL, null=True)

    @property
    def usage_time(self):
        return math.ceil((self.use_end_at - self.use_start_at).seconds / 60)

    @property
    def end_point(self):
        return Point(self.use_end_lng, self.use_end_lat, srid=4326)


class Deer(models.Model):

    name = models.CharField(max_length=20, primary_key=True)
    area = models.ForeignKey("areas.District", on_delete=models.PROTECT)
