from Views.RoomsBottons import RoomsBottons

class RoomsBottonsMenu ():
    class Constants:
        rooms = ["Recamara \n Principal", "Baño 1", "Baño 2", "Cocina", "Sala/Comedor", "Estacionamiento",
                 "Cuarto \n de \n Servicio"]
        position = [[30,220],[57,295],[190,70],[155,250],[210,420],[315,55],[30,60]]

    def __init__(self, master, action = None):
        self.__action = action

        for index_row, key in enumerate(self.Constants.rooms):
            x = self.Constants.position[index_row-1][0]
            y = self.Constants.position[index_row-1][1]
            button = RoomsBottons(master, key, action = self.__did_tap)
            button.position(x,y)

    def __did_tap(self, sender):
        self.__action(sender)
