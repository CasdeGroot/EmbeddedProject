from EmbeddedProject.managers.configmanager import ConfigManager
from EmbeddedProject.Utils.argparser import get_args
import time

def main():
    arg = get_args()
    config_manager = ConfigManager(arg.config)
    controller =  config_manager.drivers.get("controller")
    controller.start_listening()
    controller.hand_shake()


if __name__ == "__main__":
    main()
