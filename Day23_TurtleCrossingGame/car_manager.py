import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=2)
        self.color(COLORS[random.randint(0, len(COLORS)-1)])
        new_x = random.randrange(250, 390)
        self.setposition(new_x, -270)


    def move(self, y):
        new_x = self.xcor()-STARTING_MOVE_DISTANCE
        self.goto(new_x, y)


