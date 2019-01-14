from SensorProject.managers.configmanager import ConfigManager
from SensorProject.Utils.argparser import get_args


def main():
    arg = get_args()
    ConfigManager(arg.config)

    while 1:
        pass


if __name__ == "__main__":
    main()
