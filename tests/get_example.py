#!/usr/bin/env python

import json

import requests

QUERY_URL = ('https://services.arcgis.com/JJzESW51TqeY9uat/arcgis/rest/'
             'services/SSSI_England/FeatureServer/0/query')
OUTFIELDS = ["OBJECTID", "SSSI_NAME", "SSSI_AREA", "EASTING", "NORTHING",
             "LATITUDE", "LONGITUDE", "REFERENCE", "STATUS", "GID", "ENSISID",
             "GIS_FILE", "AREA", "EASTING0", "NORTHING0", "GIS_DATE",
             "VERSION"]
def main():
    params = {"where": "OBJECTID=3072",
              "outFields": ",".join(OUTFIELDS),
              "outSR": "4326",
              "f": "json"}
    result = requests.get(QUERY_URL, params=params)
    json_string = json.dumps(result.json(), sort_keys=True, indent=4)
    with open("tmp/get_example.py.json", "w") as jsonfile:
        jsonfile.write(json_string)


if __name__ == "__main__":
    main()
