import canvas
import math
import numpy as np
import schedule

cm_to_px_factor = 10


class Radar:
    def __init__(self):
        W = 500  # fixme: yo wtf andere waarden dan 500 verneukt de lijnen
        H = W
        margin = 10
        radar_window = "Radar"
        self.dimensions = W, H, 3
        self.image = np.zeros(self.dimensions, dtype=np.uint8)
        self.center = W // 2
        self.center_coord = (self.center, self.center)
        self.canvas = canvas.Canvas(radar_window, self.image, margin, W)
        self.canvas.update_canvas()
        self.dot_radius = 5
        self.dots = []
        self.lines = []

    def clean_up_lines(self):
        line_count = len(self.lines)
        if line_count == 0:
            return
        for i in range(line_count):
            coordinate = self.lines.pop(0)
            # coordinate_processed = (coordinate[0] - self.dot_radius, coordinate[1] - self.dot_radius)
            self.canvas.del_line((self.center, self.center), coordinate)

    def clean_up_dots(self):
        dot_count = len(self.dots)
        if dot_count == 0:
            return
        for i in range(dot_count):
            coordinate = self.dots.pop(0)
            self.canvas.del_dots(coordinate)

    def calc_draw_point(self, degree, distance):
        coordinate = self.calc_coord_by_degree(degree, distance)
        self.dots.append(coordinate)
        self.lines.append(coordinate)
        self.canvas.gen_line(self.center_coord, coordinate)
        self.draw(coordinate)

    def calc_coord_by_degree(self, degree, distance):
        # 1cm = cm_to_px_factor
        distance = distance * cm_to_px_factor
        angle_radians = degree * math.pi / 180
        x2 = self.center + distance * math.cos(angle_radians)
        y2 = self.center + distance * math.sin(angle_radians)
        coordinate = (int(x2), int(y2))
        return coordinate

    def draw(self, coordinate):
        # self.canvas.del_line(self.center_coord, coordinate)
        self.canvas.gen_dots(coordinate, radius=self.dot_radius)
        self.canvas.update_canvas()
