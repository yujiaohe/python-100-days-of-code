from turtle import Turtle

# ROW = 1
# COLUMN = 1
ROW = 20
COLUMN = 17

class Barrier(Turtle):

    def __init__(self):
        self.bars = []
        self.y_start = -180
        self.create_barrier()

    def create_barrier(self):
        for row in range(ROW):
            for column in range(COLUMN):
                # start position (-285, -180) with column space of 35 and row space of 10
                position = (-285 + 35 * column, self.y_start + 10 * row)
                # print(position)
                self.add_bar(position)

    def add_bar(self, position):
        new_bar = Turtle("square")
        new_bar.shapesize(0.2, 1)
        new_bar.color("yellow")
        new_bar.penup()
        new_bar.goto(position)
        self.bars.append(new_bar)

    def remove_bar(self, bar):
        self.bars.remove(bar)
        bar.goto(-400, 0)

    def next_level(self):
        if self.y_start > -240:
            self.y_start -= 5
