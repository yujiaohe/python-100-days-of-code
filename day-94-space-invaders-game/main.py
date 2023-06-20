'''
Using Python Turtle, build the classic shoot 'em up game - space invaders game.
Space Invaders Wikipedia Page
https://en.wikipedia.org/wiki/Space_Invaders
Your spaceship can move left and right and it can hit some alien ships.
Every second the aliens will move closer to your ship.
Once the aliens touch your ship then it's game over.
There are usually some barriers between you and the aliens which offers you defensive positions.
You can play the game here:
https://elgoog.im/space-invaders/
'''

import time
from turtle import Screen
from spaceship import SpaceShip
from alien import Alien
from barrier import Barrier
from bottomline import BottomLine
from scoreboard import Scoreboard

# create the window
screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("Space Invaders")
# turn off animation, pairing with .update()
screen.tracer(0)

# create aliens
alien = Alien()

# create barriers
barrier = Barrier()

# create and move a spaceship
spaceship = SpaceShip()
screen.listen()
screen.onkey(key="Left", fun=spaceship.go_left)
screen.onkey(key="Right", fun=spaceship.go_right)
screen.onkey(key="Up", fun=spaceship.go_up)
screen.onkey(key="Down", fun=spaceship.go_down)
screen.onkey(key="space", fun=spaceship.shoot)

# create bottom line
bottom_line = BottomLine()

# create scoreboard
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    # spaceship.clear()  # for debug
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()
    alien.move()
    alien.create_laser()
    for alien_laser in alien.lasers:
        alien_laser.move()
    if spaceship.laser:
        spaceship.laser.move()

    # collision: spaceship laser to barriers
    if spaceship.laser:
        for bar in barrier.bars:
            if spaceship.laser.distance(bar) < 12:
                barrier.remove_bar(bar)
                spaceship.remove_laser()
                break

    # collision: spaceship laser to aliens
    if spaceship.laser:
        for seg in alien.segments:
            if spaceship.laser.distance(seg) < 11:
                alien.remove_segment(seg)
                spaceship.remove_laser()
                scoreboard.increase_score()
                break

    # collision: spaceship laser to alien laser
    if spaceship.laser:
        for al_laser in alien.lasers:
            if al_laser.distance(spaceship.laser) < 12:
                spaceship.remove_laser()
                alien.remove_laser(al_laser)
                break

    # collision: spaceship to alien
    for seg in alien.segments:
        if seg.distance(spaceship) <= 10:
            spaceship.remove_laser()
            spaceship.reset_position()
            alien.remove_segment(seg)
            scoreboard.increase_score()
            scoreboard.update_scoreboard()
            break

    # collision: alien laser to barriers
    for al_laser in alien.lasers:
        for bar in barrier.bars:
            if al_laser.distance(bar) < 12:
                alien.remove_laser(al_laser)
                barrier.remove_bar(bar)

    # collision: alien laser to spaceship
    for al_laser in alien.lasers:
        # print(al_laser.xcor(), al_laser.ycor(), al_laser.distance(spaceship))
        if al_laser.distance(spaceship) < 22:
            alien.remove_laser(al_laser)
            if scoreboard.count > 0:
                scoreboard.decrease_count()
                spaceship.reset_position()
                break
            else:  # scoreboard.count == 0
                game_is_on = False
                scoreboard.game_over()
                break

    # collision: alien laser reach bottom
    for al_laser in alien.lasers:
        if al_laser.ycor() <= bottom_line.ycor():
            alien.remove_laser(al_laser)

    # collision: alien reach bottom
    for seg in alien.segments:
        if seg.ycor() <= bottom_line.ycor():
            if scoreboard.count > 0:
                scoreboard.decrease_count()
                spaceship.reset_position()
                break
            else:
                game_is_on = False
                scoreboard.game_over()
                break

    # collision: spaceship laser reach top
    if spaceship.laser and spaceship.laser.ycor() >= 330:
        spaceship.remove_laser()

    # if barriers are cleared, alien can downward and spaceship can forward
    if not barrier.bars:
        alien.clear()
        spaceship.clear()

    # if all aliens are removed, downward
    if not alien.segments:
        alien.next_level()
        alien.create_alien()
        barrier.next_level()
        for bar in barrier.bars:
            barrier.remove_bar(bar)
        barrier.create_barrier()

screen.exitonclick()
