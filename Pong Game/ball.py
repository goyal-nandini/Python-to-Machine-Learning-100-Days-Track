from turtle import Turtle
from paddle import Paddle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.dx = 20
        self.dy = 20
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        # Bounce off top/bottom edge
        self.dy *= -1

    def bounce_x(self): # when ball has been touched by paddle
        self.dx *= -1
        # challenge to increase speed of ball when collision with paddle
        self.move_speed *= 0.9
    
    def reset_position(self):
        # ball to go its original position
        self.goto(0, 0)
        # have to reset the speed if one misses the ball so that speed doesn't go infinitely
        self.move_speed = 0.1
        self.bounce_x() # to go to its opposite side
        # dx negative so opp side