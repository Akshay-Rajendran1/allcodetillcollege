import turtle
import Draw_USA_Flag
import print_me_first

screen = turtle.getscreen()

screen.bgcolor("white")

screen.bgpic("usa.png")
screen.title("USA Flag - https://www.pythoncircle.com")

oogway = turtle.Turtle()

oogway.speed(4000)
oogway.penup()

oogway.shape("turtle")
oogway.hideturtle()

flag_height = 250
flag_width = 475


start_x = -237
start_y = 125

stripe_height = flag_height / 13
stripe_width = flag_width

star_size = 10

x = start_x
y = start_y

for stripe in range(0, 6):
    for color in ["red", "white"]:
        Draw_USA_Flag.draw_fill_rectangle(x, y, stripe_height, stripe_width, color)
        y = y - stripe_height

Draw_USA_Flag.draw_fill_rectangle(x, y, stripe_height, stripe_width, 'red')
y = y - stripe_height

square_height = (7 / 13) * flag_height
square_width = (0.76) * flag_height
Draw_USA_Flag.draw_fill_rectangle(start_x, start_y, square_height, square_width, 'navy')

gap_between_stars = 30
gap_between_lines = stripe_height + 6
y = 112

for row in range(0, 5):
    x = -222
    for star in range(0, 6):
        Draw_USA_Flag.draw_star(x, y, 'white', star_size)
        x = x + gap_between_stars
    y = y - gap_between_lines

gap_between_stars = 30
gap_between_lines = stripe_height + 6
y = 100

for row in range(0, 4):
    x = -206
    for star in range(0, 5):
        Draw_USA_Flag.draw_star(x, y, 'white', star_size)
        x = x + gap_between_stars
    y = y - gap_between_lines

x = -350
Draw_USA_Flag.draw_star(x, y, 'white', star_size)
y = y - gap_between_lines

Draw_USA_Flag.draw_ring()
Draw_USA_Flag.draw_name()

print_me_first.print_info()

screen.mainloop()
