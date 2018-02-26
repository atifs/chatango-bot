import ch
import config

from utils import event

import html

# PREFIX = "->" # you can also mention the bot instead of using the prefix

class Bot(ch.RoomManager):
    @event
    def onInit(self):
        pass
    
    @event
    def onConnect(self, room):
        croom = config.get_room(room.name)
        room.channels = tuple(croom.channels)
        
    @event
    def onMessage(self, room, user, message):        if user == self.user: return

        if not message.body.strip(): return

        msgdata = message.body.strip().split(" ",1)

        if user.name not in config.users:
            PREFIX = config.default_user["prefix"]
        else:
            PREFIX = config.get_user(user.name)["prefix"]

        if len(msgdata) == 2:
            cmd, args = msgdata
        else:
            cmd, args = msgdata[0], ""

        if cmd == PREFIX:
            msgdata = args.split(" ",1)
            if len(msgdata) == 2:
                cmd, args = msgdata
            else:
                cmd, args = msgdata[0], ""
        elif cmd.lower() == "@" + self.user.name.replace("#", "").replace("!", ""):
            msgdata = args.split(" ", 1)
            if len(msgdata) == 2:
                cmd, args = msgdata
            else:
                cmd, args = msgdata[0], ""

        elif cmd[:len(PREFIX)] == PREFIX:
            cmd = cmd[len(PREFIX):]
        else:
            return

        cmd = cmd.lower().strip()

        if cmd not in config.cmds:
            return

        try:
            exec(config.cmds[cmd], locals())
        except BaseException as e:
            fsize = str(self.user.fontSize).rjust(2, "0")
            fcolor = self.user.fontColor
            etype = e.__class__.__name__
            eargs  = html.escape(str(e))
            msg = '<b>{}</b>: <f x{}{}="8"><i>{}</i>'
            msg = msg.format(etype, fsize, fcolor, eargs)
            traceback.print_exc()
            room.message(msg, html=True)
