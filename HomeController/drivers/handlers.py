from drivers import commands as cmds
from Utils import events


class CommandHandler(events.Sender):
    def __init__(self, sender):
        events.Sender.__init__(self)
        self.command_lookup = dict({
            cmds.Command.HANDSHAKE.name: self.handle_handshake,
            cmds.Command.EXIT.name: self.handle_exit,
            cmds.Command.OK.name: self.handle_OK,
            cmds.Command.NONE.name: self.handle_NONE
        })
        self.sender = sender

    def get_command(self, command):
        # print(command in self.command.__members__ and self.command[command].name in self.commands.keys())
        if command in cmds.Command.__members__ and cmds.Command[command].name in self.command_lookup.keys():
            # print(self.commands[self.command[command].name])
            return self.command_lookup[cmds.Command[command].name]

        return lambda: None

    def handle_handshake(self, options):
        if self.sender.handshake is False:
            self.sender.send_command(cmds.Command.HANDSHAKE)

        self.sender.handshake = True

    def handle_exit(self, options):
        return None

    def handle_OK(self, options):
        print("OK RECEIVED")

    def handle_NONE(self, options):
        return None


class BlacklightHandler(CommandHandler):
    def __init__(self, sender):
        CommandHandler.__init__(self, sender)

        self.command_lookup.update({
            cmds.BlacklightCommand.CAPTURED.name: self.handle_captured
        })

    def handle_captured(self, options):
        self.send_command(cmds.BlacklightCommand.CAPTURED, options=options)


class ControllerHandler(CommandHandler):
    def __init__(self, sender):
        CommandHandler.__init__(self, sender)




