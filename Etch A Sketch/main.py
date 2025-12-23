# rules:
# Pressing the W key moves the turtle forwards.
# Pressing the S key moves the turtle backwards.
# Pressing the A key turns the turtle counterclockwise or leftwards.
# Pressing the D key turns the turtle clockwise or rightwards.
# This allows you to draw shapes such as straight lines or curves, mimicking the classic childhood game Etch-A-Sketch.
# C key should clear all your drawings and return the turtle to the center of the screen.
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.speed(10)

def movementW():
    tim.forward(5)

def movementS():
    tim.backward(5)

def movementA():
    tim.left(5)

def movementD():
    tim.right(5)

def movementC():
    # tim.clear()
    # tim.penup()
    # tim.home()
    tim.reset() # in place of clear() and home() 
    # tim.pendown()

# 👉 degrees() does NOT rotate the turtle
# degrees() only changes the angle unit system (degrees vs radians).
# It does nothing visible for turning.
# 👉 You must use:
# left(angle) → turn counter-clockwise
# right(angle) → turn clockwise
# 🥲curve bhi draw hoega "keep pressing" w/d or w/a :)

screen.listen()
# this onkeypress() also works mam had done onkey() only
# onkey() → step‑by‑step, tap‑based control.
# onkeypress() → smoother, continuous control when holding keys.

screen.onkeypress(fun=movementW, key="w")
screen.onkeypress(fun=movementS, key="s")
screen.onkeypress(fun=movementA, key="a")
screen.onkeypress(fun=movementD, key="d")
screen.onkeypress(fun=movementC, key="c")

screen.exitonclick()

