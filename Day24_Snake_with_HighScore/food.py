import random
from turtle import Turtle
colors = ["red", "green", "pink", "yellow", "orange","white"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        self.color(colors[random.randint(0,5)])
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
