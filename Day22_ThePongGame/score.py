from turtle import Turtle
player_1 = 0
player_2 = 0
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.hideturtle()
        self.score_1 =0
        self.score_2 = 0
        self.write(f"Score:{self.score_1}:{self.score_2}", align="center", font=("Ariel", 45, "normal"))
    def increase_score(self,player):
        self.clear()
        if player == 1:
            self.score_1+=1
            self.write(f"Score:{self.score_1}:{self.score_2}",align="center", font=("Ariel", 45, "normal"))
        if player == 2:
            self.score_2 += 1
            self.write(f"Score:{self.score_1}:{self.score_2}",align="center", font=("Ariel", 45, "normal"))
