import pygame
import threading
from time import sleep
from drivers.commands import EthernetCommand
from drivers.controller_mapping import Event, EventType, JoyStick, Buttons, Hat


class ControllerReader:
    def __init__(self, networkdriver):
        self.driver = networkdriver
        self.joystick = self.init_joystick()
        (self.axes, self.buttons, self.hats) = self.init_buttons()
        self.read = False
        self.reading_thread = threading.Thread(target=self.read_input)

    @staticmethod
    def init_joystick():
        pygame.init()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        return joystick

    def init_buttons(self):
        axes = self.joystick.get_numaxes()
        buttons = self.joystick.get_numbuttons()
        hats = self.joystick.get_numhats()
        return axes, buttons, hats

    def get_axis(self, number):
        # when nothing is moved on an axis, the VALUE IS NOT EXACTLY ZERO
        # so this is used not "if joystick value not zero"
        value = self.joystick.get_axis(number)
        if value < -0.1 or value > 0.1:
            # value between 1.0 and -1.0
            print("Axis value is %s" % (value))
            print("Axis ID is %s" % (number))

            options = Event(EventType.JOYSTICK_MOVED, JoyStick(number), value).to_json()
            self.driver.send_command(EthernetCommand.CONTROLLER_INPUT, options)

    def get_button(self, number):
        # returns 1 or 0 - pressed or not
        button = self.joystick.get_button(number)
        if button:
            # just prints id of button
            print("Button ID is %s" % (number))
            options = Event(EventType.BUTTON_PRESSED, Buttons(number)).to_json()
            self.driver.send_command(EthernetCommand.CONTROLLER_INPUT, options)

    def get_hat(self, number):
        hat = self.joystick.get_hat(number)
        if hat != (0, 0):
            # returns tuple with values either 1, 0 or -1
            print("Hat value is %s, %s" % (hat[0], hat[1]))
            print("Hat ID is %s" % number)
            options = Event(EventType.HAT_PRESSED, Hat(hat)).to_json()
            self.driver.send_command(EthernetCommand.CONTROLLER_INPUT, options)

    def read_input(self):
        while self.read:
            for event in pygame.event.get():
                # loop through events, if window shut down, quit program
                if event.type == pygame.QUIT:
                    pygame.quit()
            if self.axes != 0:
                for i in range(self.axes):
                    self.get_axis(i)
            if self.buttons != 0:
                for i in range(self.buttons):
                    self.get_button(i)
            if self.hats != 0:
                for i in range(self.hats):
                    self.get_hat(i)
            sleep(0.5)

    def start_reading(self):
        self.read = True
        self.reading_thread.daemon = True
        self.reading_thread.start()

    def stop_reading(self):
        self.read = False


if __name__ == "__main__":
    controller = ControllerReader()
    controller.start_reading()

    while True:
        print(len(controller.events))
