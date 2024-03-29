#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    while True:
        if wall_is_beneath() and not wall_is_above():
            fill_cell()
        if not wall_is_on_the_right():
            move_right()
        else:
            break


if __name__ == '__main__':
    run_tasks()
