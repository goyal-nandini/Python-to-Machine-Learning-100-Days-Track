from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400) # used keyword argument
#💥✔️ what if the user enter wrong color
# user_bet = screen.textinput(title="Make Your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-150, -100, -50, 0, 50, 100]
turtle_list = []
is_race_start = False

# Add a finish line marker for clarity:🙂
line = Turtle()
line.hideturtle()
line.penup()
line.goto(210, -200)
line.pendown()
line.goto(210, 200)

# print(new_turtle.turtlesize()) # prints: (1.0, 1.0, 1.0) -> (stretch_wid, stretch_len, outline)
# 💥✔️Keep asking until user enters a valid color 
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
    random.shuffle(turtle_list) # 🥲😮randomize order each round
    for turtle in turtle_list:
        turtle_dist = random.randint(0, 10)
        turtle.forward(turtle_dist)

    # then check for finishers
    finishers = [turtle.pencolor() for turtle in turtle_list if turtle.xcor() > 210]

    if finishers:
        is_race_start = False
        announcer = Turtle()
        announcer.hideturtle()
        announcer.penup()
        announcer.goto(0, 150)

        if user_bet.lower() in finishers:
            # Case 1: Only one turtle finished, and it's the one you bet on
            if len(finishers) == 1:
                print(f"You've WON! The {finishers[0]} turtle is the winner!")
                announcer.write(f"You've WON!💥🔥 The {finishers[0]} turtle is the winner!",
                                align="center", font=("Arial", 12, "bold"))
            # Case 2: Multiple turtles finished together (a tie), and your bet is among them
            else:
                print(f"It's a tie! 🎉 Your bet {user_bet} was among the winners: {', '.join(finishers)}")
                announcer.write(f"It's a TIE! 🎉 Your bet {user_bet} was among the winners: {', '.join(finishers)}",
                                align="center", font=("Arial", 12, "bold"))
        else:
            # Case 3: Only one turtle finished, but it's NOT the one you bet on
            if len(finishers) == 1:
                print(f"You've LOST! The {finishers[0]} turtle is the winner!")
                announcer.write(f"You've LOST! The {finishers[0]} turtle is the winner!",
                                align="center", font=("Arial", 12, "bold"))
            # Case 4: Multiple turtles finished together (a tie), but your bet is NOT among them
            else:
                print(f"It's a tie! The winners are: {', '.join(finishers)}. Sadly your bet wasn't one of them.")
                announcer.write(f"It's a TIE! The winners are: {', '.join(finishers)}. Sadly your bet wasn't one of them.",
                                align="center", font=("Arial", 12, "bold"))


    # damn u can make a list of positions of y 🫥
    # for j in range(-150, 150, 50):
    #     print(j)
    #     tim.goto(x=-230, y=j)

screen.exitonclick()
