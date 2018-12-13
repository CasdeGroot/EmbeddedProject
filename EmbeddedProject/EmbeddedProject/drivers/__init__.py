from EmbeddedProject.drivers import sensordriver as sensd
from EmbeddedProject.drivers import commands as cmds
from EmbeddedProject.drivers import handlers
import time


def read_config(path):
    import json
    with open(path) as json_file:
        return json.load(json_file)


if __name__ == "__main__":
    print("Started sensor driver")
    config = read_config("../embeddedproject.json")
    driver = sensd.SensorDriver(config['blacklight_sensor'])
    driver.set_handler(handlers.BlacklightHandler(driver))
    driver.start_listening()
    driver.hand_shake()

    while True:
        driver.send_command(cmds.BlacklightCommand.CAPTURE)
        time.sleep(10)
