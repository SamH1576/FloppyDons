import json
import requests

# Set the token value below to your UCL API token
token = "uclapi-46e81733877226-cf21569aafe2bf-5703800fe32943-fe813629c8886a"

def get_rooms():
    params = {
        "token": token
    }
    url = "https://uclapi.com/roombookings/rooms"
    r = requests.get(url, params=params, verify=False)
    rooms = r.json()
    for room in rooms["rooms"]:
        room_data = "{} in {} has a capacity of {}".format(
            room["roomname"],
            room["sitename"],
            room["capacity"]
        )
        print(room_data)

if __name__ == "__main__":
    get_rooms()
