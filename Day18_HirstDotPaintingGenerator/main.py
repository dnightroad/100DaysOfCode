import random
import turtle
from turtle import Turtle, Screen
import colorgram

screen = Screen()
screen.screensize(400, 200)
tim = Turtle(visible=False)
tim.speed(0)
turtle.colormode(255)
tim.pencolor("white")
color_list = colorgram.extract('hirst.jpg', 60)
color_palette = []
for count in range(len(color_list)):
    rgb = color_list[count]
    color = rgb.rgb
    color_palette.append(color)
all_colors = len(color_palette)


def draw(space, x):
    for i in range(x):
        for j in range(x):
            color = color_palette[random.randrange(0, all_colors)]
            tim.begin_fill()
            tim.fillcolor(color.r, color.b, color.g)
            tim.circle(10)
            tim.end_fill()

            tim.forward(space)
        tim.backward(space * x)
        tim.right(90)
        tim.forward(space)
        tim.left(90)


tim.penup()
draw(30, 8)

screen.exitonclick()
