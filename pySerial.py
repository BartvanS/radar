import serial

class PySerial:
    def __init__(self, timeout = 1):
        self.ser = serial.Serial('com3', 9600, timeout=timeout)
        print("serial connected")

    def read_line(self):
        line = self.ser.readline().decode('utf-8').replace("\r\n", "")
        linesplit = line.split("|")
        return linesplit

    def close_conn(self):
        self.ser.close()
