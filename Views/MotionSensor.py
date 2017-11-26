
class MotionSensor():
    class Constants:
        number_of_dates = 40

    def __init__(self, values):
        super().__init__()
        self.__distance_average = 0
        self.__sum = 0
        self.__average_distance(values)


    def __average_distance(self, value):
        for index in range(1, 40):
            self.__sum = self.__sum + int(value)
        self.__distance_average = self.__sum / self.Constants.number_of_dates
        self.__sum = 0
        round(self.__distance_average)
