#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    i = 1
    while True:
        fill_cell()
        for _ in range(i):
            if wall_is_on_the_right():
                break
            move_right()
        if wall_is_on_the_right():
            break
        i += 1



if __name__ == '__main__':
    run_tasks()
