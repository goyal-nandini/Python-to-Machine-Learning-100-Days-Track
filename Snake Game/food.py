from turtle import Turtle
import random

class Food(Turtle): # Now we've actually created our food class and we've inherited from the turtle class.
# What that means is we can now start using things that are from the turtle class.
    def __init__(self):
        # called the Turtle's init method inside the Food's init method
        super().__init__() # superclass's call
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # 20by20 to 10by10
        # The default size of a turtle in Python is 20 by 20 pixels. BUT I USED 40 in racing as per mam did 🤔
        self.color("blue")
        self.speed("fastest")
        # random_x = random.randint(-280, 280) # we have 600 by 600 and origin at center don't want food at edges so 
        # # shifter by 20 from all 4 sides
        # random_y = random.randint(-280, 280)
        # self.goto(random_x, random_y)
        self.refresh() # don't write "reset", thats from Turtle class

    # def refresh(self): # mam did this
    #     random_x = random.randint(-280, 280) # we have 600 by 600 and origin at center don't want food at edges so 
    #     # shifter by 20 from all 4 sides
    #     random_y = random.randint(-280, 280)
    #     self.goto(random_x, random_y)
    # This is suitable when you want the food to appear at any position within the range, without restrictions on spacing.

    # this is better for snake game    (got from q&a)
    def refresh(self):
        random_x = random.randrange(-280, 280, 20)
        random_y = random.randrange(-280, 280, 20)
        self.goto(random_x, random_y)
    # This is suitable when you want the food to align with a grid (e.g., in a game like Snake, where the movement is in steps of 20).
'''Which to Use?
If the game or application requires grid alignment (e.g., Snake game), use random.randrange with a step size.
If the positions can be anywhere within the range, use random.randint.'''
