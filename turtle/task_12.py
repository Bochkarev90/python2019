import turtle
import math


turtle.shape('turtle')


def draw_arc(radius, steps):
    """ Draws an arc with recieved radius
        Moves *steps* times
    """
    arc_length = radius * math.pi
    step_length = arc_length / steps
    step_rotation = 180 / steps
    for _ in range(steps):
        turtle.forward(step_length)
        turtle.right(step_rotation)


turtle.penup()
turtle.goto(-500, 0)
turtle.pendown()
turtle.left(90)
for _ in range(15):
    draw_arc(50, 30)
    draw_arc(10, 10)
