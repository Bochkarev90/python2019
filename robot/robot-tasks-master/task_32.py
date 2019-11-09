#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.03)
def task_8_18():
    x = 0
    def column():
        """ Goes throught column, fills cells and returns filled count
        """
        x = 0
        while True:
            move_up()
            if cell_is_filled():
                x += 1
            else:
                fill_cell()
            if wall_is_above():
                break
        while not wall_is_beneath():
            move_down()
        return x

    while True:
        if not wall_is_beneath():
            mov('ax', x)
            break
        if wall_is_above():
            fill_cell()
        else:
            x += column()
        move_right()



if __name__ == '__main__':
    run_tasks()
