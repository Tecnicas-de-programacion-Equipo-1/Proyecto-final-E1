from tkinter import Tk
from Views.Buttons import Buttons

class MainView(Tk):
    class Constants:
        title = "Casa Inteligente"
        bg = "#BEC1B8"
        height = 550
        width = 800
        row_dimensions = [200, 50, 50, 200]
        column_dimensions = [150,  150, 100, 200, 100]


    def __init__(self):
        super().__init__()
        self.title(self.Constants.title)
        self.configure(bg = self.Constants.bg)
        self.maxsize(width = self.Constants.width, height = self.Constants.height)
        self.minsize(width = self.Constants.width, height = self.Constants.height)
        self.__configure_grid()
        self.__configure_UI()

    def __configure_grid(self):
        self.grid_rowconfigure(0, minsize = 200)
        self.grid_rowconfigure(1, minsize = 75)
        self.grid_rowconfigure(2, minsize = 75)
        self.grid_rowconfigure(3, minsize = 200)

        self.grid_columnconfigure(0, minsize = 150)
        self.grid_columnconfigure(1, minsize = 150)
        self.grid_columnconfigure(2, minsize = 100)
        self.grid_columnconfigure(3, minsize = 200)
        self.grid_columnconfigure(4, minsize = 100)


    def __configure_UI(self):
        Buttons()


