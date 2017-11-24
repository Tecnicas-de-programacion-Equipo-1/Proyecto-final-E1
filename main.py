from Views.MainView import MainView
from Models.WeatherManager import WeatherManager
import serial
from serial.tools import list_ports

class MainApp():
    def __init__(self):
        for port in list_ports.comports(include_links=True):
            print(port.device, port.name, port.description)

        self.__weather = WeatherManager.get_weather_data()
        #self.__weather_text  = self.__weather.information
        self.__master = MainView(action = self.__on_off, action_parking = self.__StatusParking)
        #self.__master = MainView(action=self.__on_off, weather_text=self.__weather_text,action_parking=self.__StatusParking)
        self.__arduino = serial.Serial('COM7', 115200)
        self.__master.protocol("WM_DELETE_WINDOW", self.__on_closing)

    def run(self):
        self.__master.mainloop()

    def __on_off(self, sender, pin, state):
        pin = str(pin).encode('ascii')
        self.__arduino.write(pin)

    def __StatusParking(self, pin, status):
        if status == True:
            pin = str(pin).encode("ascii")
            self.__arduino.write(pin)
        elif status == False:
            pin = 1
            pin = str(pin).encode("ascii")
            self.__arduino.write(pin)

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()


if __name__ == "__main__":
    app = MainApp()
    app.run()