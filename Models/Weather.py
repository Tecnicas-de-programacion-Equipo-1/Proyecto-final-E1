class Weather:
    class Constants:
        kelvin = 273.15
    def __init__(self, json):
        self.__country = json["name"]
        self.__weather = json["weather"][0]["description"]
        self.__temp = json["main"]["temp"]

    @property
    def information(self):
        temperature = float(self.__temp) - self.Constants.kelvin
        info = "Ciudad: {} \nTemperatura: {:.2f}°C \nDescripcion: {} ".format(self.__country, temperature , self.__weather)
        return info

    def __repr__(self):
        return "{}, {}".format(self.__name, self.__date)