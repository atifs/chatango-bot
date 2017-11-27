room.message(", ".join(__import__("os").path.splitext(x)[0] for x in __import__("os").listdir("cmds")))
