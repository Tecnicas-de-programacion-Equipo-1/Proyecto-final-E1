from tkinter import Button, N, S, E, W

class RoomsBottons(Button):
    class Constants:
        center = N + S + W + E
        room_color_off = "#848689"
        room_color_on = "#F7DC6F"
        letter_color = '#202020'
        font = "Rockwell"

    class Event:
        click = "<Button-1>"

    def __init__(self, master, key, action = None):
        super().__init__(master)
        self.__action = action
        self.key = key
        self.__state = False

        self.configure(text=self.key)
        self.configure(font=self.Constants.font)
        bg = self.Constants.room_color_on if self.__state else self.Constants.room_color_off
        foreground = self.Constants.letter_color
        self.configure(bg=bg, foreground=foreground)

        self.bind(self.Event.click, self.__did_tap)

    def position(self, x, y):
        self.place(x = x, y = y)

    def __did_tap(self, event):
        if self.__action is None: return
        self.__action(self.key)
        self.__state = not self.__state
        foreground = self.Constants.letter_color
        bg = self.Constants.room_color_on if self.__state else self.Constants.room_color_off
        self.configure(bg=bg, foreground=foreground)