from main.command import *
from main.receiver import *
from main.invoker import *

class Cliente():

    def run(self):
        living_room_light = LightReceiver()
        thermostat = ThermostatReceiver()
        living_room_light_on = LightOnCommand(living_room_light)
        living_room_light_off = LightOffCommand(living_room_light)

        set_temperature = TemperatureControlCommand(thermostat, 23.0)

        remote = RemoteControlInvoker()

        remote.set_command(living_room_light_on)
        remote.press_button() 
        
        remote.set_command(living_room_light_off)
        remote.press_button()  

        remote.set_command(set_temperature)
        remote.press_button()  