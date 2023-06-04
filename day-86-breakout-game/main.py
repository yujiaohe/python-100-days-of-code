from turtle import Screen
from ball import Ball
from paddle import Paddle
from brick import Brick
from scoreboard import Scoreboard
import time

# create the window
screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("Breakout")
# turn off animation, pairing with .update()
screen.tracer(0)


# create and move a paddle
paddle = Paddle()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

# create colorfully bricks
brick = Brick()
# create the ball and make it move
ball = Ball()
# create scoreboard
scoreboard = Scoreboard()

# when touch_count reach 4 and 12, increase ball.move_speed
touch_count = 0
while scoreboard.round < 4:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    orange_red_flag = False
    # detect collision with wall and bounce, left and right wall
    if ball.xcor() > 280 or ball.xcor() < -280:
        ball.bounce_x()
    # upper wall
    if ball.ycor() > 380:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddle) < 45 and ball.ycor() < -290:
        ball.bounce_y()

    # detect collision with bricks and score
    for seg in brick.segments:
        if ball.distance(seg) < 30:
            ball.bounce_y()
            brick.remove_segment(seg)
            touch_count += 1
            print(f"touch_count={touch_count}")
            seg_color = seg.color()[0]
            orange_red_flag = seg_color in ["orange", "red"]
            print(f"color_flag: {orange_red_flag}")
            # keep score and update scoreboard
            scoreboard.increase_score(seg_color)
            scoreboard.update_scoreboard()
            # increase ball move speed
            if touch_count == 4 or touch_count == 12 or orange_red_flag:
                ball.increase_move_speed()
                print(f"ball move speed:{ball.move_speed}")

    # detection with paddle miss
    if ball.ycor() < -350:
        ball.reset_position()
        scoreboard.increase_round()

scoreboard.game_over()
screen.exitonclick()

