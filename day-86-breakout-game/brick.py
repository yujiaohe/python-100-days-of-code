from turtle import Turtle

COLORS = ["yellow", "green", "orange", "red"]


class Brick(Turtle):

    def __init__(self):
        self.segments = []
        self.create_brick()

    def create_brick(self):
        for y_index in range(len(COLORS)):
            color = COLORS[y_index]
            for i in range(9):
                y = y_index * 2
                position_one = (-265 + 65 * i, 120 + 25 * y)
                position_two = (-265 + 65 * i, 120 + 25 * (y + 1))
                # print(position_one)
                # print(position_two)
                self.add_segment(position_one, color)
                self.add_segment(position_two, color)

    def add_segment(self, position, color):
        new_segment = Turtle(shape="square")
        new_segment.shapesize(1, 3)
        new_segment.color(color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def remove_segment(self, seg):
        self.segments.remove(seg)
        seg.goto(-400, 0)

