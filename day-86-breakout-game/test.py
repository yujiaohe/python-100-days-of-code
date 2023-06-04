import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.tracer(0)


tom = Turtle()
tom.shape("square")
tom.color("yellow")
tom.shapesize(1, 5)
# tom.goto(10, 10)
screen.update()
print(tom.color()[0])

screen.exitonclick()
