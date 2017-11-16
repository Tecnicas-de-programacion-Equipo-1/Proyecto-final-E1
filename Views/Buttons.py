from tkinter import Button, N, S, E, W

class Buttons():
    class Constants:
        blue = "blue"
        yellow = "yellow"
        grey = "grey"
        green = "green"
        pink = "pink"
        orange = "orange"
        brown = "brown"
        color_service = "#DAF7A6"
        center = N + S + E + W
        bed_room_text="Recamara Principal"
        bath_room_text = "Baño"
        garden_text = "Jardin"
        kitchen_text="Cocina"
        living_room_text="Sala/Comedor"
        parking_text="Estacionamiento"
        service_room_text="Cuarto de Servicio"
        fan_text = "Ventiladores"
        door_text = "Puertas estacionamiento"
        notifications_text = "Notificaciones"



    def __init__(self):
        self.__bedroom_button = Button()
        self.__first_bathroom_button = Button()
        self.__second_bathroom_button = Button()
        self.__garden_button = Button()
        self.__kitchen_button = Button()
        self.__living_room_button = Button()
        self.__parking_button = Button()
        self.__service_button = Button()
        self.__notifications_button = Button()
        self.__fan_button = Button()
        self.__door_button = Button()
        self.__create_buttons()

    def __create_buttons(self):

        self.__bedroom_button.configure(text = self.Constants.bed_room_text, bg = self.Constants.blue)
        self.__bedroom_button.grid(row = 0, column = 0, sticky = self.Constants.center)

        self.__first_bathroom_button.configure(text = self.Constants.bath_room_text, bg = self.Constants.grey)
        self.__first_bathroom_button.grid(row = 1, column = 0, sticky = self.Constants.center)

        self.__second_bathroom_button.configure(text = self.Constants.bath_room_text, bg = self.Constants.blue)
        self.__second_bathroom_button.grid(row = 2, column = 0, sticky = self.Constants.center)

        self.__garden_button.configure(text = self.Constants.garden_text, bg = self.Constants.green)
        self.__garden_button.grid(row = 3, column = 0, sticky = self.Constants.center)

        self.__kitchen_button.configure(text = self.Constants.kitchen_text, bg = self.Constants.orange)
        self.__kitchen_button.grid(row = 0, column = 1, sticky = self.Constants.center)

        self.__living_room_button.configure(text = self.Constants.living_room_text, bg = self.Constants.pink)
        self.__living_room_button.grid(row = 1, column = 1, sticky = self.Constants.center, rowspan = 2)

        self.__parking_button.configure(text = self.Constants.parking_text, bg = self.Constants.yellow)
        self.__parking_button.grid(row = 3, column = 1, sticky = self.Constants.center, columnspan = 2)

        self.__service_button.configure(text=self.Constants.service_room_text, bg=self.Constants.color_service)
        self.__service_button.grid(row = 0, column = 2, sticky = self.Constants.center)

        self.__notifications_button.configure(text = self.Constants.notifications_text, bg = self.Constants.grey)
        self.__notifications_button.grid(row = 0, column = 4)

        self.__fan_button.configure(text = self.Constants.fan_text, bg = self.Constants.brown)
        self.__fan_button.grid(row = 2, column = 4)

        self.__door_button.configure(text = self.Constants.door_text, bg = self.Constants.yellow)
        self.__door_button.grid(row = 3, column = 4)
