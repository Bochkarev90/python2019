import turtle
import math


turtle.shape('turtle')


def draw_circle(x, y, r, steps, counterclockwise=False, arc=False, color=''):
    """ Draws a circle
        x, y - coords of the center of the circle
        r - radius of the circle
    """
    turtle.penup()
    turtle.goto(x - r, y) if counterclockwise else turtle.goto(x + r, y)
    turtle.pendown()
    
    circle_length = 2 * r * math.pi
    step_rotation = 360 / steps
    step_length = circle_length / steps
    if arc:
        circle_length /= 2
        step_rotation /= 2
        step_length /= 2       
    if color:
        turtle.color(color)
        turtle.begin_fill()
    if counterclockwise:
        for _ in range(steps):
            turtle.left(step_rotation)
            turtle.forward(step_length)
    else:
        for _ in range(steps):
            turtle.right(step_rotation)
            turtle.forward(step_length)
    if color:
        turtle.end_fill()

turtle.left(90)
draw_circle(0, 0, 100, 100, counterclockwise=True, color='yellow')







