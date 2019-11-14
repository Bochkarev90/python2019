import turtle
import math


turtle.shape('turtle')


def draw_rectangle(n, radius):
    """ Draws a rectangle
        n - number of sides
        radius - circle's radius
    """
    side_length = math.radians(360/(2*n)) * 2 * radius
    angle = 360 / n
    turtle.penup()
    turtle.goto(side_length, 0)
    turtle.pendown()

    turtle.left((180 - angle) / 2)
    for _ in range(n):
        turtle.left(360 / n)
        turtle.forward(side_length)
    turtle.right((180 - angle) / 2)

def draw_rectangles(n, radius):
    """ Draws several rectangles
        n - number of rectangles
        radius - radius of the first circle
    """
    r = radius
    for i in range(3, n+1):
        draw_rectangle(i, radius)
        radius += r

draw_rectangles(10, 20)
