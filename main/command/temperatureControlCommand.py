from . import CommandABC
from main.receiver import ThermostatReceiver

class TemperatureControlCommand(CommandABC):
    def __init__(self, thermostat: ThermostatReceiver, temperature: float):
        self._thermostat = thermostat
        self._temperature = temperature

    def execute(self) -> None:
        self._thermostat.set_temperature(self._temperature)