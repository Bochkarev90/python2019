import turtle


turtle.shape('turtle')


def spiral(p=0.01):
    """ Draws a spiral
        p - increment
    """
    increment = p
    while True:
        turtle.forward(p)
        turtle.left(3)
        p += increment

spiral(0.01)

