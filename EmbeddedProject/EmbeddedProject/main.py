from EmbeddedProject.drivers import commands
from EmbeddedProject.managers.configmanager import ConfigManager
from EmbeddedProject.Utils.argparser import get_args
import time

from EmbeddedProject.managers.motionmanager import MotionManager
from EmbeddedProject.managers.visionmanager import VisionManager


def main():
    arg = get_args()
    config_manager = ConfigManager(arg.config)
    # vision_manager = VisionManager(config_manager)
    motion_manager = MotionManager(config_manager)

    while 1:
        pass


if __name__ == "__main__":
    main()
