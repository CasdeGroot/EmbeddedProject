import json
import time
import threading
import abc
from SensorProject.Utils.utils import get_attribute
from SensorProject.drivers.packet import Packet
from SensorProject.drivers.commands import Command


class Driver:
    def __init__(self, config):
        self.handler = None
        self.connected = False
        self.doListen = False
        self.handshake = False
        self.communicator = self.init_communicator(config)
        self.listening_thread = threading.Thread(target=self.listen)
        self.listening_thread.daemon = True
        self.handshake_thread = threading.Thread(target=self.hand_shake)
        self.handshake_thread.start()

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
        packet = Packet(command, self.handshake, options)
        if self.connected:
            self.write(bytearray(packet.serialize() + b"\r\n"))

    def receive_command(self):
        if self.connected:
            input = self.receive()
            self.parse_command(input)

    def parse_command(self, input):
        try:
            packet = json.loads(input.decode("ascii"))
            if packet['command'] == Command.HANDSHAKE.name:
                command = self.handler.get_command(command=get_attribute("command", packet))
                self.execute_command(command, options=get_attribute("options", packet))
                return

            if packet['handshake'] is False:
                return

            command = self.handler.get_command(command=get_attribute("command", packet))
            self.execute_command(command, options=get_attribute("options", packet))
        except Exception as e:
            print(e)
            return

    def execute_command(self, command, options):
        return command(options)

    def set_handler(self, handler):
        self.handler = handler

    def hand_shake(self):
        while not self.handshake:
            self.send_command(Command.HANDSHAKE)
            time.sleep(1)

    def listen(self):
        while self.doListen:
            self.receive_command()
            time.sleep(0.2)

    def start_listening(self):
        self.doListen = True
        self.listening_thread.start()

    def stop_listening(self):
        self.doListen = False
