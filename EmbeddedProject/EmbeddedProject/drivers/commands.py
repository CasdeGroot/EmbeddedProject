from enum import Enum


class Command(Enum):
    HANDSHAKE = 1,
    EXIT = 2,
    OK = 3,
    NONE = 4


class BlacklightCommand(Enum):
    HANDSHAKE = 1,
    EXIT = 2,
    OK = 3,
    NONE = 4,
    CAPTURE = 5,
    MULTI_CAPTURE = 6,
    SEND_VALUE = 7,
    GET_VALUE = 8


class EthernetCommand:
    HANDSHAKE = 1,
    EXIT = 2,
    PAUSE = 3,
    OK = 4,
    FORWARD  = 5,
    BACKWARD = 6,
    ROTATE_LEFT = 7,
    ROTATE_RIGHT = 8
