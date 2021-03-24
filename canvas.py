import cv2 as cv
# 10 px = 1 cm
step = 20

# coordinates
# 0: degree
# 1: coordinates
class Canvas:
    def __init__(self, window, img, margin, w):
        self.window = window
        self.img = img
        self.half = w // 2
        self.center = (self.half, self.half)
        self.border_margin = margin
        self.W = w
        self.dots = []

        default_lines = [[(margin, self.half), (self.W - margin, self.half)],
                         [(self.half, margin), (self.half, self.W - margin)]]
        default_circles = [self.center]
        # development help
        for line in default_lines:
            self.gen_line(line[0], line[1])
        # Outer circle
        radius = w // 2 - margin
        for coordinate in default_circles:
            self.gen_circle(coordinate, radius)
        # Center dot
        self.gen_dots(self.center, (0, 0, 255))
        # Grid
        gray = (50, 50, 50)
        for coord in range(0, self.W, step):
            self.gen_line((0, coord), (self.W, coord), gray)
            self.gen_line((coord, 0), (coord, self.W), gray)

    def add_dot(self, coordinate, color=(255, 0, 0)):
        self.dots.append(coordinate)
        self.gen_dots(coordinate, color)

    def remove_dot(self):
        coordinate = self.dots.pop()
        self.del_dots(coordinate)

    def gen_circle(self, coordinate, radius, color=(0, 255, 0)):
        thickness = 1
        cv.circle(self.img, coordinate, radius, color, thickness)
        cv.imshow(self.window, self.img)

    def gen_line(self, start, end, color=(0, 255, 0)):
        thickness = 1
        line_type = 8
        cv.line(self.img,
                start,
                end,
                color,
                thickness,
                line_type)
        cv.imshow(self.window, self.img)

    def del_line(self, start, end):
        thickness = 1
        line_type = 8
        cv.line(self.img,
                start,
                end,
                (0, 0, 0),
                thickness,
                line_type)
        cv.imshow(self.window, self.img)

    def gen_dots(self, coordinate, color=(0, 255, 0)):
        thickness = -1
        line_type = 8
        cv.circle(self.img,
                  coordinate,
                  5,
                  color,
                  thickness,
                  line_type)
        cv.imshow(self.window, self.img)

    def del_dots(self, center):
        thickness = -1
        line_type = 8
        cv.circle(self.img,
                  center,
                  5,
                  (0, 0, 0),
                  thickness,
                  line_type)
        cv.imshow(self.window, self.img)
