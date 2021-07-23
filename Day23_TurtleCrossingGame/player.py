STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("Lightblue")
        self.setheading(90)
        self.setposition(0, -280)
    def reset_player(self):
        self.goto(0, -280)
    def move_up(self):
        new_cor = self.ycor()+10
        self.goto(0,new_cor)


