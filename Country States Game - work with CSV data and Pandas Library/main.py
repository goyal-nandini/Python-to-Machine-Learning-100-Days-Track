import turtle
import pandas

screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

# screen.bgpic('blank_states_img.gif') 
# also works and saves a line of code

turtle.shape(image)

# lets work with user answer and actual ans in csv file
states = pandas.read_csv("50_states.csv")

game_is_on = True
score = 0

guessed_states = []
# Default prompt 
prompt_message = "What's another state's name?\nType 'Exit' to exit!📤"

# while game_is_on: # u can'r run it infinite times it should be off after user has guessed all 50 sates
while len(guessed_states) < 50:
 
    answer_state = screen.textinput( 
        title=f"{score}/50 Guess the State",
        prompt=prompt_message 
    )
    # answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name?\nType 'Exit' to exit!📤")

    # Case 1: user cancels or enters nothing 
    if not answer_state: 
        # Update prompt to show a warning 
        prompt_message = "Please enter a state name!" 
        continue 
 
    answer_state = answer_state.title()
    # Case 2: duplicate guess 
    if answer_state in guessed_states: 
        prompt_message = f"You already guessed {answer_state}! Try another."
        continue

    # case 3: wanne exit
    if answer_state == "Exit":
        # remaining states to learn.csv
        remaining_states = states[~states.state.isin(guessed_states)].state.to_list() # have to use .state at end as to_list() works on series not on dataframe
        # or mam used
        # remaining_states = []
        # for state in states.state.to_list():
        #     if state not in gueseed_states:
        #         remaining_states.append(state)

        data_to_csv = pandas.DataFrame(remaining_states)
        data_to_csv.to_csv("learn.csv")
        break
    
    # states.state is a pandas series
    # states.state.values gives a NumpyArray -> Pandas does not recommend using it anymore
    # states.state.to_list() gives a Pyhton List -> Pandas-recommended

    # print(states.state.values) # a list of state column
    # In pandas, .values gives you the underlying NumPy array of a Series or DataFrame.

    # mam used
    all_states = states.state.to_list() # python list


    # case: valid new state
    if answer_state in states.state.values:
        guessed_states.append(answer_state)
        state_data = states[states.state == answer_state] # pull out the row where the state is equal to answer_state

        # Now this is about extracting a single value from Pandas.
        # xcor = state_data.x # this is a pandas series from our dataframe "states", not single numbers
        # ycor = state_data.y
        # print(xcor, ycor)

        # mam used this, not .values[0] also no int() cpnversion needed
        # .item() directly extracts the single value, converts it into pyhton native type☀️
        # AND used When exactly one value is guaranteed
        xcor = state_data.x.item()
        ycor = state_data.y.item()

        # AVOID IT yet here, .values -> NumpyArray and [0] first ele ,for int()👇☀️
        # xcor = int(state_data.x.values[0])
        # ycor = int(state_data.y.values[0])

        # or u can used this .iloc its is "integer location" for iloc
        # it is index-based selection in pandas, returns python native value☀️, not a series, not numpy array
        # xcor = state_data.x.iloc[0]
        # ycor = state_data.y.iloc[0] # Works even if Series has multiple values

        score += 1
        prompt_message = "What's another state's name?\nType 'Exit' to exit!📤" # reset after a valid guess

        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(xcor, ycor)
        writer.write(answer_state, align="center", font=("Arial", 14, "normal"))  # keep it normal not Normal OKAY !!                                        
        


# see we have a csv file which has got coordinates of the particular point on the screen
# (as per each state on the country map) so the code to detect the mouse click coordinates
# we do as follows:
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop() # this is an alternative way of keeping our screen open
# even though our code has finished running.
# So it's basically an alternative to our screen.exitonclick.

# screen.exitonclick() # no use 

'''👇📍
why int() ?? the type conversion...!!??
state_data.x.values[0] is usually a NumPy type (like numpy.int64 or numpy.float64), not a plain Python int.

Turtle's goto(x, y) expects regular Python numbers (int or float).
Most of the time, NumPy numbers work fine, but occasionally they can cause type issues or formatting quirks.
'''
