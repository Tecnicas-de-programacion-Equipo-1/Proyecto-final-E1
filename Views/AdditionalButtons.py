from tkinter import Tk, Button, N, S, E, W
from Views.ControlParking import ControlParking

class AdditionalButtons(Tk):
    class Constants:
        center = N+S+W+E
        red = "#E54365"
        green = "#2F942C"
        font = "Rockwell"


    class Event:
        click = "<Button-1>"

    def __init__(self,key, action_parking = None):
        self.__key = key
        self.__button = Button(text = key)
        self.__state = False
        self.__action_parking = action_parking

        self.__button.configure(font = self.Constants.font)
        bg = self.Constants.gree if self.__state else self.Constants.red
        self.__button.configure(bg=bg)

        self.__button.bind(self.Event.click, self.__did_tap)

    def position(self, x, y):
        self.__button.place(x = x, y = y)

    def __did_tap(self, event):
        self.__state = not self.__state
        if self.__key == "Puertas Estacionamiento":
            self.__action_parking(9, self.__state)
            #ControlParking(self, action = self.__did_tap_parking)
        bg = self.Constants.green if self.__state else self.Constants.red
        self.__button.configure(bg=bg)

    def __did_tap_parking(self, pin, state):
        self.__action_parking(pin,state)