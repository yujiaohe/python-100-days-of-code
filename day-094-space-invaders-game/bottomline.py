from turtle import Turtle


class BottomLine(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.shapesize(0.1, 58)
        self.speed("fast")
        self.penup()
        self.goto(0, -320)
