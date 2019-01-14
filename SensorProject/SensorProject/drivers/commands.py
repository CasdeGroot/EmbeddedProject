from enum import Enum


class Command(Enum):
    HANDSHAKE = 1
    EXIT = 2
    OK = 3
    NONE = 4


class BlacklightCommand(Enum):
    HANDSHAKE = 1
    EXIT = 2
    OK = 3
    NONE = 4
    CAPTURE = 5
    MULTI_CAPTURE = 6
    CAPTURED = 7

