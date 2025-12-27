from turtle import Turtle
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.penup()
        self.level = 1
          
    def level_up(self):
        self.level += 1
        self.show_level()

    def show_level(self):
        self.goto(-280, 250)
        self.clear()
        self.write(f"Level: {self.level}💪", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.color("red")
        self.goto(0, 0)
        self.write("💔GAME OVER💔", align="center", font=FONT)
        self.goto(0, -50)
        self.color("yellow")
        self.write(f"YOUR LEVEL: {self.level}", align="center", font=FONT)

    
