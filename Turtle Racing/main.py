from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-150, -100, -50, 0, 50, 100]
turtle_list = []
is_race_start = False

user_bet = None 
while user_bet not in colors: 
    user_bet = screen.textinput( 
        title="Make Your Bet", 
        prompt=f"Which turtle will win the race? Choose from: {', '.join(colors)}" 
    )

if user_bet:
    is_race_start = True

# create turtles
for i in range(6):
    # hmm tim for all turtles nope, we've change to new_turtle
    # 6 new turtle being ready for the race!!
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[i])
    turtle_list.append(new_turtle)
    # lets make each of turtle to move!!

while is_race_start:
    random.shuffle(turtle_list) # randomize order each round
    # here using _ will also make one turtle move...
    # for _ in turtle_list: -> NOO
    for turtle in turtle_list: # iterate over each turtle
        # have to stop the race at finish line (x=210) and declare the winner
        if turtle.xcor() > 210: # at 250 its edge of screen, 40 is the size of turtle(40*40)
            is_race_start = False 
            winner = turtle.pencolor() # getting winner
            if winner == user_bet.lower():
                # 💥✔️wanted to display the winner on the turtle screen
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")
            
            # 💥✔️
            # 🖊️ Create a writer turtle to display text 
            announcer = Turtle() 
            announcer.hideturtle() 
            announcer.penup() 
            announcer.goto(0, 150) # position at top of screen 
            if winner == user_bet: 
                announcer.write(f"You've WON!💥🔥 The {winner} turtle is the winner!", 
                align="center", 
                font=("Arial", 16, "bold")) 
            else: announcer.write(f"You've LOST! The {winner} turtle is the winner!", 
                align="center", 
                font=("Arial", 16, "bold"))
        turtle_dist = random.randint(0, 10)
        turtle.forward(turtle_dist) # uff it makes only one turtle to move!!
    # lets make a list of them to make them move in race at random dist generated :)


    # damn u can make a list of positions of y 🫥
    # for j in range(-150, 150, 50):
    #     print(j)
    #     tim.goto(x=-230, y=j)

screen.exitonclick()

'''check this:
The for loop iterates over turtles in order: first turtle in the list, then the second, and so on.

If the first turtle crosses the finish line, the race ends immediately (is_race_start = False).

That means turtles later in the list don't get their move in that same round.
→ So yes, the winner has effectively run x rounds, while some others only ran x-1 rounds.

⚖️ Why this matters
This introduces a tiny "bias":

The first turtle in the list has a slight advantage because it always gets checked first.

If two turtles are neck-and-neck, the earlier one in the list will be declared the winner even if the later one would have crossed the line in the same round.
'''
