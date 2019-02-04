import time

import pygame
import threading
from time import sleep
from drivers.commands import ControllerCommand
from drivers.controller_mapping import ControllerEvent, InputType, JoyStick, Buttons, Hat


class ControllerReader:
    """
    Reads the inputs of a controller and maps them based off controller_mapping module
    """
    def __init__(self, networkdriver):
        """
        Initialises the controller reader
        @param networkdriver: the driver that is needed to send read input through
        """
        self.driver = networkdriver
        self.joystick = self.init_joystick()
        (self.axes, self.buttons, self.hats) = self.init_buttons()
        self.read = False
        self.reading_thread = threading.Thread(target=self.read_input)
        self.past_axis = dict({0: 0, 1: 0, 2: 0, 3: 0})
        self.past_hat = (0, 0)

    @staticmethod
    def init_joystick():
        """
        Initialises the joystick reader
        @return: None
        """
        pygame.init()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        return joystick

    def init_buttons(self):
        """
        Gets the number of buttons, axes and hats
        @return: all the axes, buttons, hats
        """
        axes = self.joystick.get_numaxes()
        buttons = self.joystick.get_numbuttons()
        hats = self.joystick.get_numhats()
        return axes, buttons, hats

    def get_axis(self, number):
        """
        check if axis has been moved  and if moved send event via driver
        @param number: ID of joystick
        @return: None
        """

        # when nothing is moved on an axis, the VALUE IS NOT EXACTLY ZERO
        # so this is used not "if joystick value not zero"
        value = self.joystick.get_axis(number)

        if value < -0.1 or value > 0.1:
            if self.past_axis.get(number) == value:
                return
            # value between 1.0 and -1.0
            print("Axis value is %s" % value)
            print("Axis ID is %s" % number)

            self.past_axis.update({number: value})

            # send controller event through driver
            options = ControllerEvent(InputType.JOYSTICK_MOVED, JoyStick(number), value).to_json()
            return options

        return None

    def get_button(self, number):
        """
        Check if button is pressed and if pressed send event through driver
        @param number: ID of button
        @return: None
        """
        # returns 1 or 0 - pressed or not
        button = self.joystick.get_button(number)
        if button:
            # just prints id of button
            # print("Button ID is %s" % (number))

            # Send controller event through driver
            options = {
                "BUTTON": ControllerEvent(InputType.BUTTON_PRESSED, Buttons(number)).to_json()
            }
            self.driver.send_command(ControllerCommand.CONTROLLER_INPUT, options)

    def get_hat(self, number):
        """
        Check if hat is pressed and if pressed send event through driver
        @param number: ID of hat button
        @return: None
        """
        hat = self.joystick.get_hat(number)
        if hat != (0, 0):
            # returns tuple with values either 1, 0 or -1
        #print("Hat value is %s, %s" % (hat[0], hat[1]))
        #print("Hat ID is %s" % number)
            self.past_hat = hat
            options = {
                "HAT": ControllerEvent(InputType.HAT_PRESSED, Hat(hat)).to_json()
            }
            self.driver.send_command(ControllerCommand.CONTROLLER_INPUT, options)
        elif self.past_hat != (0, 0):
            print("Hat value is %s, %s" % (hat[0], hat[1]))
            print("Hat ID is %s" % number)
            self.past_hat = (0, 0)
            options = {
                "HAT": ControllerEvent(InputType.HAT_PRESSED, Hat(hat)).to_json()
            }
            self.driver.send_command(ControllerCommand.CONTROLLER_INPUT, options)

    def read_input(self):
        """
        Reads the input of the controller and handles the events triggered by the input
        @return:
        """
        while self.read:
            for event in pygame.event.get():
                # loop through events, if window shut down, quit program
                if event.type == pygame.QUIT:
                    pygame.quit()
            if self.axes != 0:
                options = {}
                for i in range(self.axes - 2):
                    option = self.get_axis(i)
                    if option != None:
                        options[JoyStick(i).name] = option

                if len(options) != 0:
                    if JoyStick.LEFT_JOY_X.name not in options:
                        options[JoyStick.LEFT_JOY_X.name] = ControllerEvent(InputType.JOYSTICK_MOVED ,JoyStick.LEFT_JOY_X, 0).to_json()
                    if JoyStick.LEFT_JOY_Y.name not in options:
                        options[JoyStick.LEFT_JOY_Y.name] = ControllerEvent(InputType.JOYSTICK_MOVED, JoyStick.LEFT_JOY_Y, 0).to_json()
                    self.driver.send_command(ControllerCommand.CONTROLLER_INPUT, options)

            if self.buttons != 0:
                for i in range(self.buttons):
                    self.get_button(i)
            if self.hats != 0:
                for i in range(self.hats):
                    self.get_hat(i)
            sleep(0.2)

    def start_reading(self):
        """
        Start the thread that is reading the input of the controller
        @return: None
        """
        self.read = True
        self.reading_thread.daemon = True
        self.reading_thread.start()

    def stop_reading(self):
        """
        Stop reading controller input
        @return:
        """
        self.read = False


if __name__ == "__main__":
    controller = ControllerReader()
    controller.start_reading()

    while True:
        print(len(controller.events))
