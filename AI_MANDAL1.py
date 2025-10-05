import turtle
import random
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Advanced AI Mandala")

# Turtle setup
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
t.hideturtle()

# Function to generate gradient rainbow colors
def rainbow_colors(n, s=1, v=1):
    colors = []
    for i in range(n):
        color = colorsys.hsv_to_rgb(i/n, s, v)
        colors.append((int(color[0]*255), int(color[1]*255), int(color[2]*255)))
    return colors

# Function to draw a petal
def draw_petal(t, radius, angle):
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

# Draw mandala
def draw_mandala(layers, petals_per_layer):
    for layer in range(layers):
        radius = 20 + layer * 15
        petal_angle = 60
        num_colors = petals_per_layer
        colors = rainbow_colors(num_colors, s=random.uniform(0.5,1), v=random.uniform(0.5,1))
        for i in range(petals_per_layer):
            t.color(colors[i])
            t.penup()
            t.goto(0,0)
            t.pendown()
            t.setheading(i * (360 / petals_per_layer))
            draw_petal(t, radius, petal_angle)

# Customize your mandala
draw_mandala(layers=8, petals_per_layer=24)

turtle.done()
