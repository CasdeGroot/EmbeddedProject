from EmbeddedProject.managers.configmanager import ConfigManager
from EmbeddedProject.Utils.argparser import get_args

def main():
    arg = get_args()
    config_manager = ConfigManager(arg.config)


if __name__ == "__main__":
    main()
