from enum import Enum


class ControllerEvent:
    """
    Event class that needs to be send when a controller input has been received
    """
    def __init__(self, event_type, event, value=0):
        """
        Initialises the Controller event
        @param event_type: type of input
        @param event: the input
        @param value: possible value
        """
        self.type = event_type.name
        self.event = event.name
        self.value = value

    def to_json(self):
        """
        Function to convert Event to JSON format
        @return: Event class in JSON format
        """
        return {
            "type": self.type,
            "event": self.event,
            "value": self.value
        }


class InputType(Enum):
    """
    Enum for Input types
    @BUTTON_PRESSED: Button is pressed
    @JOYSTICK_MOVED: Joystick has been moved (can either be Left or Right joystick)
    @HAT_PRESSED: arrow key is pressed
    """
    BUTTON_PRESSED = 0
    JOYSTICK_MOVED = 1
    HAT_PRESSED = 2


class JoyStick(Enum):
    """
    Different types of joystick movement
    @LEFT_JOY_X: left joystick is moved over the x-axis
    @LEFT_JOY_Y: left joystick is moved over the y-axis
    @RIGHT_JOY_X: right joystick is moved over the x-axis
    @RIGHT_JOY_Y: right joystick is moved over the y-axis
    """
    LEFT_JOY_X = 0
    LEFT_JOY_Y = 1
    RIGHT_JOY_X = 2
    RIGHT_JOY_Y = 3


class Hat(Enum):
    """
    Arrow key press locations
    @DOWN: down key is pressed
    @UP: up key is pressed
    @LEFT: left key is pressed
    @RIGHT: right key is pressed
    """
    DOWN = (0, -1)
    UP = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    NONE = (0, 0)
    UP_RIGHT = (1, 1)
    UP_LEFT = (-1, 1)
    DOWN_RIGHT = (1, -1)
    DOWN_LEFT = (-1, -1)


class Buttons(Enum):
    """
    buttons that can be pressed
    """
    Y = 3
    B = 1
    A = 0
    X = 2
    L1 = 4
    R1 = 5
    L2 = 6
    R2 = 7
    SELECT = 8
    START = 9
    L3 = 10
    R3 = 11,
    HOME = 12
