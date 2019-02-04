from drivers import commands as cmds
from Utils import events


class CommandHandler(events.Sender):
    """
    Basic handler for basic command handling
    Mostly used as parent for implicit handlers
    """
    def __init__(self, driver):
        """
        initialses the command handler
        @param driver: the communicator
        """
        # initialise the handler as event sender
        events.Sender.__init__(self)
        # intialise the command lookup for command handling
        self.command_lookup = dict({
            cmds.Command.HANDSHAKE.name: self.handle_handshake,
            cmds.Command.EXIT.name: self.handle_exit,
            cmds.Command.OK.name: self.handle_OK,
            cmds.Command.NONE.name: self.handle_NONE
        })
        self.sender = driver

    def get_command(self, command):
        """
        get the function that is linked to a command in the command lookup
        @param command: the command (enum)
        @return: the function lambda or None if the function isn't found
        """
        if command in cmds.Command.__members__ and cmds.Command[command].name in self.command_lookup.keys():
            # print(self.commands[self.command[command].name])
            return self.command_lookup[cmds.Command[command].name]

        return lambda: None

    def handle_handshake(self, options):
        """
        handle handshake command by sending handshake command back and setting handshake as true
        @param options: in this case empty JSON, because no options are needed
        @return: None
        """
        if not self.sender.handshake:
            self.sender.send_command(cmds.Command.HANDSHAKE)

        self.sender.handshake = True

    def handle_exit(self, options):
        pass

    def handle_OK(self, options):
        pass

    def handle_NONE(self, options):
        pass


class BlacklightHandler(CommandHandler):
    """
    Handler for the communication with the blacklight sensor
    """
    def __init__(self, driver):
        """
        See CommandHandler doc for info
        @param driver:
        """
        CommandHandler.__init__(self, driver)

        self.command_lookup.update({
            cmds.BlacklightCommand.CAPTURED.name: self.handle_captured
        })

    def handle_captured(self, options):
        """
        Handle captured command by sending an event with the same command through to event listeners
        @param options: Options are an empty JSON in this case
        @return: None
        """
        self.send_command(cmds.BlacklightCommand.CAPTURED, options=options)


class ControllerHandler(CommandHandler):
    """
    Handler for handling commands send by the Embedded Project
    """
    def __init__(self, driver):
        CommandHandler.__init__(self, driver)




