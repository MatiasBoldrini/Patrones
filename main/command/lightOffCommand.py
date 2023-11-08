from . import CommandABC
from main.receiver import LightReceiver

class LightOffCommand(CommandABC):
    def __init__(self, light: LightReceiver) -> None:
        self._light = light

    def execute(self) -> None:
        self._light.turn_off()