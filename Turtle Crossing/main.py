import time
from turtle import Screen, Turtle
from player import Player
from car_shape_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

turtle = Player()
screen.listen()
screen.onkeypress(fun=turtle.move_up, key="Up")

# the other side of screen -> green line
# on the player side -> a red line
def draw_lines():
    drawer = Turtle()
    drawer.hideturtle()
    drawer.speed("fastest")
    drawer.penup()

    # Starting line (red) at bottom
    drawer.goto(-300, -250)   # left bottom
    drawer.pendown()
    drawer.color("red")
    drawer.pensize(5)
    drawer.forward(600)       # draw across screen
    drawer.penup()

    # Finish line (green) at top
    drawer.goto(-300, 250)    # left top
    drawer.pendown()
    drawer.color("green")
    drawer.pensize(5)
    drawer.forward(600)       # draw across screen
    drawer.penup()

# 📍restart pause resume :)

draw_lines()

# Game heading:
heading = Turtle()
heading.hideturtle()
heading.penup()
heading.goto(0, 270)
heading.color("yellow")
heading.write("Turtle Crossing Game", align="center", font=("Courier", 20, "bold"))

cars = CarManager()

# # create 10 cars
# for _ in range(10):
#     cars.car_creation()

# # move them
# for _ in range(50):
#     cars.car_motion()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.car_creation() # one car is created in every 0.1 second
    cars.car_motion()
    scoreboard.show_level()

    # collision with car
    # distance() works fine, but you must call it with a Turtle instance (like car), not the manager object.
    for car in cars.all_cars:
        if turtle.distance(car) < 20:
            scoreboard.game_over()
            cars.clear_all() # no working 🔴
            game_is_on = False
    
    
    # player reaches finish line -> restart the game
    if turtle.ycor() > 250:
        turtle.goto(0, -280) # reset player to start position
        # for car in cars.all_cars:
        cars.level_up() # increases car speed once
        scoreboard.level_up() # update level

        
screen.exitonclick()
