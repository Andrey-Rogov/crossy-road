from turtle import Turtle
from random import choice, randint

COLORS = ["orange", "black", "green", "blue", "purple"]
MOVE_DISTANCE = 10
MOVE_INCREMENT = 0


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        chance = randint(1, 10)
        if chance == 5:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(choice(COLORS))
            y_position = randint(-250, 220)
            for car in self.all_cars:
                if car.ycor() - 5 <= y_position <= car.ycor() + 5:
                    y_position += 5
            new_car.goto(300, y_position)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(MOVE_DISTANCE + MOVE_INCREMENT)
            if car.xcor() <= -450:
                car.goto(300, randint(-250, 250))
                # to = randint(-250, 250)
                # for item in self.all_cars:
                #     if item.ycor() - 5 <= to <= item.ycor() + 5:
                #         to -= 5
