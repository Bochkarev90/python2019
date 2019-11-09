#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    def cross():
        """ Draws a cross
            Starts and ends in the left top point
        """
        move_right()
        fill_cell()
        move_down()
        fill_cell()
        move_left()
        fill_cell()
        move_right(2)
        fill_cell()
        move_down()
        move_left()
        fill_cell()
        move_left()
        move_up(2)

    for _ in range(5):
        for _ in range(9):
            cross()
            move_right(4)
        cross()
        while not wall_is_on_the_left():
            move_left()
        move_down(2)
        if wall_is_beneath():
            move_up(2)
        else:
            move_down(2)

if __name__ == '__main__':
    run_tasks()
