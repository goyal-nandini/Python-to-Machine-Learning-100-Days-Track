from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.pos = position
        self.create_paddle()
    
    def create_paddle(self):
        self.penup()
        self.color("blue")
        self.shape("square")
        # original -> 20 by 20 so width=20 and height=100 
        self.shapesize(stretch_wid=5, stretch_len=1, outline=3)

        self.goto(self.pos)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
