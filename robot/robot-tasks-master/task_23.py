#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    while True:
        move_right()
        while not wall_is_above():
            move_up()
        while not wall_is_beneath():
            fill_cell()
            move_down()
        if wall_is_on_the_right():
            while wall_is_beneath():
                move_left()
            break



if __name__ == '__main__':
    run_tasks()
