import config

cuser = config.get_user(user.name)

room.message(config.get_lang(cuser["lang"], "hello").format(user.name.title()))