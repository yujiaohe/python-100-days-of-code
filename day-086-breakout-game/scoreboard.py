from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")
COLOR_SCORE = {"yellow": 1,
               "green": 3,
               "orange": 5,
               "red": 7
               }


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.round = 1
        self.color("white")
        self.penup()
        self.goto(0, 340)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Round: {min(self.round, 3)}/3\t\tScore: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_round(self):
        self.round += 1
        self.update_scoreboard()

    def increase_score(self, seg_color):
        self.score += COLOR_SCORE[seg_color]
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)

