from Models.DataArduino import DataArduino
from Models.Weather import Weather

class Automatic_Control_Fans():

    def __inti(self,temp_one, temp_two):
        self.__temp_one = temp_one
        self.__temp_two = temp_two
        self.__out_side_temp = Weather.temperature()

    def compare(self):
        if self.__temp_one > self.__out_side_temp :
            DataArduino.on_off_fans(True,"fan_one")

        elif self.__temp_two > self.__out_side_temp:
            DataArduino.on_off_fans(True, "fan_two")


