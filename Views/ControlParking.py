from tkinter import Button

class ControlParking():
    class Constants:
        pin_parking = 9

    class event:
        click = "<Button-1>"

    def __init__(self, action = None):
        super().__init__()
        self.__action = action
        self.__pin_parking = self.Constants.pin_parking
        self.__state = False
        self.bind(self.event.click, self.__did_tap)

    def __did_tap(self):
        if self.__action is None: return
        self.__state = not self.__state
        self.__action(self.__pin_parking, self.__state)