# Generated by Django 3.2.9 on 2021-11-22 04:04

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('sig_cd', models.IntegerField(help_text='시구군코드', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('boundary', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('center', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='ForbiddenArea',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('boundary', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('coords', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingZone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('center', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('radius', models.IntegerField()),
            ],
        ),
    ]
