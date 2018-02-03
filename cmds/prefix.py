import config

if user.name[0] not in ("#", "!"):
    cuser = config.get_user(user.name)
    if not args or not args.strip():
        room.message(config.get_lang(cuser["lang"], "current_prefix").format(cuser["prefix"]))
    else:
        new_prefix = args.split()[0]
        if len(new_prefix) > 5:
            room.message(config.get_lang(cuser["lang"], "prefix_too_long").format(new_prefix))
        elif new_prefix[0] == "_":
            room.message(config.get_lang(cuser["lang"], "invalid_prefix").format(new_prefix))
        else:
            cuser["prefix"] = new_prefix
            room.message(config.get_lang(cuser["lang"], "new_prefix").format(new_prefix))
else:
    room.message(config.get_lang("en", "not_for_anons"))