from . import ch
from .utils import event
import traceback
import html
ch.debug = True

class Bot(ch.RoomManager):
    @event
    def onInit(self):
        pass

    @event
    def onConnect(self, room):
        print(f"Connected to {room.name}")
        #room.message("<i>test</i>", channels = ("red", "blue"), html = True)

    @event
    def onMessage(self, room, user, message):
        if user == self.user:
            return
        if message.body.startswith("->"):
            cmd, *args = message.body[2:].split()
        else:
            return

        if user.name == "theclonerx" and cmd == "eval":
            try:
                room.message(repr(eval(" ".join(args))))
            except BaseException as e:
                room.message(f'<f x14F00="8"><b>{e.__class__.__name__}</b>: <i>{html.escape(str(e))}</i>', channels=("red",), html=True)

    # @event
    # def onEventCalled(self, room, event, *args, **kwargs):
    #     pass

   
