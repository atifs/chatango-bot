import json
import os
import sys

rooms = []
auth  = {}
cmds  = {}
langs = {}
owners = []
users = {}

users_default = {"lang": "en"}


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
                if data[0]
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
                ename = e.__class.__.__name__
                eargs = str(e)
                msg = "Error loading cmd {}.\n\t{}: {}"
                msg = msg.format(cmd, ename, eargs)
                print(msg, file = sys.stderr)

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
        with open(os.path.join("users", name + ".json"), "w", encoding = "utf-8") as file:
            json.dump(val, file)


def load_all():
    load_auth()
    load_rooms()
    load_langs()
    load_owners()
    load_cmds()
    load_users()

def save_all():
    save_rooms(10)
    save_owners(10)
    save_auth()
    save_users()

def get_lang(lang, id):
    if lang in langs and id in langs[lang]:
        return langs[lang][id]
    return "langs[{}][{}]".format(repr(lang), repr(id))



def get_user(name):
    if name not in users:
        user = {"name": name}
        user.update(users_default)
        users[name] = user
    return users[name]
