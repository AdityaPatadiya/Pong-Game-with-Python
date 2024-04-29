from turtle import Turtle
FONT = ("Arial", 20, "normal")


class player_score(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 220)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
