from turtle import Turtle

POSITIONS = ((190, 200), (0, -200), (190, -200), (-190, -200), (0, 200), (-190, 200),
             (190, 0), (0, 0), (-190, 0))


class Road(Turtle):

    def __init__(self):
        super().__init__()
        self.lines = []
        self.create_road()

    def create_road(self):
        for position in POSITIONS:
            self.add_line(position)

    def add_line(self, position):
        new_line = Turtle("square")
        new_line.color("white")
        new_line.shapesize(1, 6)
        new_line.penup()
        new_line.goto(position)
        self.lines.append(new_line)
