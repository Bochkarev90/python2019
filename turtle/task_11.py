import turtle


turtle.shape('turtle')


def draw_left_circle(step):
    for _ in range(90):
        turtle.left(4)
        turtle.forward(step)


def draw_right_circle(step):
    for _ in range(90):
        turtle.right(4)
        turtle.forward(step)

def draw_butterfly(n):
    """ Draws a butterfly
        n - number of wings
    """
    turtle.right(90)
    step = 1
    for _ in range(n):
        draw_left_circle(step)
        draw_right_circle(step)
        step += 1

draw_butterfly(30)

