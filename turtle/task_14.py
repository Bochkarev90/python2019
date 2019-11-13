import turtle


turtle.shape('turtle')


def draw_star(n, size):
    """ Draws a star with n vertices.
        size - length of the star's side
    """
    angle = 180 - 180 / n
    for _ in range(n):
        turtle.forward(size)
        turtle.left(angle)

draw_star(15, 150)

