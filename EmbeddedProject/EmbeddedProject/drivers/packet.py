import json


class Packet:
    def __init__(self, command, handshake, options):
        self.command = command
        self.handshake = handshake
        self.options = options

    def to_json(self):
        packet = {
            "command": self.command.name,
            "handshake": self.handshake,
            "options": {}
        }
        for option in self.options:
            packet["options"][option] = self.options[option]

        return packet

    def serialize(self):
        packet = self.to_json()
        return bytearray(json.dumps(packet).encode("ascii"))