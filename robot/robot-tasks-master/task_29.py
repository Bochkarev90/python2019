#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    i = 0
    while True:
        if cell_is_filled():
            i += 1
        else:
            i = 0
        if i == 3:
            break
        if wall_is_on_the_right():
            break
        move_right()


if __name__ == '__main__':
    run_tasks()
