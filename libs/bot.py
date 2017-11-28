from . import ch
from . import config

from .utils import event

import traceback
import html

PREFIX = "->"
if __import__("os").name == "posix":
    device = "Linux"
else:
    device = "Windows"
class Bot(ch.RoomManager):
    def onInit(self):
        print("Im {}, your bot... Running on {}, V-{}.\r".format(config.auth["name"], device, config.auth["ver"]))
        print(" ")
        
    def onConnect(self, room):
        print("Joining to "+room.name)
        
    def onMessage(self, room, user, message):
        print("[{}] <{}>: {}".format(room.name, user.name, message.body))
        if user == self.user: return

        if not message.body.strip(): return
        msgdata = message.body.split(" ",1)
        if len(msgdata) > 1:
            cmd, args = msgdata[0], msgdata[1]
        else:
            cmd, args = msgdata[0],""
            cmd = cmd.lower()

        

        if cmd[:len(PREFIX)] != PREFIX: return
        else: cmd = cmd[len(PREFIX):].lower()

        if cmd not in config.cmds: return

        try:
            exec(config.cmds[cmd])
        except BaseException as e:
            room.message(f'<f x{str(self.user.fontSize).rjust(2, "0")}F00="{self.user.fontFace}"><b>{e.__class__.__name__}</b>: <f x{str(self.user.fontSize).rjust(2, "0")}F00="8"><i>{html.escape(str(e))}</i>', channels=("red",), html=True)
