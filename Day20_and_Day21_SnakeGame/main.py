##the Snake Game
import time
import turtle
from turtle import Screen
from food import Food
from snake import Snake
from food import *
from score import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The cool Snake Game")
screen.tracer(0)
snake = Snake()
food=Food()
score = Score()
turtle.listen()

screen.update()
game_is_on = True
hungry_snake = True
while game_is_on == True:
    screen.update()
    time.sleep(0.20)

    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()


    #detect collision with wall
    if snake.move()== False:
        pen = turtle.Turtle()
        pen.color("white")
        pen.write("GAME OVER :(", font=("Calibri", 15))
        game_is_on = False
    #detect collision with the tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            pen = turtle.Turtle()
            pen.color("white")
            pen.write("GAME OVER :(", font=("Calibri", 15))
            game_is_on = False















screen.exitonclick()
