from main.command import CommandABC

class RemoteControlInvoker():
    def __init__(self):
        self._command = None

    def set_command(self, command: CommandABC):
        self._command = command

    def press_button(self):
        if self._command:
            self._command.execute()