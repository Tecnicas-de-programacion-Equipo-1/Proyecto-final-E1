from tkinter import Button, N, S, E, W

class RoomsBottons(Button):
    class Constants:
        center = N + S + W + E
        room_color = "#848689"
        letter_color = '#202020'
        font = "Rockwell"

    class Event:
        click = "<Button-1>"

    def __init__(self, master, key, action = None):
        super().__init__(master)
        self.__action = action
        self.key = key

        self.configure(text=self.key)
        self.configure(font=self.Constants.font)
        bg, foreground = (self.Constants.room_color, self.Constants.letter_color)
        self.configure(bg=bg, foreground=foreground)

        self.bind(self.Event.click, self.__did_tap)

    def position(self, x, y):
        self.place(x = x, y = y)

    def __did_tap(self, event):
        if self.__action is None: return
        self.__action(self.key)