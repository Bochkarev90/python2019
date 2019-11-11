import turtle

turtle.shape('turtle')
def draw_square(n):
    """ n - side length
    """
    for _ in range(4):
        turtle.forward(n)
        turtle.left(90)

def draw_squares(n, distance):
    """ n - number of squares
        distance - distance between squares
    """
    for i in range(n):
        turtle.penup()
        turtle.backward(distance)
        turtle.right(90)
        turtle.forward(distance)
        turtle.left(90)
        turtle.pendown()
        draw_square(i * distance * 2)

draw_squares(10, 10)
