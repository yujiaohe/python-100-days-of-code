# Create the screen
# Create and move a paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detection when paddle misses
# Keep score

from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create and move a paddle
r_paddle = Paddle(350, 0)
# Create another paddle
l_paddle = Paddle(-350, 0)
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Create the ball and make it move
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bonce
        ball.bounce_y()

    # Detect collision with r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        # print("Made contact")
        ball.bounce_x()

    # Detection when r_paddle misses
    # Keep score
    if ball.xcor() > 380:
        # print("reset the ball")
        ball.reset_position()
        scoreboard.l_point()
    # Detection when l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()


