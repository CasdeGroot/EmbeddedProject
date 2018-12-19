from EmbeddedProject.Utils.factory import create
from EmbeddedProject.Utils.utils import get_attribute


class ConfigManager:
    def __init__(self, path):
        self.config = self.read_config(path)
        self.drivers = self.init_drivers(get_attribute("drivers", self.config))

    def init_drivers(self, drivers_config):
        drivers = dict()
        for name in drivers_config:
            conf = get_attribute(name, drivers_config)
            self.init_driver(conf, name, drivers)

        return drivers

    @staticmethod
    def init_driver(driver_config, name, drivers):
        if(get_attribute("enable", driver_config)) is True:
            driver = create(get_attribute("driver", driver_config))(driver_config)

            if driver is not None:
                handler = create(get_attribute("handler", driver_config))
                if handler is not None:
                    driver.set_handler(handler(driver))
                    drivers.update({name: driver})
                else:
                    print("handler not found: " + get_attribute("handler", driver_config))
            else:
                print("driver not found: " + get_attribute("driver", driver_config))

    @staticmethod
    def read_config(path):
        import json
        with open(path) as json_file:
            return json.load(json_file)
