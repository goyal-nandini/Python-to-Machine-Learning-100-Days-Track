from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 22
# 👍
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self): # a though of combining it with __init__ came but see this🖊️🗯️info.md
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)
        
    def add_segment(self, pos):
        # new_segment.shape("square") NOPE, have to do this👇
        new_segment = Turtle("square") # to make new object
        new_segment.color("white") 
    # The first thing we want to fix is that line.
    # So when we create each new segment, before we tell it to go to its position, let's go ahead and tell it to pull the pen up. This way it won't actually draw
        new_segment.penup()
        new_segment.shapesize(0.9, 0.9) # ⛎🐍 makes a snake like appearance
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position()) # NEW method used
        # position(): This method retrieves the current position (likely as an (x, y) tuple) of the last segment of the snake.
        # self.segments[-1]: This accesses the last segment of the snake. In Python, -1 is used to index the last item in a list.
        # The argument passed to add_segment is the position of the last segment, meaning the new segment will be added at the same position as the last segment.
        

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1): # backward loop
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20) # just to move head only this time 
        # self.segments[0].left(90)
    
    # i got this from q&a🙂🟢💥 try it
    # def turn(self, direction):
    #     opposite = (self.head.heading() + 180) % 360
    #     if direction != opposite:
    #         self.head.setheading(direction)

    def up(self):
        # (me)
        # for seg in self.segments:
        #     seg.right(90)
# Let's think about how we can turn the snake up. In order to turn the snake,
# the segment that we're most interested in is the first segment.
# That's basically the head of the snake
        if self.head.heading() != DOWN: # 👍
            self.head.setheading(UP)
        # it's heading to 90 degrees and then the rest of the body will follow because
# it's continuously moving on every tick of the clock.

    def down(self):
        # If it's already going up, then it's not allowed to go down.
        if self.head.heading() != UP: # rem each segement("head" is first segment) is individual turtle, and the turtle has a heading method
            self.head.setheading(DOWN) 

    def left(self):
        # If it's already going right, then it's not allowed to go left. 
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        # if it's already going left, then it's not allowed to go right.
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

# I realized that there's something about the snake game that we haven't really
# accounted for.
# And it's the fact that the snake can't move back on itself.
# It can't go forwards and then go the opposite direction because that requires
# the head to change directions.
# And this is not allowed in the official snake game.
# So how can we code this into our game?
# 👍we have to figure out when the head is pointing towards down direction,
# then we shouldn't allow it to go up. and similar for all
# So this way, even though our snake can move freely through the space, it can't go back on itself.