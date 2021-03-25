import cv2 as cv
import numpy as np
import pySerial
import canvas
import time

serial = pySerial.PySerial()
W = 500  # fixme: yo wtf andere waarden dan 500 verneukt de lijnen
H = W
margin = 10
radar_window = "Radar"
size = W, H, 3
radar_image = np.zeros(size, dtype=np.uint8)
canvas = canvas.Canvas(radar_window, radar_image, margin, W)
canvas.update_canvas()

# time.sleep(1)
while True:
    canvas.update_canvas()
    if serial.ser.inWaiting():
        line = serial.read_line()
        print(line)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
