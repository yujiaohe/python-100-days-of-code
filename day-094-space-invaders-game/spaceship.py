import random
from turtle import Turtle
from laser import Laser


class SpaceShip(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.random(), random.random(), random.random())
        self.shapesize(1, 2)
        self.speed("fastest")
        self.penup()
        self.goto(0, -300)
        # create laser until user hit space bar
        self.laser = None
        self.clear_flag = False

    def go_left(self):
        new_x = self.xcor() - 10
        if new_x > -285:
            self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 10
        if new_x <= 280:
            self.goto(new_x, self.ycor())

    def go_up(self):
        if self.clear_flag:
            new_y = self.ycor() + 10
            if new_y < 340:
                self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 10
        if new_y > -340:
            self.goto(self.xcor(), new_y)

    def clear(self):
        self.clear_flag = True

    def shoot(self):
        if not self.laser:
            laser = Laser(position=(self.xcor(), self.ycor() + 10))
            self.laser = laser

    def remove_laser(self):
        if self.laser:
            self.laser.goto(-400, 0)
            self.laser = None

    def reset_position(self):
        self.color(random.random(), random.random(), random.random())
        self.goto(0, -300)
        if self.laser:
            self.remove_laser()
