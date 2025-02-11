"""
File: breakout.py
-----------------
This program implements the game Breakout!  The user controls a paddle
moving horizontally with the mouse, and the user must bounce the ball
to make it collide and remove bricks from the screen.  The user has
3 turns.  If the ball falls below the bottom of the screen, the user
loses a turn.  If the user removes all bricks before their turns
run out, they win!
"""

import math
from graphics import Canvas
import random
import time

"""
Dimensions of the canvas, in pixels
These should be used when setting up the initial size of the game,
but in later calculations you should use canvas.get_canvas_width() and 
canvas.get_canvas_height() rather than these constants for accurate size information.
"""
CANVAS_WIDTH = 420
CANVAS_HEIGHT = 600

# Stage 1: Set up the Bricks

# Number of bricks in each row
NBRICK_COLUMNS = 10

# Number of rows of bricks
NBRICK_ROWS = 10

# Separation between neighboring bricks, in pixels
BRICK_SEP = 4

# Width of each brick, in pixels
BRICK_WIDTH = math.floor((CANVAS_WIDTH - (NBRICK_COLUMNS + 1.0) * BRICK_SEP) / NBRICK_COLUMNS)

# Height of each brick, in pixels
BRICK_HEIGHT = 8

# Offset of the top brick row from the top, in pixels
BRICK_Y_OFFSET = 70

# Stage 2: Create the Bouncing Ball

# Radius of the ball in pixels
BALL_RADIUS = 10

# The ball's vertical velocity.
VELOCITY_Y = 6.0

# The ball's minimum and maximum horizontal velocity; the bounds of the
# initial random velocity that you should choose (randomly +/-).
VELOCITY_X_MIN = 2.0
VELOCITY_X_MAX = 6.0

# Animation delay or pause time between ball moves (in seconds)
DELAY = 1 / 60

# Stage 3: Create the Paddle

# Dimensions of the paddle
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 10

# Offset of the paddle up from the bottom
PADDLE_Y_OFFSET = 30

# Stage 5: Polish and Finishing Up

# Number of turns
NTURNS = 3

BOUNCE_SOUND = "bounce.au"

DELAY = 0.02

BALL_SPEED = random.randint(1, 7)



def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    canvas.set_canvas_title("Breakout")
    color = "red"
    bricks = []
    x1 = 0
    y1 = BRICK_Y_OFFSET
    for i in range(10):
        y1 += BRICK_HEIGHT + BRICK_SEP
        for j in range(0, 10):
            if i == 0:
                color == "red"
            if i == 2:
                color = "gold"
            if i == 4:
                color = "yellow"
            if i == 6:
                color = "lime"
            if i == 8:
                color = "cyan"
            draw_bricks(canvas, bricks, color, x1, y1)
            x1 += BRICK_SEP + BRICK_WIDTH

        x1 = 0

    ball = make_ball(canvas)
    dx = BALL_SPEED
    dy = BALL_SPEED

    lives = 3

    paddle = make_paddle(canvas)
    y1 = canvas.get_canvas_height() - 30

    while lives != 0:
        mouse_x = canvas.get_mouse_x()
        canvas.moveto(paddle, mouse_x, y1)

        canvas.move(ball, dx, dy)

        curr_x = canvas.get_left_x(ball)
        curr_y = canvas.get_top_y(ball)
        width = canvas.get_canvas_width()/2
        height = canvas.get_canvas_height()/2
        if curr_x < 0:
            dx = BALL_SPEED
        if curr_x + BALL_RADIUS * 2 > canvas.get_canvas_width():
            dx = -BALL_SPEED
        if curr_y < 0:
            dy = BALL_SPEED
        if curr_y + BALL_RADIUS * 2 > canvas.get_canvas_height():
            canvas.moveto(ball, width, height)
            lives -= 1

        ball_coords = canvas.coords(ball)
        x_1 = ball_coords[0]
        y_1 = ball_coords[1]
        x_2 = ball_coords[2]
        y_2 = ball_coords[3]
        colliding_list = canvas.find_overlapping(x_1, y_1, x_2, y_2)
        for object in colliding_list:
            if object == paddle:
                #if
                dy = -dy
            for brick in bricks:
                if brick == object:
                    dy = -dy
                    dx = -dx
                    canvas.delete(brick)
        canvas.update()
        time.sleep(DELAY)

    canvas.mainloop()

def make_ball(canvas):
    width = canvas.get_canvas_width()
    height = canvas.get_canvas_height()

    top_left_x = width/2
    top_left_y = height/2


    bottom_right_x = top_left_x + BALL_RADIUS * 2
    bottom_right_y = top_left_y + BALL_RADIUS * 2

    ball = canvas.create_oval(top_left_x, top_left_y, bottom_right_x, bottom_right_y)

    canvas.set_fill_color(ball, "black")
    canvas.set_outline_color(ball, "black")
    return ball


def draw_bricks(canvas, bricks, color, x1, y1):
    x2 = x1 + BRICK_WIDTH
    y2 = y1 + BRICK_HEIGHT
    rect = canvas.create_rectangle(x1, y1, x2, y2)
    bricks.append(rect)
    canvas.set_fill_color(rect, color)
    canvas.set_outline_color(rect, "white")
    canvas.set_outline_width(rect, BRICK_SEP)
    return bricks

def make_paddle(canvas):
    x1 = canvas.get_canvas_width()/2
    y1 = canvas.get_canvas_height() - 30
    y2 = y1 + PADDLE_HEIGHT
    x2 = x1 + PADDLE_WIDTH
    rect = canvas.create_rectangle(x1, y1, x2, y2)
    canvas.set_fill_color(rect, "black")
    canvas.set_outline_color(rect, "black")
    canvas.update()
    return rect


if __name__ == '__main__':
    main()