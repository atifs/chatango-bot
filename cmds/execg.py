import config

cuser = config.get_user(user.name)

if user.name in config.owners:
    exec(args, globals())
    room.message(config.get_lang(cuser["lang"], "done"))
