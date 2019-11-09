#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    def fill_the_string(first_unfilled_cell_position: int, 
            second_unfilled_cell_position: int
            ):
        """ Fills all cells in the string except cells from parameters.
            Then move to the first sell of next string if possible
        """
        i = 0
        while True:
            if i != first_unfilled_cell_position \
                    and i != second_unfilled_cell_position:
                fill_cell()
            if wall_is_on_the_right():
                break
            move_right()
            i += 1
        while not wall_is_on_the_left():
            move_left()
        if not wall_is_beneath():
            move_down()
            
    
    number_of_cells = 1
    while not wall_is_on_the_right():
        move_right()
        number_of_cells += 1
    while not wall_is_on_the_left():
        move_left()
    
    for i in range(number_of_cells):
        fill_the_string(i, number_of_cells-1-i)




if __name__ == '__main__':
    run_tasks()
