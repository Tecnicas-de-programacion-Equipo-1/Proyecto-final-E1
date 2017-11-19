from Views.MainView import MainView
import serial
from serial.tools import list_ports

class MainApp():
    class Constant:
        port = "COM6"
        event = "WM_DELETE_WINDOW"
        baudios = 115200

    def __init__(self):
        for port in list_ports.comports(include_links = True):
            print(port.device, port.name, port.description)
        self.__master = MainView(tap_handler = self.__toggle_did_change)
        self.__arduino = serial.Serial(self.Constant.port, self.Constant.baudios)
        self.__master.protocol(self.Constant.event, self.__on_closing)

    def run(self):
        self.__master.mainloop()

    def __toggle_did_change(self, state):
        if state == 3:
            value = str(1).encode("ascii")
            self.__arduino.write(value)
        elif state == 4:
            value = str(0).encode("ascii")
            self.__arduino.write(value)

    def __on_closing(self):
        self.__arduino.close()
        self.__master.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.run()