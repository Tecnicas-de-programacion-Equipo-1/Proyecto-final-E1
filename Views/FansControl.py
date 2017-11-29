from tkinter import Button

class FansControl(Button):
    class Constants:
        bedroom_fan_on = "fan_one_on"
        bedroom_fan_off = "fan_one_off"


    class Event:
        click = "<Button-1>"

    def __init__(self, status, fans_action = None):
        super().__init__()
        self.__fans_action = fans_action
        self.__status = status


   # def bedroom(self):
        if self.__status:
            self.__fans_action(self.__status, self.Constants.bedroom_fan_on)
        else:
            self.__fans_action(self.__status, self.Constants.bedroom_fan_off)