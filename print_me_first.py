# Program Name: main.py
# Program Description:
#   This is the Seventh lab
#
#   In this program I make a program to draw a flag about the USA olympic team
# @Author: Akshay Rajendran
# @Date: 7/23/22

from datetime import datetime
import turtle

def print_info():
    s_x = 400
    s_y = -300
    x = s_x
    y = s_y
    turtle.pensize(5)
    turtle.pencolor('blue')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    name = "name:    :Akshay"
    turtle.write(name, align="right", font=("Helvetica", 10))

    y = y - (25)

    turtle.pensize(5)
    turtle.pencolor('blue')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    lab = "Program    :olympics_rings.py"
    turtle.write(lab, align="right", font=("Helvetica", 10))

    y = y - (25)

    currentTime = datetime.now()
    timestampStr = currentTime.strftime("%b-%d-%Y %a %I:%M:%S")

    turtle.pensize(5)
    turtle.pencolor('blue')
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(timestampStr, align="right", font=("Helvetica", 10))