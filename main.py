from libs import bot, config



def main():
    config.load_all()
    my_bot = bot.Bot(config.auth["name"], config.auth["password"], False)
    for room in config.rooms:
        my_bot.joinRoom(room)
    try:
        my_bot.main()
    finally:
        config.save_all()

if __name__ == '__main__':
    main()
    input()