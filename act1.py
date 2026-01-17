import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create turtle
t = turtle.Turtle()
t.speed(3)
t.width(2)

# Function to draw a polygon
def draw_polygon(sides, length, color):
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(sides):
        t.forward(length)
        t.left(360 / sides)
    t.end_fill()

# Draw equilateral triangle
t.penup()
t.goto(-200, 0)
t.pendown()
draw_polygon(3, 100, "red")

# Draw rectangle
t.penup()
t.goto(0, 0)
t.pendown()
t.fillcolor("green")
t.begin_fill()
for _ in range(2):
    t.forward(140)
    t.left(90)
    t.forward(80)
    t.left(90)
t.end_fill()

# Draw hexagon
t.penup()
t.goto(200, 0)
t.pendown()
draw_polygon(6, 70, "yellow")

# Finish
t.hideturtle()
screen.mainloop()
