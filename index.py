import cv2 as cv
import numpy as np
def gen_line(window,img, start, end):
	thickness = 2
	line_type = 8
	cv.line(img,
			start,
			end,
			(0, 255, 0),
			thickness,
			line_type)
	cv.imshow(window, img)

def del_line(window,img, start, end):
	thickness = 2
	line_type = 8
	cv.line(img,
			start,
			end,
			(0, 0, 0),
			thickness,
			line_type)
	cv.imshow(window, img)

def gen_dots(window, img, center):
	thickness = -1
	line_type = 8
	cv.circle(img,
				center,
				5,
				(0, 0, 255),
				thickness,
				line_type)
	cv.imshow(window, img)

def del_dots(window, img, center):
	thickness = -1
	line_type = 8
	cv.circle(img,
				center,
				5,
				(0, 0, 0),
				thickness,
				line_type)
	cv.imshow(window, img)
W = 400
H = W
center = int(W / 2)
center_coord = (center, center)
radar_window = "Radar"
size = W, H, 3
radar_image = np.zeros(size, dtype=np.uint8)
#coordinates
lines = [[(0, 0), (400, 400)], [(400, 0), (0, 400)]]
#3 px = 1 cm
# 0: degree
# 1: coordinates
dots = [[0, center_coord], [1, (200, 242)]]

for line in lines:
	gen_line(radar_window, radar_image, line[0], line[1])
for dot in dots:
	gen_dots(radar_window, radar_image, dot[1])
cv.waitKey(0)
# for line in lines:
# 	del_line(radar_window, radar_image, line[0], line[1])
for dot in dots:
	del_dots(radar_window, radar_image, dot[1])	
	
cv.waitKey(0)
cv.destroyAllWindows()