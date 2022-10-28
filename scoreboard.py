import os
from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')
FONT_GO = ('Courier', 16, 'bold')


def read_score():
    if os.path.exists('score.txt'):
        with open('score.txt', 'r') as f:
            return int(f.read())
    else:
        with open('score.txt', 'w') as f:
            f.write('0')
            return 0


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.higher_score = read_score()
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.pencolor("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(font=FONT, align=ALIGNMENT, move=False,
                   arg=f"Level: {self.score}  Higher score: {self.higher_score}")

    def upgrade_score(self):
        self.score += 1
        if self.score > self.higher_score:
            self.higher_score = self.score
            self.score_on_file()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(font=FONT_GO, align=ALIGNMENT, arg="GAME OVER")

    def score_on_file(self):
        with open('score.txt', "w") as my_file:
            my_file.write(str(self.higher_score))
