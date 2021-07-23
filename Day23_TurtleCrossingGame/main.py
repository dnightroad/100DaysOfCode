import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
player = Player()
score = Scoreboard()
#screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move_up,"Up")
#settings for the car for loop
starting_position = -30
starting_x = 280

cars = []

game_is_on = True


for car in range(1,18):
    random_start = random.randrange(20, 150)
    car = CarManager()
    new_ycor = car.ycor() - starting_position
    car.goto(starting_x+random_start, new_ycor)
    cars.append(car)
    starting_position -=30
new_cars = []
for element in range(0,17):
    i = random.randint(0,16)
    new_cars.append(cars[i])

while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move(car.ycor())
        if car.xcor()<-280:
            new_x = 280
            car.goto(new_x, car.ycor())
        if car.distance(player)<30:
            score.game_lost()
            game_is_on = False
    for car in new_cars:
      car.move(car.ycor())
      if car.distance(player) < 20:
          score.game_lost()
          game_is_on = False
    if player.ycor()> 280:
        score.update_score()
        player.reset_player()


screen.exitonclick()
