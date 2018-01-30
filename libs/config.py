import json
import os
import sys

rooms = []
auth  = {}
cmds  = {}
owners = []

def load_auth():
    auth.clear()
    with open("config/auth.json") as file:
        auth.update(json.load(file))

def load_rooms():
    rooms.clear()
    with open("config/rooms.txt") as file:
        for line in file:
            rooms.extend(x.lower() for x in line.split())

def load_rooms():
    owners.clear()
    with open("config/owners.txt") as file:
        for line in file:
            owners.extend(x.lower() for x in line.split())


def load_cmds():
    cmds.clear()
    for path in os.listdir("cmds"):
        path = os.path.join("cmds", path)
        cmd = os.path.splitext(os.path.split(path)[1])[0]
        with open(path) as file:
            try:
                cmds[cmd] = compile(file.read(), path, "exec")
            except BaseException as e:
                print("Error loading cmd {}.\n\t{}: {}".format(cmd, e.__class.__.__name__, e), file = sys.stderr)

def save_auth():
    with open("config/auth.json", "w") as file:
        json.dump(file, auth)

def save_rooms(rooms_per_line):
    with open("config/rooms.txt", "w") as file:
        for i, room in enumerate(rooms):
            file.write(room)
            if (i + 1) % rooms_per_line == 0:
                file.write("\n")
            elif (i + 1) % rooms_per_line != rooms_per_line - 1:
                file.write(" ")

def save_owners(owners_per_line):
    with open("config/owners.txt", "w") as file:
        for i, owner in enumerate(owners):
            file.write(owner)
            if (i + 1) % owners_per_line == 0:
                file.write("\n")
            elif (i + 1) % owners_per_line != owners_per_line - 1:
                file.write(" ")


def load_all():
    load_auth()
    load_rooms()
    load_cmds()
    load_owners()

def save_all():
    save_rooms(10)
    save_owners(10)
    save_auth()
