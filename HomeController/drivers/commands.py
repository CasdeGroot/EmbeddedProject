from enum import Enum


class Command(Enum):
    """
    Base commands for all drivers
    @HANDSHAKE: driver is trying to connect to other driver
    @EXIT: driver is exiting communication
    @OK: driver responses to command without needing to send a value
    @NONE: no action needed (filler for None functions)
    """
    HANDSHAKE = 1
    EXIT = 2
    OK = 3
    NONE = 4


class BlacklightCommand(Enum):
    """
    The blacklight commands
    @CAPTURE: capture one image
    @MULTI_CAPTURE: capture multiple images
    @CAPTURED: Response command if an image is captured correctly
    """
    HANDSHAKE = 1
    EXIT = 2
    OK = 3
    NONE = 4
    CAPTURE = 5
    MULTI_CAPTURE = 6
    CAPTURED = 7


class ControllerCommand(Enum):
    """
    Commands for the controller connection
    @CONTROLLER_INPUT: controller input has been received
    """
    HANDSHAKE = 1
    EXIT = 2
    PAUSE = 3
    OK = 4
    CONTROLLER_INPUT = 5
