import time
from turtle import Screen
from road import Road
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
#screen.bgcolor("gray")
screen.bgpic("road.png")
screen.title("Turtler")
screen.tracer(0)
#lines = Road()

scoreboard = Scoreboard()
screen.listen()
new_car = CarManager()
player1 = Player()
screen.onkeypress(player1.up, "Up")

game_is_on = True
x = 1
while game_is_on:
    time.sleep(0.1)
    screen.update()

    new_car.add_car()
    new_car.car_move(x)
    new_car.car_remove()

    for car in new_car.traffic[1:]:
        if player1.distance(car) < 20:
            scoreboard.decrease_lives()
            if scoreboard.lives == 0:
                scoreboard.game_over()
            player1.refresh()


    # update scores
    if player1.ycor() > 290:
        scoreboard.increase_score()
        player1.refresh()
        x += 1




