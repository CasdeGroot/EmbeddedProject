from EmbeddedProject.Utils.events import Linker
from EmbeddedProject.drivers.controller_mapping import EventType


class MotionManager:
    def __init__(self, configmanager):
        self.handler = configmanager.drivers.get("controller").handler
        self.link = Linker(self.handler, self.handle_input)
        self.controller_event = dict({
            EventType.JOYSTICK_MOVED: self.handle_joystick,
            EventType.BUTTON_PRESSED: self.handle_button,
            EventType.HAT_PRESSED: self.handle_hat
        })

    def handle_input(self, command, event):
        handle_event = self.controller_event.get(EventType[event.type])
        handle_event(event)

    def handle_hat(self, event):
        print(event.type)
        pass

    def handle_joystick(self, event):
        print(event.type)
        pass

    def handle_button(self, event):
        print(event.type)
        pass

