from tkinter import Tk, Canvas
from Views.ButtonsMenu import ButtonsMenu
from Views.RoomsBottonsMenu import RoomsBottonsMenu

class MainView(Tk):
    class Constants:
        title = "Casa Inteligente"
        color_house = "#848689"
        bg = "#505F80"
        height = 500
        width = 800


    def __init__(self, action = None):
        super().__init__()
        self.__action=action
        self.title(self.Constants.title)
        self.configure(bg = self.Constants.bg)
        self.maxsize(width = self.Constants.width, height = self.Constants.height)
        self.minsize(width = self.Constants.width, height = self.Constants.height)
        self.__configure_grid()
        self.__configure_UI(action = action)

    def __configure_grid(self):
        self.grid_columnconfigure(0, minsize = 400)
        self.grid_columnconfigure(1, minsize = 300)

        self.__canvas = Canvas(self, width=400, height=500, bg=self.Constants.bg)
        self.__canvas.grid(column=0)

    def __configure_UI(self, action = None):
        ButtonsMenu(self.__canvas)
        RoomsBottonsMenu(self, action = self.__did_tap)

    def __did_tap(self, sender, pin, status):
        self.__action(sender, pin, status)







