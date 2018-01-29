import os

room.message(", ".join(os.path.splitext(x)[0] for x in os.listdir("cmds")))
