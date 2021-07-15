import time
from turtle import Screen
import player as pl
import car_manager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
player = pl.Player()
cars_manager = car_manager.CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_down, "Down")
    if len(cars_manager.all_cars) < 15:
        cars_manager.create_car()
    if player.ycor() >= 300:
        player.goto(pl.STARTING_POSITION)
        car_manager.MOVE_INCREMENT += 5
        pl.MOVE_DISTANCE += 5
        score.increase_lvl()
    for car in cars_manager.all_cars:
        if car.xcor() - 35 <= player.xcor() <= car.xcor() + 15 and car.ycor() - 15 <= player.ycor() <= car.ycor() + 15:
            car.color("red")
            game_is_on = False
            score.game_over()
    cars_manager.move_cars()
    time.sleep(0.1)
    screen.update()
screen.exitonclick()