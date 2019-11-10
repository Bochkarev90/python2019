import turtle

def print_circle(n):
    """ n - degree of rotation
    """
    for _ in range(n):
        turtle.forward(5)
        turtle.left(360 / n)

print_circle(100)
