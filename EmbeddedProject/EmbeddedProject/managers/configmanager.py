from EmbeddedProject.drivers.sensordriver import SensorDriver
from EmbeddedProject.drivers.ethernetdriver import EthernetDriver
from EmbeddedProject.Utils.factory import create


class ConfigManager:
    def __init__(self, path):
        config = self.read_config(path)
        self.sensors = dict()
        self.networks = dict()
        self.init_sensors(config["sensors"])
        self.init_network(config["networking"])

    def init_sensors(self, sensor_config):
        for name in sensor_config:
            conf = sensor_config[name]
            sensor = SensorDriver(conf)
            handler = create(conf["handler"])
            if not handler is None:
                sensor.set_handler(handler(sensor))
            else:
                print("handler not found: " + conf["handler"])
            self.sensors.update({ name: sensor})

    def init_network(self, networking_config):
        for name in networking_config:
            conf = networking_config[name]
            driver = EthernetDriver(conf)
            self.networks.update({name: driver})

    @staticmethod
    def read_config(path):
        import json
        with open(path) as json_file:
            return json.load(json_file)
