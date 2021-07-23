FONT = ("Courier", 24, "normal")
from turtle import Turtle
class Scoreboard(Turtle):
    global score
    score = 0
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.setposition(-250, 260)
        self.write(f"Score:{score}", font= FONT)
    def update_score(self):
        global score
        score += 1
        self.clear()
        self.write(f"Score:{score}", font=FONT)
    def game_lost(self):
        self.setposition(0,0)
        self.write(f"Game over! ", font=FONT)



