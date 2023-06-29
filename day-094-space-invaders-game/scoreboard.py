from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.count = 3
        self.color("white")
        self.penup()
        self.goto(0, -360)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Life remain: {self.count}\t\t\t\t\t\tScore: {self.score}", align=ALIGNMENT, font=FONT)

    def decrease_count(self):
        self.count -= 1
        self.update_scoreboard()

    def increase_score(self):
        self.score += 20
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)