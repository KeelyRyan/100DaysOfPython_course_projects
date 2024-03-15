from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1)
        self.color("blue")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        y = int(self.ycor() + MOVE_DISTANCE)
        self.goto(self.xcor(), y)

    def refresh(self):
        self.goto(STARTING_POSITION)
