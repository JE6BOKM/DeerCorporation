from django.contrib.gis.db import models


class RideHistory(models.Model):

    use_start_at = models.DateTimeField()
    use_end_at = models.DateTimeField()
    use_end_lat = models.DecimalField(max_digits=10, decimal_places=6)
    use_end_lng = models.DecimalField(max_digits=10, decimal_places=6)
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True)
    use_deer = models.ForeignKey("Deer", on_delete=models.SET_NULL, null=True)


class Deer(models.Model):

    name = models.CharField(max_length=20, primary_key=True)
    area = models.ForeignKey("areas.District", on_delete=models.PROTECT)
