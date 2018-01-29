import json
import os
import sysr

rooms = []
auth  = {}
cmds  = {}

def load_auth():
    auth.clear()
    with open("config/auth.json") as file:
        auth.update(json.load(file))

def load_rooms():
    rooms.clear()
    with open("config/rooms.txt") as file:
        for line in file:
            rooms.extend(line.split())

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


def save_rooms(room_per_line):
    with open("config/rooms.txt", "w") as file:
        for i, room in enumerate(rooms):
            file.write(room)
            if (i + 1) % room_per_line == 0:
                file.write("\n")
            elif (i + 1) % room_per_line != room_per_line - 1:
                file.write(" ")

def load_all():
    load_auth()
    load_rooms()
    load_cmds()

def save_all():
    save_rooms(10)
