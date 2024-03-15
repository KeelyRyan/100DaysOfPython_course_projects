from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 10, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.score = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score  :
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
