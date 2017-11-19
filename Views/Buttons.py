from tkinter import Button, N, S, E, W, Label
class Buttons():
    class Constants:
        red = "#E54365"
        green = "#2F942C"
        room_color = "#848689"
        weather_color = "#AFB5C2"
        black = "black"
        center = N + S + E + W
        font = "Rockwell"
        bed_room_text="Recamara \n Principal"
        bath_room_text = "Baño"
        garden_text = "Jardin"
        kitchen_text="Cocina"
        living_room_text="Sala/Comedor"
        parking_text="Estacionamiento"
        service_room_text="Cuarto \n de \n Servicio"
        fan_text = "Ventiladores"
        door_text = "Puertas estacionamiento"
        notifications_text = "Notificaciones"
        weather_text = "Informacion del Clima"



    def __init__(self, master_rooms, tap_handler = None):
        self.__tap_handler = tap_handler
        self.__state_button = 4
        self.__rooms = master_rooms
        self.__notifications_button = Button(font=self.Constants.font)
        self.__fan_button = Button(font=self.Constants.font)
        self.__door_button = Button(font=self.Constants.font)
        self.__weather_label = Label(bg=self.Constants.weather_color, width=35, height=10, font=self.Constants.font)
        self.__create_buttons()

    def __create_buttons(self):
        self.__rooms.create_polygon((0, 0), (0, 200), (125, 200), (125, 175), (150, 175), (150, 0),
                                    fill=self.Constants.room_color, outline=self.Constants.black)
        self.__rooms.create_text(75,100, font = self.Constants.font, text = self.Constants.bed_room_text)

        self.__rooms.create_polygon((0, 200), (0, 275), (125, 275), (125, 200), fill=self.Constants.room_color,
                                    outline=self.Constants.black)
        self.__rooms.create_text(62.5, 237.5, font=self.Constants.font, text=self.Constants.bath_room_text)

        self.__rooms.create_polygon((50, 275), (50, 350), (125, 350), (125, 275), fill=self.Constants.room_color,
                                    outline=self.Constants.black)
        self.__rooms.create_text(87.5, 312.5, font=self.Constants.font, text=self.Constants.bath_room_text)

        self.__rooms.create_polygon((0, 275), (50, 275), (50, 350), (100, 350), (100, 375), (150, 375), (150, 500),
                                    (0, 500), fill=self.Constants.room_color, outline=self.Constants.black)
        self.__rooms.create_text(75, 437.5, font=self.Constants.font, text=self.Constants.garden_text)

        self.__rooms.create_polygon((150, 0), (150, 175), (300, 175), (300, 0), fill=self.Constants.room_color,
                                    outline=self.Constants.black)
        self.__rooms.create_text(225, 87.5, font=self.Constants.font, text=self.Constants.kitchen_text)

        self.__rooms.create_polygon((125, 175), (125, 350), (100, 350), (100, 375), (300, 375), (300, 175),
                                    fill=self.Constants.room_color, outline=self.Constants.black)
        self.__rooms.create_text(212.5, 275, font=self.Constants.font, text=self.Constants.living_room_text)

        self.__rooms.create_polygon((150, 375), (150, 500), (400, 500), (400, 375), fill=self.Constants.room_color,
                                    outline=self.Constants.black)
        self.__rooms.create_text(275, 437.5, font=self.Constants.font, text=self.Constants.parking_text)

        self.__rooms.create_polygon((300, 0), (300, 200), (400, 200), (400, 0), fill=self.Constants.room_color,
                                    outline=self.Constants.black)
        self.__rooms.create_text(350, 100, font=self.Constants.font, text=self.Constants.service_room_text)

        self.__weather_label.place(x=450, y=50)
        self.__weather_label.config(text=self.Constants.weather_text)

        self.__notifications_button.configure(text = self.Constants.notifications_text, bg = self.Constants.red)
        self.__notifications_button.place(x = 550, y = 275)

        self.__fan_button.configure(text = self.Constants.fan_text, bg = self.Constants.green)
        self.__fan_button.place(x = 555, y = 350)


        self.__door_button.configure(text = self.Constants.door_text, bg = self.Constants.red, command = self.ParkingControl)
        self.__door_button.place(x = 525, y = 425)

    def ParkingControl(self):
        if self.__state_button == 3:
            self.__state_button = 4
        elif self.__state_button == 4:
            self.__state_button = 3
        if self.__tap_handler is None: return
        self.__tap_handler(self.__state_button)






