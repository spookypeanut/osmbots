import osmapi

LAT_MIN = 51.82031
LAT_MAX = 51.82129
LONG_MIN = -0.23969
LONG_MAX = -0.23852

OUTER_COORDS = [(LAT_MIN, LONG_MIN),
                (LAT_MAX, LONG_MIN),
                (LAT_MAX, LONG_MAX),
                (LAT_MIN, LONG_MAX)]

# See the result here:
# https://master.apis.dev.openstreetmap.org/#map=17/51.82032/-0.23782
OSM_URL = "https://master.apis.dev.openstreetmap.org/"


def main():
    api = osmapi.OsmApi(api=OSM_URL, passwordfile="credentials.txt")
    api.ChangesetCreate({u"comment": u"Test of automated edit"})
    tags = {"name": "Test node", "natural": "peak"}
    print(api.NodeCreate({u"lon": LONG_MIN, u"lat": LAT_MIN, u"tag": tags}))
    nodes = []
    first = None
    for lat, lon in OUTER_COORDS:
        nodes.append(api.NodeCreate({"lon": lon, "lat": lat})["id"])
        if first is None:
            first = nodes[-1]
    nodes.append(first)
    tags = {"name": "Test way", "building": "yes"}
    api.WayCreate({"nd": nodes, "tag": tags})

    api.ChangesetClose()


if __name__ == "__main__":
    main()
