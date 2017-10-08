import json
import requests
import threading
from datetime import datetime, timedelta
from geopy.distance import vincenty
from operator import itemgetter
import io

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
    #return tuple of all items in all_rooms and not in booked_rooms
    q = []
    for k, v in all_rooms.items():
        if k not in booked_rooms:
            q += [(k, v["coordinates"])]
    return q


#get my location
send_url = 'http://freegeoip.net/json'
m = requests.get(send_url)
j = json.loads(m.text)
mylat = j['latitude']
mylon = j['longitude']
myloc = (float(mylat), float(mylon))
#print(myloc)

def get_distances(freerooms):
    #return list of distances in meters between myloc and free rooms
    distancearray = []
    for i in range (0, len(freerooms)-1):
        latitud = freerooms[i][1]["lat"]
        longitud = freerooms[i][1]["lng"]
        roomloc = (float(latitud),float(longitud))
        distancearray.append(vincenty(myloc, roomloc).meters)
    return distancearray

def nearest_rooms(freess):
    #return roomname, coordinates and distance of 5 closest rooms
    sorted_distance = sorted(freess, key=itemgetter(1))
    five_rooms = []
    for i in range(0,5):
        five_rooms.append(sorted_distance[i])
    return five_rooms

if __name__ == "__main__":
    all_rooms = fetch_all_rooms()
    booked_rooms = fetch_booked_rooms()
    frees = fetch_free_rooms(all_rooms, booked_rooms)
    # frees = [(room1, {lat: 1, lon 2}), (room2, {lat: 3, lon 4}), ...]
    distances = get_distances(frees)
    frees = zip(frees,distances)

    final_list = {"status": "ok",
                   "rooms": nearest_rooms(frees),
                }

<<<<<<< HEAD
    with io.open('data.txt', 'w', encoding='utf-8') as f:
        f.write(json.dumps(final_list, ensure_ascii=False))

=======
    with open('result.json', 'w') as fp:
        string = json.dumps(final_list)
        fp.write("{}".format(string))
>>>>>>> 4d1b9c9d33edab8a2a7b93e4c5310223942a0c6b
    #print(json.dumps(final_list))
    # for item in final_list:
    #     print(item)
