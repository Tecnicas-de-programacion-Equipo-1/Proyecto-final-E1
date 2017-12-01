from Models.DataArduino import DataArduino
from Models.WeatherManager import WeatherManager
from Models.ControlTwilio import ControlTwilio
from Views.MainView import MainView

class MainApp():
    class Constants:
        delete = "WM_DELETE_WINDOW"
        additionals_buttons = ["Notificaciones", "Control - Ventiladores", "Ventilador - Sala", "ventilador - Recamara","Puertas Estacionamiento"]
        danger = 5

    def __init__(self):
        self.__danger_activation = False
        self.__notification_activation =False
        self.__weather = WeatherManager.get_weather_data()
        self.__weather_text  = self.__weather.information
        self.__master = MainView(action = self.__on_off, weather_text = self.__weather_text, action_additional_buttons = self.__on__off_additional_buttons, fans_action = self.__on_off_fan)
        self.__Arduino = DataArduino()
        self.__master.protocol(self.Constants.delete, self.__on_closing)
        self.__Control_twilio = ControlTwilio()
        self.__Arduino.read_port()
        self.__MotionSensor()

    def run(self):
        self.__master.mainloop()

    def __MotionSensor(self):
        data = self.__Arduino.update_clock()
        self.__Arduino.handle_data(data)
        if int(data) == self.Constants.danger:
            self.__danger_activation = True
        self.__notification()
        self.__master.after(1,self.__MotionSensor)

    def __on_off(self, sender, code, state):
        self.__Arduino.on_off(sender,code,state)

    def __on__off_additional_buttons(self, on_off, status):
        if (on_off == self.Constants.additionals_buttons[0]):
            self.__notification_activation = status

        if (on_off == self.Constants.additionals_buttons[4]):
            self.__Arduino.on__off_parking(on_off,status)

    def __notification(self):
        if self.__danger_activation and self.__notification_activation:
            self.__Control_twilio.send_message()
            self.__notification_activation = not(self.__notification_activation)

    def __on_off_fan(self, fan_state, fan_code):
        self.on_off_fans(self, fan_state, fan_code)

    def __on_closing(self):
        self.__Arduino.on_closing(self.__master)


if __name__ == "__main__":
    app = MainApp()
    app.run()