import os
import subprocess

from django.conf import settings
from django.contrib.gis.geos import Point
from django.contrib.gis.utils import LayerMapping
from django.core.management.base import BaseCommand

import requests

from apps.areas.models import District


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "-version", type=str, help="shp version i.e.202101", default="202101"
        )

    def handle(self, *args, **kwargs):
        self.stdout.write("Start laod sig")

        # download shp and insert data

        version = kwargs.get("version")
        file_name = f"SIG_{version}"

        url = f"http://www.gisdeveloper.co.kr/download/admin_shp/{file_name}.zip"  # TODO: get argument of version

        subprocess.run(["wget", url, "-P", settings.ROOT_DIR / "tmp"])
        subprocess.run(
            [
                "unzip",
                f"{settings.ROOT_DIR/'tmp'/file_name}",
                "-d",
                f"{settings.ROOT_DIR/'tmp'}",
            ]
        )

        sig_shp = settings.ROOT_DIR / "tmp" / "TL_SCCO_SIG.shp"

        district_mapping = {
            "sig_cd": "SIG_CD",
            "name": "SIG_KOR_NM",
            "boundary": "MULTIPOLYGON",
        }

        lm = LayerMapping(
            District, sig_shp, district_mapping, transform=False, encoding="cp949"
        )
        lm.save(strict=True, verbose=True)

        # Naver maps API
        NAVER_CLIENT_ID = os.environ.get("NAVER_CLIENT_ID", None)
        NAVER_CLIENT_SECRET = os.environ.get("NAVER_CLIENT_SECRET", None)
        if not NAVER_CLIENT_ID or not NAVER_CLIENT_SECRET:
            self.stdout.write("[ERROR] Naver authentication keys are missing")

        headers = {
            "X-NCP-APIGW-API-KEY-ID": NAVER_CLIENT_ID,
            "X-NCP-APIGW-API-KEY": NAVER_CLIENT_SECRET,
        }
        geocode_url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"
        reverse_geocode_url = (
            "https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc"
        )

        districts = District.objects.all()
        for district in districts:
            # get lon, lat with query
            resp = requests.get(
                url=geocode_url,
                headers=headers,
                params={
                    "query": district.name,
                },
                timeout=2,
            )
            resp_json = resp.json()
            addresses = resp_json["addresses"]
            lon, lat = addresses[0]["x"], addresses[0]["y"]  # 경도, 위도
            # get center coords with lon, lat
            resp = requests.get(
                url=reverse_geocode_url,
                headers=headers,
                params={
                    "coords": f"{lon},{lat}",
                    "orders": "legalcode",
                    "output": "json",
                },
                timeout=2,
            )
            resp_json = resp.json()
            area2 = resp_json["results"][0]["region"]["area2"]
            center_coords = area2["coords"]["center"]
            district.center = Point(center_coords["x"], center_coords["y"])
        District.objects.bulk_update(districts, ["center"])

        subprocess.run(["rm", "-rf", settings.ROOT_DIR / "tmp"])
        self.stdout.write("Finish load sig")
