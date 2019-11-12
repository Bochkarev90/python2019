import turtle


turtle.shape('turtle')


def draw_rectangle(n):
    """ Draws a rectangle
        n - number of sides
    """
    for _ in range(n):
        turtle.left(360 / n)
        turtle.forward(20 * n)
    turtle.forward(10)

for i in range(3, 13):
    draw_rectangle(i)
