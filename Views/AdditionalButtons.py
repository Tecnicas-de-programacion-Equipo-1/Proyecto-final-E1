from tkinter import Button, N, S, E, W
from Views.ControlParking import ControlParking

class AdditionalButtons(Button):
    class Constants:
        center = N+S+W+E
        red = "#E54365"
        green = "#2F942C"
        font = "Rockwell"
        parking = "Puertas Estacionamiento"


    class Event:
        click = "<Button-1>"

    def __init__(self,key, action_parking = None):
        super().__init__()
        self.__action_parking = action_parking
        self.__key = key
        self.__button = Button(text = key)
        self.__state = False

        self.__button.configure(font = self.Constants.font)
        bg = self.Constants.green if self.__state else self.Constants.red
        self.__button.configure(bg=bg)

        self.__button.bind(self.Event.click, self.__did_tap)

    def position(self, x, y):
        self.__button.place(x = x, y = y)

    def __did_tap(self, event):
        self.__state = not self.__state
        if self.__key == self.Constants.parking:
            ControlParking(self.__state, action_parking = self.__tap_parking)
        bg = self.Constants.green if self.__state else self.Constants.red
        self.__button.configure(bg=bg)

    def __tap_parking(self, on_off, status):
        self.__action_parking(on_off, status)