from turtle import Turtle

FONT = ("Courier", 18, "bold")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.goto(0, 260)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.lives = 5
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Level: {self.score} | Lives: {self.lives}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def decrease_lives(self):
        self.lives -= 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
