from . import ch
from .utils import event
import sys


ch.debug = True

class Bot(ch.RoomManager):
    @event
    def onInit(self):
        pass

    @event
    def onConnect(self, room):
        pass

    @event
    def onEventCalled(self, room, event, *args, **kwargs):
        pass

   
