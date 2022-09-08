#!python
import numpy as np
import cubit

# define the parametric values
# fuel pellet
f_radius = 4.1
f_height = 2 * 5.93


command = "create cylinder height " + str(f_height) + " radius " + str(f_radius)
cubit.cmd(command)

# vol id 2
command = "create sphere radius 10.1542" 
cubit.cmd(command)

command = "move Volume 2 x 0 y 0 z 15.6842 include_merged"
cubit.cmd(command)

command = "Volume 2 copy reflect z nomesh"
cubit.cmd(command)

command = "subtract volume 2 3 from volume 1"
cubit.cmd(command)

# inner cylinder
#command = "create cylinder height " + str(c_height - 2*c_thick) + " radius " + str(c_in_radius)
#cubit.cmd(command)
# subtract 
#command = "subtract volume 2 from volume 1"
#cubit.cmd(command)


