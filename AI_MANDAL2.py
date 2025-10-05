import turtle
import random

# Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Dasara-Inspired Indian Mandala")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Rangoli-style festive colors
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "white"]

# Function to draw a petal
def draw_petal(t, radius, angle):
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

# Function to draw a layer of petals
def draw_flower_layer(radius, petals):
    angle = 360 / petals
    for i in range(petals):
        t.color(random.choice(colors))
        draw_petal(t, radius, 60)
        t.left(angle)

# Function to draw geometric diamonds
def draw_diamond(t, size):
    t.begin_fill()
    for _ in range(2):
        t.forward(size)
        t.left(45)
        t.forward(size)
        t.left(135)
    t.end_fill()

# Draw concentric layers
for layer in range(1, 6):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    radius = 20 + layer * 20
    petals = 6 + layer * 2
    draw_flower_layer(radius, petals)
    
    # Add diamonds between petals
    for i in range(petals):
        t.penup()
        t.goto(0,0)
        t.setheading(i * (360 / petals))
        t.forward(radius + 10)
        t.pendown()
        t.color(random.choice(colors))
        draw_diamond(t, 15)

# Finish
turtle.done()
