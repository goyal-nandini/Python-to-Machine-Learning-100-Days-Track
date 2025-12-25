from turtle import Turtle

# a finishing touch: (don't liking the hard-coded pieces of text)
ALIGNMENT = "center"
FONT = ("Chalkboard", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white") # imp
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f"Score: {self.score} 📈", align=ALIGNMENT, font=FONT)


    def increase_score(self): 
        self.score += 1
        self.clear() # the scoreboard is wipped(don't overlap on/with the previous score)
        self.update_scoreboard() # new text is written
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER 💔", align=ALIGNMENT, font=FONT)