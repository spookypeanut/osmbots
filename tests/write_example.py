import osmapi

LAT_MIN = 51.82031
LAT_MAX = 51.82129
LONG_MIN = -0.23969
LONG_MAX = -0.23852

OSM_URL = "https://master.apis.dev.openstreetmap.org/"


def get_credentials():
    """ Get credentials from a file in the current directory, in the form:

        username
        P4$$W0rD

    """
    with open("credentials.txt", "r") as cred_file:
        lines = cred_file.readlines()
        username = lines[0].strip()
        password = lines[1].strip()
    return {"username": username, "password": password}


def main():
    credentials = get_credentials()
    api = osmapi.OsmApi(api=OSM_URL, **credentials)
    api.ChangesetCreate({u"comment": u"Test of automated edit"})
    tags = {"name": "Test node", "natural": "peak"}
    print(api.NodeCreate({u"lon": LONG_MIN, u"lat": LAT_MIN, u"tag": tags}))
    api.ChangesetClose()


if __name__ == "__main__":
    main()
