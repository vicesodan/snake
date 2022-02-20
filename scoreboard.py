from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.points = 0
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.points}", False, "center", ("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Arial", 18, "normal"))

    def plus_point(self):
        self.points += 1
        self.clear()
        self.update_scoreboard()