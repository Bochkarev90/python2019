import turtle
import math
import time


turtle.shape('turtle')


def draw_circle(x, y, r, steps, counterclockwise=False, arc=False, color='black', color_filling=''):
    """ Draws a circle
        x, y - coords of the center of the circle
        r - radius of the circle
    """
    turtle.penup()
    turtle.goto(x, y - r) if counterclockwise else turtle.goto(x, y + r)
    turtle.pendown()
    
    circle_length = 2 * r * math.pi
    step_rotation = 360 / steps
    step_length = circle_length / steps
    if arc:
        circle_length /= 2
        step_rotation /= 2
        step_length /= 2       
    
    turtle.color(color)
    if color_filling:
        turtle.color(color_filling)
        turtle.begin_fill()
    if counterclockwise:
        for _ in range(steps):
            turtle.left(step_rotation)
            turtle.forward(step_length)
    else:
        for _ in range(steps):
            turtle.right(step_rotation)
            turtle.forward(step_length)
    if color_filling:
        turtle.end_fill()


# HEAD
draw_circle(0, 0, 100, 100, color_filling='yellow')

# EYES
draw_circle(-40,40, 10, 10, color_filling='blue')
draw_circle(40, 40, 10, 10, color_filling='blue')

# NOSE
turtle.penup()
turtle.goto(0, 15)
turtle.pendown()
turtle.color('black')
turtle.width(10)
turtle.goto(0, -15)

# MOUTH
turtle.right(90)
draw_circle(60, -80, 60, 60, arc=True, color='red')


time.sleep(5)




