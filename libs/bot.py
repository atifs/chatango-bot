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
        pass
        
    @event
    def onMessage(self, room, user, message):
        cmd1 = False
        if user == self.user: return

        if not message.body.strip(): return

        msgdata = message.body.split(" ",1)

        if len(msgdata) == 2:
            cmd, args = msgdata
        else:
            cmd, args = msgdata[0], ""

        cmd = cmd.lower()
        if user.name[0] in ("#", "!") or user.name not in config.users:
            PREFIX = config.users_default["prefix"]
        else:
            PREFIX = config.get_user(user.name)["prefix"]
        if self.user.name[0] in ("#", "!"):
            self.anonfix = self.user.name[1:]
        else:
            self.anonfix = self.user.name
        if cmd == "@" + self.anonfix and args:
            cmd1 = True
            msgdata = args.split(" ", 1)
            if len(msgdata) > 1:
                cmd, args = msgdata[0], msgdata[1]
                cmd = cmd.lower()
            else:
                cmd, args = msgdata, ""
                cmd = cmd.lower()

        elif cmd[:len(PREFIX)] == PREFIX:
            cmd = cmd[len(PREFIX):]
        else:
            return
       
        if cmd not in config.cmds:
            return

        try:
            exec(config.cmds[cmd], locals())
        except BaseException as e:
            fsize = str(self.user.fontSize).rjust(2, "0")
            fface = self.user.fontFace
            etype = e.__class__.__name__
            eargs  = html.escape(str(e))
            msg = '<f x{}F00="{}"><b>{}</b>: <f x{}F00="8"><i>{}</i>'
            msg = msg.format(fsize, fface, etype, fsize, eargs)
            room.message(msg, channels=("red",), html=True)
