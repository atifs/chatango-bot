from libs import config

if user.name in config.owners:
    room.message(repr(eval(args)))
