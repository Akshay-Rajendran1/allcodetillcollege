import turtle

screen = turtle.getscreen()

screen.bgcolor("white")

screen.title("USA Flag - https://www.pythoncircle.com")

master_oogway = turtle.Turtle()

master_oogway.speed(4000)
master_oogway.penup()

master_oogway.shape("turtle")

flag_height = 250
flag_width = 475

start_x = -237
start_y = 125

stripe_height = flag_height / 13
stripe_width = flag_width

star_size = 10

x = start_x
y = start_y

def draw_fill_rectangle(x, y, height, width, color):
    master_oogway.goto(x, y)
    master_oogway.pendown()
    master_oogway.color(color)
    master_oogway.begin_fill()
    master_oogway.forward(width)
    master_oogway.right(90)
    master_oogway.forward(height)
    master_oogway.right(90)
    master_oogway.forward(width)
    master_oogway.right(90)
    master_oogway.forward(height)
    master_oogway.right(90)
    master_oogway.end_fill()
    master_oogway.penup()

def draw_star(x, y, color, length):
    master_oogway.goto(x, y)
    master_oogway.setheading(0)
    master_oogway.pendown()
    master_oogway.begin_fill()
    master_oogway.color(color)
    for turn in range(0, 5):
        master_oogway.forward(length)
        master_oogway.right(144)
        master_oogway.forward(length)
        master_oogway.right(144)
    master_oogway.end_fill()
    master_oogway.penup()

def draw_ring():
    RADIUS = 70
    STARTING_POINT_X = -200
    STARTING_POINT_Y = -300

    x = STARTING_POINT_X
    y = STARTING_POINT_Y

    color = "blue"
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(RADIUS)

    x = STARTING_POINT_X + 100
    y = STARTING_POINT_Y - 50

    color = "orange"
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(RADIUS)

    x = STARTING_POINT_X + 200
    y = STARTING_POINT_Y + 10

    color = "black"
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(RADIUS)

    x = STARTING_POINT_X + 300
    y = STARTING_POINT_Y - 50

    color = "green"
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(RADIUS)

    x = STARTING_POINT_X + 400
    y = STARTING_POINT_Y + 10

    color = "red"
    turtle.hideturtle()
    turtle.pensize(10)
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(RADIUS)

def draw_name():
    STRT_X = 10
    STRT_Y = 280
    x = STRT_X
    y = STRT_Y
    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor('blue')
    turtle.write("USA", align="center", font=("Helvetica", 60, "bold"))
    STRT_X = 10
    STRT_Y = 200
    x = STRT_X
    y = STRT_Y
    turtle.penup()
    turtle.goto(x, y)
    turtle.pencolor('blue')
    turtle.write("OLYMPIC TEAM", align="center", font=("Helvetica", 60, "bold"))
