from . import ch
from . import config

from .utils import event

import traceback
import html

PREFIX = "->" # you can also mention the bot instead of using the prefix

class Bot(ch.RoomManager):
    @event
    def onInit(self):
        pass
    
    @event
    def onConnect(self, room):
        pass
        
    @event
    def onMessage(self, room, user, message):
        if user == self.user: return

        if not message.body.strip(): return
        msgdata = message.body.split(" ",1)
        if len(msgdata) == 2:
            cmd, args = msgdata
        else:
            cmd, args = msgdata[0], ""
        cmd = cmd.lower()

        if cmd == "@" + self.user.name:
            msgdata = args.split(" ", 1)
            if len(msgdata) == 2:
                cmd, args = msgdata
            else:
                cmd, args = msgdata[0], ""

        elif cmd[:len(PREFIX)] == PREFIX:
            cmd = cmd[len(PREFIX):]
        else:
            return

        if cmd not in config.cmds:
            return

        try:
            exec(config.cmds[cmd])
        except BaseException as e:
            room.message(f'<f x{str(self.user.fontSize).rjust(2, "0")}F00="{self.user.fontFace}"><b>{e.__class__.__name__}</b>: <f x{str(self.user.fontSize).rjust(2, "0")}F00="8"><i>{html.escape(str(e))}</i>', channels=("red",), html=True)
