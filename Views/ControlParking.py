from tkinter import Button

class ControlParking(Button):
    class Constants:
        on = "Abre puerta"
        off = "Cierra puerta"

    class Event:
        click = "<Button-1>"

    def __init__(self, status, action_parking = None):
        super().__init__()
        self.__action_parking = action_parking
        self.__status = status
        if self.__status:
            self.__action_parking(self.Constants.on, self.__status)
        else:
            self.__action_parking(self.Constants.off, self.__status)