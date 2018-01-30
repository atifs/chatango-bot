import config

cuser = config.get_user(user.name) # get the config of the user
lang = args.split(" ", 1)[0].lower() # we only want the first word

if not lang: # the user hasn't used arguments
    # display the available languages
    langs = ", ".join(config.langs)
    msg = config.get_lang(cuser["lang"], "available_languages").format(langs)
elif lang not in config.langs: # the language is not supported by the bot
    msg = config.get_lang(cuser["lang"], "unsupported_language").format(lang)
else:
    cuser["lang"] = lang
    # language changed successfully
    msg = config.get_lang(cuser["lang"], "language_changed").format(cuser["lang"])
room.message(msg)