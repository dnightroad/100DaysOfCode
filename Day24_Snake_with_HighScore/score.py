from turtle import Turtle
counter = 0
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0,250)
        self.hideturtle()
        self.score =0
        with open('./score.txt') as hight_score:
            self.h_score = hight_score.read()

        self.write(f"Score:{self.score} High score:{self.h_score}", font=("Calibri", 25, "normal"), align="center")

    def update_hight_score(self):
        if self.score > int(str(self.h_score)):
            with open('./score.txt', 'w') as hight_score:
                hight_score.write(str(self.score))


    def increase_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score:{self.score}  High score:{self.h_score}", font=("Calibri", 25, "normal"), align="center")
