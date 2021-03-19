import serial
import time
ser = serial.Serial('/dev/ttyS9', 9600, timeout=1)
#wait for the connection to complete
# time.sleep(3)
print(ser.name)
message = b"180"
ser.write(message)
s = ""
for char in message:
    s += ser.read(1).decode("utf-8")
print(s)
ser.close()
