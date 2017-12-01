from Models.DataArduino import DataArduino
from Models.WeatherManager import WeatherManager
from Views.MainView import MainView

class MainApp():
    class Constants:
        delete = "WM_DELETE_WINDOW"

    def __init__(self):
        self.__weather = WeatherManager.get_weather_data()
        self.__weather_text  = self.__weather.information
        self.__master = MainView(action = self.__on_off, weather_text = self.__weather_text, action_additional_buttons = self.__on__off_additional_buttons, fans_action = self.__on_off_fan)
        self.__Arduino = DataArduino()
        self.__master.protocol(self.Constants.delete, self.__on_closing)
        self.__MotionSensor()
        self.__Arduino.read_port()

    def run(self):
        self.__master.mainloop()

    def __MotionSensor(self):
        data = self.__Arduino.update_clock()
        self.__Arduino.handle_data(data)
        self.__master.after(1,self.__MotionSensor)

    def __on_off(self, sender, code, state):
        self.__Arduino.on_off(sender,code,state)

    def __on__off_additional_buttons(self, on_off, status):
        if (on_off == "Puertas Estacionamiento"):
            self.__Arduino.on__off_parking(on_off,status)

    def __on_off_fan(self, fan_state, fan_code):
        DataArduino.on_off_fans(self, fan_state, fan_code)

    def __on_closing(self):
        self.__Arduino.on_closing(self.__master)


if __name__ == "__main__":
    app = MainApp()
    app.run()