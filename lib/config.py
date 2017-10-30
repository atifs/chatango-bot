import json

rooms = []
auth  = {}

def load_all():
    load_auth()
    load_rooms()

def load_auth():
    global auth
    with open("config/auth.json") as file:
        for k, v in json.load(file).items():
            auth[k] = v

def load_rooms():
    global rooms
    with open("config/rooms.txt") as file:
        for line in file:
            for room in line.split():
                rooms.append(room)

def save_all():
    save_rooms(50)

def save_rooms(room_per_line):
    with open("config/rooms.txt") as file:
        for i, room in enumerate(rooms):
            if i % room_per_line == 0:
                file.write("\n")
            elif i % room_per_line == room_per_line - 1:
                file.write(room)
            else:
                file.write(room + " ")