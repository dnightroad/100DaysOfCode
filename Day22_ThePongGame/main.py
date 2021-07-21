from turtle import Screen, onkey
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=620)
screen.title("The Awesome Pong")
screen.tracer(0)

left_paddle = Paddle()
left_paddle.setposition(-350, 0)
right_paddle = Paddle()
right_paddle.setposition(350, 0)

ball = Ball()
score = Score()
game_is_on = True
def go_up():
    new_y = right_paddle.ycor()+20
    right_paddle.goto(right_paddle.xcor(), new_y)
def go_down():
    new_y = right_paddle.ycor()-20
    right_paddle.goto(right_paddle.xcor(), new_y)
def go_up_left():
    new_y = left_paddle.ycor()+20
    left_paddle.goto(left_paddle.xcor(), new_y)
def go_down_left():
    new_y = left_paddle.ycor()-20
    left_paddle.goto(left_paddle.xcor(), new_y)
#Player1 will use the arrows, player 2 will use 'w' for up and 's' for down
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_up_left, "w")
screen.onkey(go_down_left, "s")
player_2 = 0
player_1 = 0
while game_is_on:
    time.sleep(0.08)
    screen.update()
    ball.move()
    #detect collision with wall
    if ball.ycor()>=280 or ball.ycor() <= -280:
        ball.bounce()
    #detect collition with the paddles
    if ball.distance(right_paddle)<60 and ball.xcor()> 320 or ball.distance(left_paddle)<60 and ball.xcor() < -320:
        ball.bounce_horizontal()
    if ball.xcor() > 350:
        score.increase_score(2)
        ball.goto(0,0)
    if ball.xcor() < -350:
        score.increase_score(1)
        ball.goto(0, 0)
    #define winner
    if score.score_1 >= 6:
        score.goto(0,0)
        score.write("Winner is PLayer 1", align="center", font=("Ariel", 45, "normal"))
        game_is_on = False
    if score.score_2 >= 6:
        score.goto(0,0)
        score.write("Winner is Player 2", align="center", font=("Ariel", 45, "normal"))
        game_is_on = False










screen.exitonclick()