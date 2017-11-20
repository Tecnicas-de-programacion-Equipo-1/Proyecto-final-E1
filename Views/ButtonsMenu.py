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

    class Event:
        click = "<Button-1>"


    def __init__(self, master_rooms, action = None):
        self.__action = action
        self.__rooms = master_rooms
        self.__notifications_button = Button(font=self.Constants.font)
        self.__fan_button = Button(font=self.Constants.font)
        self.__door_button = Button(font=self.Constants.font)
        self.__weather_label = Label(bg=self.Constants.weather_color, width=35, height=10, font=self.Constants.font)
        self.__create_plane()
        self.__create_buttons()
        self.__door_button.bind(self.Event.click, self.__did_tap)

    def __create_plane(self):
        self.__rooms.create_polygon((0, 0), (0, 200), (125, 200), (125, 175), (150, 175), (150, 0),
                                    fill=self.Constants.room_color, outline=self.Constants.black)
        self.__rooms.create_polygon((0, 200), (0, 275), (125, 275), (125, 200), fill=self.Constants.room_color,
                                    outline=self.Constants.black)
        self.__rooms.create_polygon((50, 275), (50, 350), (125, 350), (125, 275), fill=self.Constants.room_color,
                                    outline=self.Constants.black)
        self.__rooms.create_polygon((0, 275), (50, 275), (50, 350), (100, 350), (100, 375), (150, 375), (150, 500),
                                    (0, 500), fill=self.Constants.room_color, outline=self.Constants.black)
        self.__rooms.create_polygon((150, 0), (150, 175), (300, 175), (300, 0), fill=self.Constants.room_color,
                                    outline=self.Constants.black)
        self.__rooms.create_polygon((125, 175), (125, 350), (100, 350), (100, 375), (300, 375), (300, 175),
                                    fill=self.Constants.room_color, outline=self.Constants.black)
        self.__rooms.create_polygon((150, 375), (150, 500), (400, 500), (400, 375), fill=self.Constants.room_color,
                                    outline=self.Constants.black)
        self.__rooms.create_polygon((300, 0), (300, 200), (400, 200), (400, 0), fill=self.Constants.room_color,
                                    outline=self.Constants.black)
    
    def __create_buttons(self):


        self.__weather_label.place(x=450, y=50)
        self.__weather_label.config(text=self.Constants.weather_text)

        self.__notifications_button.configure(text = self.Constants.notifications_text, bg = self.Constants.red)
        self.__notifications_button.place(x = 550, y = 275)

        self.__fan_button.configure(text = self.Constants.fan_text, bg = self.Constants.green)
        self.__fan_button.place(x = 555, y = 350)

        self.__door_button.configure(text = self.Constants.door_text, bg = self.Constants.red)
        self.__door_button.place(x = 525, y = 425)

    def __did_tap(self, event):
        if self.__action is None: return
        self.__action("estacionamiento")