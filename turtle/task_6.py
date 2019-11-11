import turtle

def spider(n):
    turtle.shape("turtle")
    """ Draws a spider with n ends
    """
    for _ in range(n):
        turtle.forward(100)
        turtle.stamp()
        turtle.right(180)
        turtle.forward(100)
        turtle.right(180 + 360 / n)

spider(12)
