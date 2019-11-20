from graph import *
import random

windowSize(500, 600)
print(windowSize())
width, height = windowSize()


def cloud(x, y, radius):
    penColor('black')
    brushColor('white')
    circle(x, y, radius)


def sun(x, y, radius):
    penColor('yellow')
    brushColor('yellow')
    circle(x, y, radius)


def sky(y):
    """
    Draws the sky
    :param y: where the sky ends
    """
    penColor(0, 247, 255)
    brushColor(0, 247, 255)
    rectangle(0, 0, width, y)


def sea(y1, y2, color='blue'):
    """
    Draws the sea
    :param y1: where the sea starts
    :param y2: where the sea ends
    :param color: color of the sea
    """
    penColor(color)
    brushColor(color)
    rectangle(0, y1, width, y2)


def ground(y, color='yellow'):
    """
    Draws the ground
    :param y: where the ground starts
    :param color: color of the ground
    """
    penColor(color)
    brushColor(color)
    rectangle(0, y, width, height)


def umbrella(x, y):
    """
    Draws an umbrella
    :param x: distance from left edge
    :param y: distance from ground
    :return:
    """
    penColor(250, 128, 114)
    brushColor(250, 128, 114)
    rectangle(x-5, height-y, x+5, height/2+50)
    brushColor(255, 140, 120)
    polygon([
        (x, height/2+40), (x-75, height/2+100), (x+75, height/2+100)
    ])


sky(height/2)
sea(height/2, height/4*3)
ground(height/4*3)
sun(width-100, 100, 50)
for _ in range(10):
    cloud(random.randint(100, 300), random.randint(100, 150), 10)
umbrella(100, 30)

run()
