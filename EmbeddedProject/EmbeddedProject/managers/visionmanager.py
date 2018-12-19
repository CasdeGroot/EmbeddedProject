import glob

from EmbeddedProject.drivers import commands as cmds
from subprocess import call
from EmbeddedProject.Utils.events import Linker
from EmbeddedProject.drivers.handlers import CommandHandler
from EmbeddedProject.vision.spot_detector import SpotDetector


class VisionManager:
    def __init__(self, configmanager):
        self.handler = configmanager.drivers.get("blacklight", CommandHandler(self)).handler
        self.linker = Linker(self.handler, self.handle_command)
        self.spot_detector = SpotDetector(configmanager.config["vision"])

    def handle_command(self, command, options):
        print("handle command")
        if command is cmds.BlacklightCommand.CAPTURED:
            call(["/home/avans/Desktop/Projects/SmartTooling/EmbeddedProject/EmbeddedProject/managers/get_images.sh"])
            spot_detected = self.spot_detector.detect_spot()
            print("spot detected: " + str(spot_detected))
