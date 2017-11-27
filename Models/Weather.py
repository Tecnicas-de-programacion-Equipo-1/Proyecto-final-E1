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
        info = """MX,{}    -   {}\nTemperatura: {:.2f}°C """.format(self.__country, self.__weather, temperature)
        return info

    @property
    def temperature(self):
        temperature = float(self.__temp) - self.Constants.kelvin
        return temperature

    def __repr__(self):
        return "{}, {}".format(self.__name, self.__date)