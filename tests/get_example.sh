#!/bin/bash

curl -o $0.json 'https://services.arcgis.com/JJzESW51TqeY9uat/arcgis/rest/services/SSSI_England/FeatureServer/0/query?where=OBJECTID%3D3072&outFields=OBJECTID,SSSI_NAME,GIS_FILE&outSR=4326&f=json'
