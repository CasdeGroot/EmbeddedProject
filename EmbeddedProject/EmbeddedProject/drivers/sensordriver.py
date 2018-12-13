import serial
import json
import time
import threading


class SensorDriver:
    def __init__(self, sensor_config):
        self.commands = None
        self.connected = False
        self.serial = self.init_serial(sensor_config)
        self.handshake = False
        self.listening_thread = threading.Thread(target=self.listen)

    def init_serial(self, sensor_config):
        try:
            ser = serial.Serial(port=sensor_config['com_port'], baudrate=sensor_config['baud_rate'],
                                timeout=sensor_config['timeout'], writeTimeout=sensor_config['writeTimeout'])
            if not ser.isOpen():
                try:
                    ser.open()
                    self.connected = True
                except Exception as e:
                    print("error opening port" + str(e))
            else:
                self.connected = True

            ser.flushInput()
            ser.flushOutput()
        except Exception as e:
            print("error opening port")

        return None

    def send_command(self, command, options=dict()):
        packet = {
            "command": command.name,
            "handshake": self.handshake,
            "options": {}
        }
        for option in options:
            packet["options"][option] = options[option]

        print("Received: " + json.dumps(packet))
        if self.connected:
            self.serial.write(bytearray(json.dumps(packet).encode("ascii") + b"\r\n"))

    def receive_command(self):
        if self.connected:
            input = self.serial.readline().strip().rstrip()
            print(b"Sending:  " + input)
            try:
                packet = json.loads(input.decode("ascii"))
                if packet['command'] == self.commands.command.HANDSHAKE.name:
                    command = self.commands.get_command(command=packet["command"])
                    self.execute_command(command, options=packet["options"])
                    return

                if packet['handshake'] is False:
                    self.hand_shake()

                command = self.commands.get_command(command=packet["command"])
                self.execute_command(command, options=packet["options"])
            except Exception as e:
                print(e)
                return

    def execute_command(self, command, options):
        return command(options)

    def set_handler(self, handler):
        self.commands = handler

    def hand_shake(self):
        while not self.handshake:
            self.send_command(self.commands.command.HANDSHAKE)
            time.sleep(1)

    def listen(self):
        while True:
            self.receive_command()
            time.sleep(0.2)

    def start_listening(self):
        self.listening_thread.daemon = True
        self.listening_thread.start()

