import turtle
from turtle import Turtle, Screen
import random

# import colorgram
#
# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     rgb = color.rgb
#     rgb_colors.append((rgb.r, rgb.g, rgb.b))
#
# print(rgb_colors)


def draw_square():
    """Turtle Challenge - Draw a Square"""
    tim = Turtle()
    for _ in range(4):
        tim.right(90)
        tim.forward(100)


def draw_dashed_line():
    """Turtle Challenge 2 - Draw a dashed line"""
    tim = Turtle()
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


def draw_different_shapes():
    """Turtle Challenge 3 - Draw Different Shapes"""
    tim = Turtle()
    for nums in range(3, 11):
        angle = 360 / nums
        r = random.random()
        g = random.random()
        b = random.random()
        tim.pencolor((r, g, b))
        for _ in range(nums):
            tim.forward(100)
            tim.right(angle)


def generate_random_walk():
    """Turtle Challenge 4 - Generate a Random Walk"""
    tim = Turtle()
    tim.width(10)
    tim.speed("fastest")
    angles = [0, 90, 180, 270]
    for _ in range(200):
        tim.pencolor(random_color())
        tim.forward(30)
        tim.setheading(random.choice(angles))


def random_color():
    """Return a tuple with rgb value between (0, 1)"""
    r, g, b = random.random(), random.random(), random.random()
    tup = (r, g, b)
    return tup


def draw_spirograph(size_of_gap=5):
    """Turtle Challenge 5 - Draw a Spirograph"""
    tim = Turtle()
    tim.speed("fastest")
    for _ in range(360 // size_of_gap):
        tim.color(random_color())
        tim.circle(100)
        tim.left(size_of_gap)


color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160),
              (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32),
              (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19),
              (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162),
              (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85),
              (145, 227, 216), (122, 193, 148), (102, 220, 229),
              (221, 178, 216), (253, 197, 0), (80, 135, 179)]


def hirst_painting():
    """Hirst painting"""
    # 10 * 10 spot
    # 20 inside, 50 space
    tim = Turtle()
    turtle.colormode(255)
    tim.speed("fastest")
    tim.penup()
    tim.hideturtle()
    start_x = -200
    start_y = -200
    tim.goto(start_x, start_y)
    for y in range(0, 10):
        for x in range(0, 10):
            tim.goto(x * 50 + start_x, y * 50 + start_y)
            tim.dot(20, random.choice(color_list))


draws = {
    1: draw_square,
    2: draw_dashed_line,
    3: draw_different_shapes,
    4: generate_random_walk,
    5: draw_spirograph,
    6: hirst_painting,
}

print("Play with python turtle module")
for key, value in draws.items():
    print(f"{key}. {value.__name__}")
choice = int(input("Type 1-5 for different shapes: "))
draws[choice]()

screen = Screen()
screen.exitonclick()
