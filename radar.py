from canvas import Canvas
import math
import numpy as np
import schedule


class Radar:
    def __init__(self, sensor_max_distance_cm):
        self.W = 1000
        H = self.W
        margin = 20
        radar_window = "Radar"
        self.dimensions = self.W, H, 3
        self.image = np.zeros(self.dimensions, dtype=np.uint8)
        self.center = self.W // 2
        self.center_coord = (self.center, self.center)
        self.dot_radius = 5
        self.dots = []
        self.lines = []
        self.circle_radius = self.W // 2 - margin
        self.cm_to_px_factor = self.circle_radius // sensor_max_distance_cm
        self.canvas = Canvas(radar_window, self.image, margin, self.W, circle_radius=self.circle_radius,
                             sensor_max_distance_cm=sensor_max_distance_cm)
        self.canvas.update_canvas()

    def clean_up_lines(self):
        line_count = len(self.lines)
        if line_count == 0:
            return
        for i in range(line_count):
            coordinate = self.lines.pop(0)
            self.canvas.del_line((self.center, self.center), coordinate)

    def clean_up_dots(self):
        dot_count = len(self.dots)
        if dot_count == 0:
            return
        for i in range(dot_count):
            coordinate = self.dots.pop(0)
            self.canvas.del_dots(coordinate)

    def calc_draw_point(self, degree, distance_in_cm):
        distance_in_px = distance_in_cm * self.cm_to_px_factor
        coordinate = None
        if 0 < distance_in_px <= self.circle_radius:
            coordinate = self.calc_coord_by_degree(degree, distance_in_px)
            self.dots.append(coordinate)
            self.canvas.gen_dots(coordinate, radius=self.dot_radius)
        elif distance_in_px > self.circle_radius or distance_in_px < 0:
            coordinate = self.calc_coord_by_degree(degree, self.circle_radius)

        self.canvas.gen_line(self.center_coord, coordinate)
        self.lines.append(coordinate)
        self.canvas.update_canvas()

    def calc_coord_by_degree(self, degree, distance):
        angle_radians = degree * math.pi / 180
        x2 = self.center + distance * math.cos(angle_radians)
        y2 = self.center + distance * math.sin(angle_radians)
        coordinate = (int(x2), int(y2))
        return coordinate
