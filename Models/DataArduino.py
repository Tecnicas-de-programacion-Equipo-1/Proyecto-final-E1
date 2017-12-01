import serial
from serial.tools import list_ports

class DataArduino():

    def __init__(self):
        self.__arduino = None
        self.__array_complete = False
        self.__array_values = []
        self.Arduino()
        self.value_sensor = self.handle_data(self.update_clock())


    def read_port(self):
        for port in list_ports.comports(include_links=True):
            print(port.device, port.name, port.description)

    def Arduino(self):
        self.__arduino = serial.Serial('COM5', 115200)


    def on_off(self, sender, code, state):
        data = ("1" + code) if state else ("0" + code)
        data = str(data).encode('ascii')
        self.__arduino.write(data)
        return data

    def on__off_parking(self, on_off, status):
        data = "True" if status else "False"
        data = str(data).encode("ascii")
        self.__arduino.write(data)

    def on_off_fans(self,function_of_fans, bedroom_fan_state):
        data = ( bedroom_fan_state + "_on") if function_of_fans else ( bedroom_fan_state + "_off" )
        data = str(data).encode("ascii")
        self.__arduino.write(data)

    def handle_data(self, data):
        clean_values = data.strip(' \n\r').split(",")
        value = clean_values[0]
        temp_one = clean_values[1]
        temp_two = clean_values[2]
        Automatic_Control_Fans(temp_one, temp_two)
        return value

    def update_clock(self):
        data = self.__arduino.readline().decode()
        return data

    def on_closing(self, master):
        self.__arduino.close()
        master.destroy()