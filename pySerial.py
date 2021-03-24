import serial
import time
# wait for the connection to complete
# time.sleep(3)



class PySerial:
    def __init__(self):
        self.ser = serial.Serial('com3', 9600, timeout=1)
        print("kaas")

    def read_line(self):
        line = self.ser.readline().decode('utf-8').replace("\r\n", "")
        linesplit = line.split("|")
        return linesplit
    def close_conn(self):
        self.ser.close()
