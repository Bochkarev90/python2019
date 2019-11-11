import turtle


turtle.shape('turtle')


def square_spiral(i):
    """ Draws a square spiral
        i - size of first sides
    """
    step = i
    while True:
        for _ in range(2):
            turtle.forward(i)
            turtle.left(90)
        i += step

square_spiral(10)

