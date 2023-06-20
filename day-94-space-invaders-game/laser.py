from turtle import Turtle


class Laser(Turtle):

    def __init__(self, position, mode="spaceship"):
        super().__init__()
        self.shape("square")
        self.shapesize(0.8, 0.1)
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(position)
        self.y_move = 10
        if mode == "alien":
            self.color("blue")
            self.y_move = -10

    def move(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    def remove(self):
        self.goto(-400, 0)
