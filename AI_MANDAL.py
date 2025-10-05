import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("AI Mandala")

# Turtle setup
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)  # Use RGB colors

# Function to generate rainbow colors
def rainbow_colors(n):
    colors = []
    for i in range(n):
        color = colorsys.hsv_to_rgb(i/n, 1, 1)  # HSV to RGB
        colors.append((int(color[0]*255), int(color[1]*255), int(color[2]*255)))
    return colors

# Parameters
num_colors = 36
num_shapes = 36
colors = rainbow_colors(num_colors)

# Draw mandala
for i in range(num_shapes):
    t.color(colors[i % num_colors])
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.circle(100)
    t.right(360 / num_shapes)  # Rotate for symmetry

# Hide turtle
t.hideturtle()

# Finish
turtle.done()
