from Views.MainView import MainView
from Models.WeatherManager import WeatherManager
import serial
from serial.tools import list_ports

class MainApp():
    def __init__(self):
        for port in list_ports.comports(include_links=True):
            print(port.device, port.name, port.description)
        self.__weather = WeatherManager.get_weather_data()
        self.__weather_text  = self.__weather.information
        self.__master = MainView(action = self.__on_off, weather_text = self.__weather_text, action_parking = self.__on__off_parking)
        self.__arduino = serial.Serial('COM5', 115200)
        self.__master.protocol("WM_DELETE_WINDOW", self.__on_closing)
        self.__home_temperature()

    def run(self):
        self.__master.mainloop()

    def __on_off(self, sender, code, state):
        data = ("1" + code) if state else ("0" + code)
        data = str(data).encode('ascii')
        self.__arduino.write(data)

    def __on__off_parking(self, on_off, status):
        data = str(on_off).encode("ascii")
        self.__arduino.write(data)

    def __handle_data(self,data):

        clean_values = data.strip(' \n\r').split(",")
        temperature1 = clean_values[0]
        temperature2 = clean_values[1]
        print ("1:",temperature1)
        print ("2:",temperature2)

        # self.__master.update_bar(temperature1)
        # self.__master.update_text(temperature2)


    def __home_temperature(self):
        temperature_data = self.__arduino.readline().decode()
        self.__handle_data(temperature_data)
        self.__master.after(1, self.__home_temperature)

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.run()