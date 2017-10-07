import json
import requests
import threading
from datetime import datetime, timedelta
from geopy.distance import vincenty

#methods for fetching all-rooms and booked-rooms using UCLAPI
token = "uclapi-b122f02364cceb-6ec34be674c766-69f4d9c4c6e139-647b11df6fcef4"

def fetch_all_rooms():
    #returns json of all rooms
    params = {
        "token": token,
    }
    url = "https://uclapi.com/roombookings/rooms"
    r = requests.get(url, params=params)
    all_rooms = r.json()["rooms"]
    d = {}
    for r in all_rooms:
        d[r["roomname"]] = r["location"]
    return d

def fetch_booked_rooms():
    #fetches json struct of booked room from the current hour to the end of the hour
    time_now = datetime.now()
    start_datetime = time_now.strftime("%Y-%m-%d"+"T"+"%H"+":00:00+01:00")
    end_datetime = (time_now + timedelta(hours=100)).strftime("%Y-%m-%d"+"T"+"%H"+":00:00+00:00")
    params = {
        "token": token,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
    }
    url = "https://uclapi.com/roombookings/bookings"
    r = requests.get(url, params=params)
    resp = r.json()

    booked_rooms = []
#Results come in pages
    while resp["next_page_exists"]:
        booked_rooms += resp["bookings"]
        page_token = resp["page_token"]

        p = {"token": token, "page_token": page_token}
        resp = requests.get(url, params=p).json()

    booked_rooms += resp["bookings"]
    q = []
    for b in booked_rooms:
        q += [b["roomname"]]
    return set(q)

def fetch_free_rooms(all_rooms, booked_rooms):
    q = []
    for k, v in all_rooms.items():
        if k not in booked_rooms:
            q += [k, v["coordinates"]]
    return q


#get my location
send_url = 'http://freegeoip.net/json'
m = requests.get(send_url)
j = json.loads(m.text)
mylat = j['latitude']
mylon = j['longitude']
myloc = (float(mylat), float(mylon))

def get_distances(freerooms):
    # params = {
    #     "token": token
    # }
    # url = "https://uclapi.com/roombookings/rooms"
    # r = requests.get(url, params=params, verify=False)
    # rooms = r.json()
    for room in freerooms:
        latitud = room["location"]["coordinates"]["lat"]
        longitud = room["location"]["coordinates"]["lng"]
        roomloc = (float(latitud),float(longitud))
        print(vincenty(myloc, roomloc).meters)

if __name__ == "__main__":
    all_rooms = fetch_all_rooms()
    booked_rooms = fetch_booked_rooms()
    #print(len(booked_rooms))
    frees = fetch_free_rooms(all_rooms, booked_rooms)
    #for f in frees:
    #    pass
    print(frees)
    get_distances(frees)