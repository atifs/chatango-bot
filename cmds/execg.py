from libs import config

if user.name in config.owners:
    exec(args, globals())
    room.message("Done")
