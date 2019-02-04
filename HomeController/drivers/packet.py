import json


class Packet:
    """
    Packet that is used for communication
    """
    def __init__(self, command, handshake, options):
        """
        initialises the packet
        @param command: the command that needs to be executed
        @param handshake: indicates if communication has been initialised
        @param options: the parameters needed or asked by
        """
        self.command = command
        self.handshake = handshake
        self.options = options

    def to_json(self):
        """
        converts packet to json
        @return:
        """
        packet = {
            "command": self.command.name,
            "handshake": self.handshake,
            "options": {}
        }
        for option in self.options:
            packet["options"][option] = self.options[option]

        return packet

    def serialize(self):
        """
        converts packet to byte array
        @return:
        """
        packet = self.to_json()
        return bytearray(json.dumps(packet).encode("ascii"))