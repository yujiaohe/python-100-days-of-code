import random
from turtle import Turtle
from laser import Laser

# LIMIT = 0
# ROW = 1
# COLUMN = 1
# how many alien can shoot laser at the same time
LIMIT = 5
ROW = 5
COLUMN = 11


class Alien(Turtle):

    def __init__(self):
        self.segments = []
        self.lasers = []
        self.x_move = 3
        self.y_move = 0
        self.y_start = 170
        self.create_alien()
        self.create_laser()
        self.clear_flag = False

    def next_level(self):
        if self.y_start > 35:
            self.y_start -= 5
        self.x_move += 2

    def create_alien(self):
        for row in range(ROW):
            for column in range(COLUMN):
                position = (-265 + 30 * column, self.y_start + 40 * row)
                self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("turtle")
        new_segment.color("green")
        new_segment.setheading(270)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def clear(self):
        self.clear_flag = True

    def downward(self):
        self.y_move = -5

    def move(self):
        for seg in self.segments:
            new_x = seg.xcor() + self.x_move
            if new_x > 280 or new_x < -280:
                self.x_move *= -1
                if self.clear_flag:
                    self.downward()
                break
        for seg in self.segments:
            new_x = seg.xcor() + self.x_move
            new_y = seg.ycor() + self.y_move
            seg.goto(new_x, new_y)
        self.y_move = 0

    def remove_segment(self, seg):
        self.segments.remove(seg)
        seg.goto(-400, 0)

    def get_first_row(self):
        fist_row = {}
        for seg in self.segments:
            x = seg.xcor()
            y = seg.ycor()
            if x not in fist_row:
                fist_row[x] = y
            elif y < fist_row[x]:
                fist_row[x] = y
        return fist_row

    def create_laser(self):
        first_row = self.get_first_row()
        shooter = []
        for seg in self.segments:
            if seg.xcor() in first_row and seg.ycor() == first_row[seg.xcor()]:
                shooter.append(seg)
        seg = random.choice(shooter)
        if len(self.lasers) < LIMIT:
            laser = Laser(position=(seg.xcor(), seg.ycor() - 10), mode="alien")
            self.lasers.append(laser)

    def remove_laser(self, laser):
        self.lasers.remove(laser)
        laser.goto(-400, 0)
        self.create_laser()
