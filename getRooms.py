import json
import requests
import threading
from datetime import datetime, timedelta

#methods for fetching all-rooms and booked-rooms using UCLAPI
token = "uclapi-b122f02364cceb-6ec34be674c766-69f4d9c4c6e139-647b11df6fcef4"

def fetch_all_rooms():
	#returns json of all rooms
    params = {
        "token": token,
    }
    url = "https://uclapi.com/roombookings/rooms"
    r = requests.get(url, params=params)
    all_rooms = r.json()
    return all_rooms

def fetch_booked_rooms():
	#fetches json struct of booked room from the current hour to the end of the hour
	time_now = datetime.now()
	start_datetime = time_now.strftime("%Y-%m-%d"+"T"+"%H"+":00:00+01:00")
	end_datetime = (time_now + timedelta(hours=1)).strftime("%Y-%m-%d"+"T"+"%H"+":00:00+00:00")
	params = {
		"token": token,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
    }
	url = "https://uclapi.com/roombookings/bookings"
	r = requests.get(url, params=params)
	booked_rooms = r.json()
	return booked_rooms
	# for room in booked_rooms["bookings"]:
	# 	print(room["start_time"])
	# 	print(room["roomid"])
	# 	print(room["roomname"])
		

	#print(booked_rooms)

def fetch_free_rooms(all_rooms, booked_rooms):
	# bookedrooms = 0
	# for room in all_rooms["rooms"]:
	# 	for bookedroom in booked_rooms["bookings"]:
	# 		if (room["roomname"] == bookedroom["roomname"]):
	# 			bookedrooms+=1
	free_rooms = {}
	for room1 in all_rooms["rooms"]:
		for room2 in booked_rooms["bookings"]:
			if room1["roomname"] == room2["roomname"]:
				continue
			else:
				free_rooms['location'] = []
				free_rooms['location'].append({
					'lat': room1["location"]["coordinates"]["lat"],
					'lng': room1["location"]["coordinates"]["lng"],
					})

	return free_rooms

if __name__ == "__main__":
	all_rooms = fetch_all_rooms()
	booked_rooms = fetch_booked_rooms()
	print(all_rooms)
	print(booked_rooms.keys())
	frees = fetch_free_rooms(all_rooms, booked_rooms)
	print(frees)