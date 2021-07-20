from turtle import Turtle
counter = 0
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0,270)
        self.hideturtle()
        self.score =0
        self.write(f"Score:{self.score}", font=("Calibri", 25, "normal"))
    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score:{self.score}", font=("Calibri", 25, "normal"))