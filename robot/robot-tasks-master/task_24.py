#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
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
    
    move_down()
    move_right()
    cross()

if __name__ == '__main__':
    run_tasks()
