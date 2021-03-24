import cv2 as cv
import numpy as np
import pySerial
import time
import canvas

W = 500
H = W
margin = 10
radar_window = "Radar"
size = W, H, 3
radar_image = np.zeros(size, dtype=np.uint8)
canvas = canvas.Canvas(radar_window, radar_image, margin, W)

# for dot in dots:
#     canvas.gen_dots(radar_window, radar_image, dot)
cv.waitKey(0)
# for line in lines:
# 	del_line(radar_window, radar_image, line[0], line[1])
# for dot in dots:
# 	del_dots(radar_window, radar_image, dot[1])

# serial = pySerial.PySerial()
# while True:
#     # time.sleep(1)
#     if serial.ser.inWaiting():
#         line = serial.read_line()
#         print(line)
cv.waitKey(0)
cv.destroyAllWindows()
