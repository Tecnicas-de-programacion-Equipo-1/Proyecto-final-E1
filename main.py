from Views.MainView import MainView
from Models.WeatherManager import WeatherManager
import serial
from serial.tools import list_ports

class MainApp():
    def __init__(self):
        for port in list_ports.comports(include_links=True):
            print(port.device, port.name, port.description)

        self.__master = MainView(action = self.__on_off)
        self.__arduino = serial.Serial('COM3', 115200)
        self.__master.protocol("WM_DELETE_WINDOW", self.__on_closing)

    def run(self):
        self.__weather = WeatherManager.get_weather_data()
        self.__master.mainloop()

    def __on_off(self, sender, pin, state):
        pin = str(pin).encode('ascii')
        self.__arduino.write(pin)

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()


if __name__ == "__main__":
    app = MainApp()
    app.run()