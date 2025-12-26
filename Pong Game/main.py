# TODO setup the screen
# TODO create a paddle and move it
# TODO refract the code and make another paddle
# TODO create the ball and move it
# TODO tricky part: detect collision wall and bounce
# TODO detect collision with paddle: hardest part of logic
# TODO Detect if the ball goes out of bounds at the edge of the screen
# If yes then reset the bowls position to the centre of the screen 
# The ball should then start moving towards the other player
# TODO prepare score board 
# TODO increase the speed if ball hits the paddle

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("green")
screen.title("Pong")


# 1. animation turned off
screen.tracer(0) # tracer controlls the animation
# when used with 0 as arg, the animations turned off
# if u turn off the animation, then u have to manually update the screen and 
# refresh it every single time -> see below while loop 💪

# Central dashed line
turtle = Turtle()
turtle.pencolor("white")
turtle.pensize(10)
turtle.hideturtle()
turtle.penup()
turtle.setheading(270)
turtle.backward(300)
 
for i in range(15):
    turtle.pendown()
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)

# 2. paddle get created in the background
# goes to paddle class
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# paddle = Turtle()
# paddle.penup()
# paddle.color("white")
# paddle.shape("square")
# # original -> 20 by 20 so width=20 and height=100 
# paddle.shapesize(stretch_wid=5, stretch_len=1, outline=3)

# paddle.goto(x=350, y=0)

# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)

# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
 

# 3. at this point we actually updae the screen and show wverything that happened in the background so far...!!
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # collision with wall 
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # collision with both paddle 
    # distance function measures from the center of the ball and from the center of the paddle hence have to add one more cond
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        print(ball.distance(r_paddle))
        ball.bounce_x()

    
    # detect if right paddle misses -> score goes to left one and vice versa
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    # detect if left paddle misses -> its in separate condition because
    # later on we need to detect when the right-sided or left-sided
    # actually gains a point
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
