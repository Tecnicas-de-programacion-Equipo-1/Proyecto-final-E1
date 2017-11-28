from Views.MainView import MainView
from Models.WeatherManager import WeatherManager
from Views.DataArduino import DataArduino

class MainApp():
    def __init__(self):
        DataArduino.read_port(self)
        self.__weather = WeatherManager.get_weather_data()
        self.__weather_text  = self.__weather.information
        self.__master = MainView(action = self.__on_off, weather_text = self.__weather_text, action_parking = self.__on__off_parking)
        DataArduino.Arduino(self)
        self.__master.protocol("WM_DELETE_WINDOW", self.__on_closing)

    def run(self):
        self.__master.mainloop()

    def __on_off(self, sender, code, state):
        DataArduino.on_off(self,sender,code,state)

    def __on__off_parking(self, on_off, status):
        DataArduino.on__off_parking(self,on_off,status)

    def __on_closing(self):
        DataArduino.on_closing(self, self.__master)

if __name__ == "__main__":
    app = MainApp()
    app.run()