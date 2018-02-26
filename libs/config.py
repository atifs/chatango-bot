import json
import os
import sys

rooms = [] # the list of rooms that the bot ´should´ be in
auth  = {}
cmds  = {}
langs = {}
owners = []
users = {}
rooms_config = {} # same as users, but for rooms

default_room = {}
default_user = {}

def load_default_user():
    default_user.clear()
    with open("config/default_user.json") as file:
        default_user.update(json.load(file))

def load_default_room():
    default_room.clear()
    with open("config/default_room.json") as file:
        default_room.update(json.load(file))

def load_auth():
    auth.clear()
    with open("config/auth.json") as file:
        auth.update(json.load(file))

def load_rooms():
    rooms.clear()
    with open("config/rooms.txt") as file:
        for line in file:
            rooms.extend(x.lower() for x in line.split())

def load_owners():
    owners.clear()
    with open("config/owners.txt") as file:
        for line in file:
            owners.extend(x.lower() for x in line.split())

def load_langs():
    langs.clear()
    for path in os.scandir("langs/"):
        lang = os.path.splitext(os.path.split(path.path)[1])[0]
        langs[lang] = {}
        with open(path.path, encoding = "utf-8") as file:
            for line in file:
                data = line.strip().split(" ", 1)
                if len(data) == 1 and data[0]:
                    raise ValueError("Invalid format")
                if data[0]:
                    id, text = data
                    langs[lang][id] = text

def load_cmds():
    cmds.clear()
    for path in os.listdir("cmds"):
        path = os.path.join("cmds", path)
        cmd = os.path.splitext(os.path.split(path)[1])[0]
        with open(path) as file:
            try:
                cmds[cmd] = compile(file.read(), path, "exec")
            except BaseException as e:
                ename = e.__class__.__name__
                eargs = str(e)
                msg = "Error loading cmd {}.\n\t{}: {}"
                msg = msg.format(cmd, ename, eargs)
                print(msg, file = sys.stderr)

def load_rooms_config():
    rooms_config.clear()
    for path in os.scandir("rooms/"):
        name = os.path.splitext(os.path.split(path.path)[1])[0].lower()
        with open(path.path, encoding = "utf-8") as file:
            rooms_config[name] = json.load(file)

def load_users():
    users.clear()
    for path in os.scandir("users/"):
        name = os.path.splitext(os.path.split(path.path)[1])[0].lower()
        with open(path.path, encoding = "utf-8") as file:
            users[name] = json.load(file)

def save_auth():
    with open("config/auth.json", "w") as file:
        json.dump(auth, file)

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

def save_users():
    for name, val in users.items():
        path = os.path.join("users", name + ".json")
        with open(path, "w", encoding = "utf-8") as file:
            json.dump(val, file)

def save_rooms_config():
    for name, val in rooms.config.items():
        path = os.path.join("rooms", name + ".json")
        with open(path, "w", encoding = "utf-8") as file:
            json.dump(val, file)

def load_all():
    load_auth()
    load_rooms()
    load_langs()
    load_owners()
    load_cmds()
    load_default_user()
    load_users()
    load_default_room()
    load_rooms_config()

def save_all():
    save_rooms(10)
    save_owners(10)
    save_auth()
    save_users()
    save_rooms_config()

def get_lang(lang, id):
    if lang in langs and id in langs[lang]:
        return langs[lang][id]
    return "langs[{}][{}]".format(repr(lang), repr(id))

def get_user(name):
    if name not in users:
        user = {"name": name}
        user.update(default_user)
        if name[0] not in "#!": # don't save anons
            users[name] = user
    else:
        for k, v in default_user.items():
            if k not in users[name]:
                users[name][k] = v
    return users[name]

def get_room(name):
    if name not in rooms_config:
        room = {"name": name}
        room.update(default_room)
        rooms_config[name] = room
    else:
        for k, v in default_room.items():
            if k not in rooms_config[name]:
                rooms_config[name][k] = v
    return rooms_config[name]


