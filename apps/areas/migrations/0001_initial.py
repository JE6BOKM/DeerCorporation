# Generated by Django 3.2.9 on 2021-11-19 08:52

import django.contrib.gis.db.models.fields
from django.db import migrations, models
from django.contrib.postgres.operations import CreateExtension


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        CreateExtension("postgis"),
        migrations.CreateModel(
            name="District",
            fields=[
                (
                    "district_id",
                    models.CharField(
                        max_length=30, primary_key=True, serialize=False
                    ),
                ),
                (
                    "district_boundary",
                    django.contrib.gis.db.models.fields.PolygonField(srid=4326),
                ),
                (
                    "district_center",
                    django.contrib.gis.db.models.fields.PointField(srid=4326),
                ),
                (
                    "district_coords",
                    django.contrib.gis.db.models.fields.MultiPointField(
                        srid=4326
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ForbiddenArea",
            fields=[
                (
                    "forbidden_area_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                (
                    "forbidden_area_boundary",
                    django.contrib.gis.db.models.fields.PolygonField(srid=4326),
                ),
                (
                    "forbidden_area_coords",
                    django.contrib.gis.db.models.fields.MultiPointField(
                        srid=4326
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ParkingZone",
            fields=[
                (
                    "parkingzone_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                (
                    "parkingzone_center",
                    django.contrib.gis.db.models.fields.PointField(srid=4326),
                ),
                ("parkingzone_radius", models.IntegerField()),
            ],
        ),
    ]
