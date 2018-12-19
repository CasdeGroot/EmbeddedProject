from EmbeddedProject.drivers.driver import Driver
import serial


class SensorDriver(Driver):
    def __init__(self, sensor_config):
        Driver.__init__(self, sensor_config)
        self.start_listening()

    def init_communicator(self, sensor_config):
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

            return ser
        except Exception as e:
            print("error opening port")

        return None

    def write(self, serialized_packet):
        # print("Wrote: " + serialized_packet)
        self.communicator.write(serialized_packet)

    def receive(self):
        serialized_packet = self.communicator.readline().strip().rstrip()
        print("Received: " + serialized_packet)
        return serialized_packet

