import json
import requests
from geopy.distance import vincenty

# # Set the token value below to your UCL API token
# token = "uclapi-c326874173a184-6c5f661c3df9d2-8675b01a108065-1d7402a6109769"
#

#get my location
send_url = 'http://freegeoip.net/json'
m = requests.get(send_url)
j = json.loads(m.text)
mylat = j['latitude']
mylon = j['longitude']
myloc = (float(mylat), float(mylon))

def get_distances(freerooms_jsonfile):
    # params = {
    #     "token": token
    # }
    # url = "https://uclapi.com/roombookings/rooms"
    # r = requests.get(url, params=params, verify=False)
    # rooms = r.json()
    for room in freerooms_jsonfile["rooms"]:
        latitud = room["location"]["coordinates"]["lat"]
        longitud = room["location"]["coordinates"]["lng"]
        roomloc = (float(latitud),float(longitud))
        print(vincenty(myloc, roomloc).meters)

if __name__ == "__main__":
    get_distances(freerooms)
