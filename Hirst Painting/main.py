# colorgram.py is a Python library that lets you extract colors from images
import colorgram

rgb_colors = [] 
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    # rgb_colors.append(color.rgb) # color.rgb returns the RGB values as a tuple.
    # eg. Rgb(r=245, g=243, b=238)

    # but we want like this (245, 243, 238)
# color.rgb is an object that contains the RGB values of a color extracted by the colorgram library.
# color.rgb.r accesses the red component of the RGB tuple.
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    tup = (r, g, b)
    rgb_colors.append(tup)

print(rgb_colors) # will prints a list of RGB tuples

# part1 said for "above" to get "below" list of colors, now "above" no use!!
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed(0) # fastest it is!!
tim.penup() # really useful as now in yr code no pendown()/penup() would be needed!!
tim.hideturtle() # :)

# ISSUE -> the dots move out of the screen
# ⭐ FIX: start from bottom-left
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

# this was me and bit copilot for moving to next row
ycor = 10
while ycor > 1:
    xcor = 10 # reset for each row
    while xcor > 1:
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()
        xcor-=1

    # move to next row
    tim.penup()
    tim.backward(50 * 9) # as a backgayer in cars, facing front only
    tim.left(90) # on same row now
    tim.forward(50) # visualise it, move up(next row)
    tim.right(90) # turns left to cover this row
    tim.pendown() # starts the row as pendown
    ycor-=1
# 10*10 and 50 paces sepa b/w dots

# # more
# for y in range(-250, 250, 50):
#     for x in range(-250, 250, 50):
#         tim.goto(x,y)
#         tim.dot(20, random.choice(color_list))


# more
# for i in range(10):
#     tim.goto(-250, -200 + (i * 50))
#     for _ in range(10):
#         tim.dot(20, random.choice(color_list))
#         tim.forward(50)


t.Screen().exitonclick()
