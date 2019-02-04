import json
import time
import threading
import abc
from Utils.utils import get_attribute
from drivers.packet import Packet
from drivers.commands import Command


class Driver:
    """
    Parent class for basic communication
    Driver can be initialised in different ways (for example Serial or Ethernet)
    """
    def __init__(self, config):
        """
        initialises the driver
        @param config: the configuration for the driver
        """
        # the event handler for event handling
        self.handler = None
        self.connected = False
        self.doListen = False
        self.handshake = False
        # the communicator for communication
        self.communicator = self.init_communicator(config)
        # thread for listening to incoming messages
        self.listening_thread = threading.Thread(target=self.listen)
        self.listening_thread.daemon = True
        # event to handshake with other communicator
        self.handshake_thread = threading.Thread(target=self.hand_shake)

    @abc.abstractmethod
    def init_communicator(self, config):
        """Initialise the communicator (Serial or UDP)"""

    @abc.abstractmethod
    def write(self, serialised_packet):
        """write a serialized packet"""

    @abc.abstractmethod
    def receive(self):
        """receive a serialized packet"""

    def send_command(self, command, options=dict()):
        """
        sends a command with possible options
        @param command: the command itself (Enum)
        @param options: Json with parameters that are needed by the event
        @return: None
        """
        packet = Packet(command, self.handshake, options)
        if self.connected and self.handshake is True or command.name is "HANDSHAKE":
            self.write(bytearray(packet.serialize() + b"\r\n"))

    def receive_command(self):
        """
        receive, parse and handle a message from communicator
        @return: None
        """
        if self.connected:
            input = self.receive()
            self.parse_command(input)

    def parse_command(self, input):
        """
        parses a raw message and handles the command in the message
        @param input: raw message from communicator
        @return: None
        """
        try:
            packet = json.loads(input.decode("ascii"))
            if packet['command'] == Command.HANDSHAKE.name and packet['handshake'] is False:
                command = self.handler.get_command(command=get_attribute("command", packet))
                self.execute_command(command, options=packet['handshake'])
                return

            if packet['handshake'] is False:
                return

            command = self.handler.get_command(command=get_attribute("command", packet))
            self.execute_command(command, options=get_attribute("options", packet))
        except Exception as e:
            print(e)
            return

    def execute_command(self, command, options):
        """
        executes the command lambda
        @param command: the function that needs to be executed
        @param options: the options given by the communicator
        @return:
        """
        return command(options)

    def set_handler(self, handler):
        """
        sets the command handler for incoming command handling
        @param handler: the handler that handles incoming commands
        @return: None
        """
        self.handler = handler

    def hand_shake(self):
        """
        Handshake with other communicator to initiate communication protocol
        @return: None
        """
        # while handshake hasn't been received -> send handshake command
        while not self.handshake:
            self.send_command(Command.HANDSHAKE)
            time.sleep(1)

    def listen(self):
        """
        listen to incoming commands from other commmunicator
        @return: None
        """
        while self.doListen:
            self.receive_command()
            time.sleep(0.2)

    def start_listening(self):
        """
        starts the listening thread
        @return: None
        """
        self.doListen = True
        self.listening_thread.start()

    def stop_listening(self):
        """
        stop listening to incoming commands
        @return:
        """
        self.doListen = False
