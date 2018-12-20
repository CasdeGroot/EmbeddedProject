from drivers.controllerreader import ControllerReader
from managers.configmanager import ConfigManager
from Utils.argparser import get_args


def main():
    arg = get_args()
    config_manager = ConfigManager(arg.config)
    controller = config_manager.drivers.get("controller")
    reader = ControllerReader(controller)
    reader.start_reading()

    while 1:
        pass


if __name__ == "__main__":
    main()
