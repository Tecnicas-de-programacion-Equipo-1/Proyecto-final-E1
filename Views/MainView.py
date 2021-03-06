from tkinter import Tk, Canvas
from Views.ButtonsMenu import ButtonsMenu
from Views.RoomsBottonsMenu import RoomsBottonsMenu

class MainView(Tk):
    class Constants:
        title = "Casa Inteligente"
        bg = "#797D85"
        height = 500
        width = 800



    def __init__(self, action = None, weather_text = None, action_additional_buttons = None):
        super().__init__()
        self.__action=action
        self.__action_additional_buttons = action_additional_buttons
        self.title(self.Constants.title)
        self.configure(bg = self.Constants.bg)
        self.maxsize(width = self.Constants.width, height = self.Constants.height)
        self.minsize(width = self.Constants.width, height = self.Constants.height)
        self.__configure_grid()
        self.__configure_UI(action = action, text = weather_text, action_additional_buttons = action_additional_buttons)

    def __configure_grid(self):
        self.grid_columnconfigure(0, minsize = 400)
        self.grid_columnconfigure(1, minsize = 300)

        self.__canvas = Canvas(self, width=400, height=500, bg=self.Constants.bg)
        self.__canvas.grid(column=0)

    def __configure_UI(self, action = None, text = None, action_additional_buttons = None):
        ButtonsMenu(self.__canvas, text, action = self.__did_tap_additional_buttons)
        RoomsBottonsMenu(self, action = self.__did_tap)

    def __did_tap(self, sender, code, status):
        self.__action(sender, code, status)

    def __did_tap_additional_buttons(self, on__off, status):
        self.__action_additional_buttons(on__off,status)

