#!python
import numpy as np
import cubit

# define the parametric values
## fuel pellet
f_radius = 4.1
f_height = 2 * 5.93

## dish
dish_sph_radius = 10.1542
dish_depth = 0.3

## chamfer
chamf_radius = 0.25

command = "create cylinder height " + str(f_height) + " radius " + str(f_radius)
cubit.cmd(command)
command = "modify curve 1 2 chamfer radius " + str(chamf_radius)
cubit.cmd(command)

# vol id 2
command = "create sphere radius " + str(dish_sph_radius) 
cubit.cmd(command)

command = "move Volume 2 x 0 y 0 z " + str( f_height/2 + (dish_sph_radius - dish_depth) ) + " include_merged"
cubit.cmd(command)

# vol id 3
command = "Volume 2 copy reflect z nomesh"
cubit.cmd(command)

command = "subtract volume 2 3 from volume 1"
cubit.cmd(command)
