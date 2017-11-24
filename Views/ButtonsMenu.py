from tkinter import Button, N, S, E, W, Label
from Views.AdditionalButtons import AdditionalButtons

class ButtonsMenu():
    class Constants:
        bed_room_points = [(0, 0), (0, 200), (125, 200), (125, 175), (150, 175), (150, 0)]
        bath_room1_points = [(0, 200), (0, 275), (125, 275), (125, 200)]
        bath_room2_points = [(50, 275), (50, 350), (125, 350), (125, 275)]
        garden_ponits = [(0, 275), (50, 275), (50, 350), (100, 350), (100, 375), (150, 375), (150, 500), (0, 500)]
        garden_text_points = [75, 437.5]
        kitchen_ponits = [(150, 0), (150, 175), (300, 175), (300, 0)]
        living_room_points = [(125, 175), (125, 350), (100, 350), (100, 375), (300, 375), (300, 175)]
        parking_points = [(150, 375), (150, 500), (400, 500), (400, 375)]
        service_room_points = [(300, 0), (300, 200), (400, 200), (400, 0)]
        red = "#E54365"
        green = "#2F942C"
        room_color = "#6E6E6E"
        weather_color = "#AFB5C2"
        black = "black"
        center = N + S + E + W
        font = "Rockwell"
        additionals_buttons = ["Jardin", "Ventiladores", "Puertas Estacionamiento"]
        additionals_buttons_positions = [[550, 275], [510, 350], [575, 425]]
        garden_text = "Jardin"
        fan_text = "Ventiladores"
        door_text = "Puertas estacionamiento"
        notifications_text = "Notificaciones"
        weather_text = "Informacion del Clima"
        bg = "#505F80"

    class Event:
        click = "<Button-1>"


    def __init__(self, canvas, text, action_parking = None):
        self.__rooms = canvas
        self.__action_parking = action_parking
        self.__weather_text = text
        self.__notifications_button = Button(font=self.Constants.font)
        self.__fan_button = Button(font=self.Constants.font)
        self.__door_button = Button(font=self.Constants.font)
        self.__weather_label = Label(bg=self.Constants.weather_color, width=35, height=10, font=self.Constants.font)
        self.__create_plane()
        self.__create_buttons()

    def __create_plane(self):
        self.__rooms.create_polygon(self.Constants.bed_room_points, fill=self.Constants.room_color, outline=self.Constants.black)
        self.__rooms.create_polygon(self.Constants.bath_room1_points, fill=self.Constants.room_color, outline=self.Constants.black)
        self.__rooms.create_polygon(self.Constants.bath_room2_points, fill=self.Constants.room_color, outline=self.Constants.black)
        self.__rooms.create_polygon(self.Constants.garden_ponits, fill=self.Constants.room_color, outline=self.Constants.black)
        self.__rooms.create_text(self.Constants.garden_text_points, font=self.Constants.font, text=self.Constants.garden_text)
        self.__rooms.create_polygon(self.Constants.kitchen_ponits, fill=self.Constants.room_color, outline=self.Constants.black)
        self.__rooms.create_polygon(self.Constants.living_room_points, fill=self.Constants.room_color, outline=self.Constants.black)
        self.__rooms.create_polygon(self.Constants.parking_points, fill=self.Constants.room_color, outline=self.Constants.black)
        self.__rooms.create_polygon(self.Constants.service_room_points, fill=self.Constants.room_color, outline=self.Constants.black)

    def __create_buttons(self):

        for index, key in enumerate(self.Constants.additionals_buttons):
            x = self.Constants.additionals_buttons_positions[index-1][0]
            y = self.Constants.additionals_buttons_positions[index-1][1]
            button = AdditionalButtons(key, action_parking = self.__did_tap_parking)
            button.position(x,y)

        self.__weather_label.place(x = 450, y = 50)
        self.__weather_label.config(text=self.__weather_text)

    def __did_tap_parking(self, pin, status):
        self.__action_parking(pin, status)




