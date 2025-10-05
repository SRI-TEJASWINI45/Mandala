import turtle
import random
import math

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("New Dasara-Inspired Mandala")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.colormode(255)

# Festive colors
colors = [
    (255, 69, 0),   # OrangeRed
    (255, 215, 0),  # Gold
    (50, 205, 50),  # LimeGreen
    (30, 144, 255), # DodgerBlue
    (255, 20, 147), # DeepPink
    (255, 140, 0),  # DarkOrange
]

# Draw a teardrop/paisley shape
def draw_teardrop(t, size):
    t.begin_fill()
    t.circle(size, 180)
    t.left(90)
    t.forward(size * 1.5)
    t.left(90)
    t.circle(size, 180)
    t.left(90)
    t.forward(size * 1.5)
    t.end_fill()

# Draw a lotus layer
def draw_lotus_layer(t, radius, petals):
    angle = 360 / petals
    for i in range(petals):
        t.color(random.choice(colors))
        t.penup()
        t.goto(0,0)
        t.setheading(i * angle)
        t.forward(radius)
        t.pendown()
        draw_teardrop(t, 15)

# Draw triangular spikes
def draw_triangle_layer(t, radius, spikes):
    angle = 360 / spikes
    for i in range(spikes):
        t.color(random.choice(colors))
        t.penup()
        t.goto(0,0)
        t.setheading(i * angle)
        t.forward(radius)
        t.pendown()
        t.begin_fill()
        for _ in range(3):
            t.forward(20)
            t.left(120)
        t.end_fill()

# Draw spiral circles
def draw_spiral_layer(t, radius, count):
    for i in range(count):
        t.color(random.choice(colors))
        t.penup()
        t.goto(0,0)
        t.setheading(i * (360/count))
        t.forward(radius)
        t.pendown()
        t.circle(10 + i%5)

# Generate Dasara Mandala
for layer in range(1,6):
    radius = 20 + layer*25
    petals = 6 + layer*2
    draw_lotus_layer(t, radius, petals)
    draw_triangle_layer(t, radius + 15, petals*2)
    draw_spiral_layer(t, radius + 30, petals*3)

turtle.done()
