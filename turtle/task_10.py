import turtle


turtle.shape('turtle')


def draw_left_circle():
    for _ in range(90):
        turtle.left(4)
        turtle.forward(10)


def draw_right_circle():
    for _ in range(90):
        turtle.right(4)
        turtle.forward(10)

def draw_flower(n):
    """ Draws a flower 
        n - number of flower petals
    """
    angle = 360 / n
    for _ in range(n // 2):
        draw_left_circle()
        draw_right_circle()
        turtle.left(angle)

draw_flower(10)


