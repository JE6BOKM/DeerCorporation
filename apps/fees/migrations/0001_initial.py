# Generated by Django 3.2.9 on 2021-11-22 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingZoneDiscount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_rate', models.FloatField(default=0.3)),
                ('parkingzone', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='areas.parkingzone')),
            ],
        ),
        migrations.CreateModel(
            name='DistrictFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_fee', models.IntegerField()),
                ('fee_per_min', models.IntegerField()),
                ('over_district_fee', models.IntegerField(default=200)),
                ('district', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='areas.district')),
            ],
        ),
    ]
