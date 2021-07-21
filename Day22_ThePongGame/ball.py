import random
from turtle import Turtle
colors = ["red", "pink", "green", "blue", "yellow", "orange", "white"]
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(colors[random.randint(0,len(colors)-1)])
        self.shape("circle")
        self.setposition(0,0)
        self.x_move = 10
        self.y_move = 10
    def move(self):

        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)
    def bounce(self):
        self.y_move *= -1
    def bounce_horizontal(self):
        self.x_move *= -1

