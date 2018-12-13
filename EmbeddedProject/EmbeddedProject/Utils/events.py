from events import Events


class Linker:
    def __init__(self, sender, receiver_function):
        sender.event.on_change += receiver_function


class Sender:
    def __init__(self):
        self.event = Events()

    def send_command(self, command, options):
        self.event.on_change(command, options)


if __name__ == "__main__":
    sender = Sender()
    sender.send_command("HANDSHAKE")
