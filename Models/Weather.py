class Weather:
    def __init__(self, json):
        self.__country = json["name"]
        self.__weather = json["weather"][0]["description"]
        self.__temp = json["main"]["temp"]

    @property
    def name(self):
        info = """Ciudad: {} \nTemperatura: {} \nDescripcion: {} """.format(self.__country, self.__temp, self.__weather)
        return info

    def __repr__(self):
        return "{}, {}".format(self.__name, self.__date)