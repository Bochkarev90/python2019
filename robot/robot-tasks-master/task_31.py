#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.11)
def task_8_30():
    while True:
        while not wall_is_on_the_right():
            move_right()
        while wall_is_beneath():
            if wall_is_on_the_left():
                return
            move_left()
        while not wall_is_beneath():
            move_down()



if __name__ == '__main__':
    run_tasks()
