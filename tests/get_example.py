#!/usr/bin/env python

import requests
import json

params = {"where": "OBJECTID=3072",
          "outFields": "OBJECTID,SSSI_NAME,GIS_FILE",
          "outSR": "4326",
          "f": "json"}
url = 'https://services.arcgis.com/JJzESW51TqeY9uat/arcgis/rest/services/SSSI_England/FeatureServer/0/query'
r = requests.get(url, params=params)
json_string = json.dumps(r.json(), sort_keys=True, indent=4)
with open("tmp/get_example.py.json", "w") as f:

    f.write(json_string)
