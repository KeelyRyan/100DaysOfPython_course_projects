from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.traffic = []
        #self.create_car()

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(COLORS[random.randint(0, 5)])
            new_car.goto(300, random.randint(-250, 250))
            self.traffic.append(new_car)

    def add_car(self):
        self.create_car()

    def car_move(self, x):
        for car in self.traffic:
            car.backward(STARTING_MOVE_DISTANCE * x)

    def car_remove(self):
        for car in self.traffic:
            if car.xcor() == -300:
                self.traffic.remove(car)
                car.reset()






