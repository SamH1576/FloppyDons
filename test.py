import json
import requests
from geopy.distance import vincenty

# Set the token value below to your UCL API token
token = "uclapi-c326874173a184-6c5f661c3df9d2-8675b01a108065-1d7402a6109769"


def get_rooms():
    params = {
        "token": token
    }
    myloc = (51.5249193, -0.1332382)
    url = "https://uclapi.com/roombookings/rooms"
    r = requests.get(url, params=params, verify=False)
    rooms = r.json()
    for room in rooms["rooms"]:
        latitud = room["location"]["coordinates"]["lat"]
        longitud = room["location"]["coordinates"]["lng"]
        roomloc = (float(latitud),float(longitud))
        print(vincenty(myloc, roomloc).miles)

if __name__ == "__main__":
    get_rooms()
