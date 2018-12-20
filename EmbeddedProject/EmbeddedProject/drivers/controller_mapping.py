from enum import Enum


class Event:
    def __init__(self, event_type, event, value=0):
        self.type = event_type.name
        self.event = event.name
        self.value = value

    def to_json(self):
        return {
            "type": self.type,
            "event": self.event,
            "value": self.value
        }


class EventType(Enum):
    BUTTON_PRESSED = 0
    JOYSTICK_MOVED = 1
    HAT_PRESSED = 2


class JoyStick(Enum):
    LEFT_JOY_X = 0
    LEFT_JOY_Y = 1
    RIGHT_JOY_X = 2
    RIGHT_JOY_Y = 3


class Hat(Enum):
    DOWN = (0, -1)
    UP = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class Buttons(Enum):
    Y = 0
    B = 1
    A = 2
    X = 3
    L1 = 4
    R1 = 5
    L2 = 6
    R2 = 7
    SELECT = 8
    START = 9
    L3 = 10
    R3 = 11,
    HOME = 12