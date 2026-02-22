from robot import *

while(is_wall_up() and is_wall_down() and is_free_right()):
        move_right()
        
while(is_wall_up() and is_wall_down() and is_free_left()):
    move_left()