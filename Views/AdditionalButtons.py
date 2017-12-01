from tkinter import Button, N, S, E, W

class AdditionalButtons(Button):
    class Constants:
        center = N+S+W+E
        red = "#F17878"
        green = "#5BDA72"
        font = "Rockwell"
        # parking = "Puertas Estacionamiento"
        # bedroom = "ventilador - Recamara"
        # livingroom = "Ventilador - Sala"
        # both_fans = "Control - Ventiladores"
        overrelief = "sunken"


    class Event:
        click = "<Button-1>"

    def __init__(self,key, coed_for_others, action = None, fans_action = None):
        super().__init__()
        self.__action = action
        self.__fans_action = fans_action
        self.__code_for_others = coed_for_others
        self.__key = key
        self.__button = Button(text = key, overrelief = self.Constants.overrelief)
        self.__state = False

        self.__button.configure(font = self.Constants.font)
        bg = self.Constants.green if self.__state else self.Constants.red
        self.__button.configure(bg=bg)

        self.__button.bind(self.Event.click, self.__did_tap)

    def position(self, x, y):
        self.__button.place(x = x, y = y)

    def __did_tap(self, event):
        self.__state = not self.__state
        self.__action(self.__key, self.__state)
        self.__fans_action(self.__state,self.__code_for_others)
        bg = self.Constants.green if self.__state else self.Constants.red
        self.__button.configure(bg=bg)

    def __tap(self, on_off, status):
        self.__action(on_off, status)

