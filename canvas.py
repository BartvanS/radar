import cv2 as cv
import math

grid_step = 20


# coordinates
# 0: degree
# 1: coordinates
class Canvas:
    def __init__(self, window, img, margin, w, circle_radius):
        self.window = window
        self.img = img
        self.half = w // 2
        self.center = (self.half, self.half)
        self.border_margin = margin
        self.W = w
        self.dots = []
        self.radius = circle_radius
        self.setup_canvas()

    def setup_canvas(self):
        self.update_canvas()
        cv.moveWindow(self.window, 0, 0)

    def update_canvas(self):
        # Grid
        gray = (50, 50, 50)
        for coord in range(0, self.W, grid_step):
            self.gen_line((0, coord), (self.W, coord), gray)
            self.gen_line((coord, 0), (coord, self.W), gray)
        # Center dot
        self.gen_dots(self.center, (0, 0, 255))
        # Outer circle
        self.gen_circle(self.center, self.radius)
        cv.imshow(self.window, self.img)

    def add_dot(self, coordinate, color=(255, 0, 0)):
        self.dots.append(coordinate)
        self.gen_dots(coordinate, color)

    def remove_dot(self):
        coordinate = self.dots.pop()
        self.del_dots(coordinate)

    def gen_circle(self, coordinate, radius, color=(0, 255, 0)):
        thickness = 1
        cv.circle(self.img, coordinate, radius, color, thickness)

    def gen_line(self, start, end, color=(0, 255, 0)):
        thickness = 1
        line_type = 8
        cv.line(self.img,
                start,
                end,
                color,
                thickness,
                line_type)

    def del_line(self, start, end):
        thickness = 1
        line_type = 8
        cv.line(self.img,
                start,
                end,
                (0, 0, 0),
                thickness,
                line_type)

    def gen_dots(self, coordinate, color=(0, 255, 0), radius=5):
        thickness = -1
        line_type = 8
        cv.circle(self.img,
                  coordinate,
                  radius,
                  color,
                  thickness,
                  line_type)

    def del_dots(self, center):
        thickness = -1
        line_type = 8
        cv.circle(self.img,
                  center,
                  5,
                  (0, 0, 0),
                  thickness,
                  line_type)
