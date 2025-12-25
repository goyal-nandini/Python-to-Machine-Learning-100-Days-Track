from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 My Snake Game 🐍")


segments = []
screen.tracer(0) # stop automatic screen refresh

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up") # so now going to class and implementing there :)
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

   
game_is_on = True
while game_is_on:
    screen.update() # manually refresh screen once, Without calling update(), nothing appears to move.
    time.sleep(0.1) # controls speed, a timer to delay the refresh so that we can control how often it happens
  
    snake.move()
    
    # todo 6: detect collison with food
    if snake.head.distance(food) < 15: # Return the distance from the turtle to (x,y), the given other turtle, in turtle step units.
        # print("nom nom nom")
        # gpto a new position
        food.refresh()
        snake.extend() 
        scoreboard.increase_score()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
  
    # or optimise the above for loop!! using slicing
    for segment in snake.segments[1:]:  # Skip the head
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()    
        

# more: Create initial snake body
# snake_body = []
# for i in range(3):
#     body_segment = Turtle('square')
#     body_segment.color('white')
#     x_offset = -20 * len(snake_body)
#     body_segment.goto(x_offset, 0)
#     snake_body.append(body_segment)

# TODO 2: move our snake automatically across the screen without having to do anything.
# challenge: all segments moving separately/flickery effect -> tracer() update() time.slee()(for speed)
# challenge: how do we turn our snake? -> 
# head turns rest of body moves away from head, the segemts are not linked
# have to rethink about their turn: intuition:
# body movement happens before head movement.
# Body logic:
# “Go to the position where the segment in front of you WAS.”
# Turning the snake means changing only the head’s direction; the body follows automatically by copying previous positions, which creates the turning effect.

# TODO 3: tidy up the code, OOPS :)
# TODO 4: control the snake :) up, down, right, left
# day 2
# TODO 5: Food class (random food on scree)
# TODO 6: TO detect when the snake and the food have come into contact, and then to tell the food to move itself to a new random location?
# TODO 7: create a scoreboard and manage it for the game
# TODO 8: detect collision with the wall
# TODO 9: detect collison with its tail -> adding add_segment() and extend() method in snake class

screen.exitonclick()
