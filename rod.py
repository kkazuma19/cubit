#!python
import numpy as np
import cubit

# define the parametric values
# fuel pellet
f_radius = 4.1
f_height = 2 * 5.93
n_pellets = 3

# dish
dish_sph_radius = 10.1542
dish_depth = 0.3

# chamfer
chamf_radius = 0.25

# gap
gap = 0.08

# cladding
c_thick = 0.56
c_plenum = 0.5
c_height = f_height * n_pellets + 2 * c_thick + c_plenum
c_in_radius = f_radius + gap
c_out_radius = c_in_radius + c_thick

### create fuel pellets
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

command = "Volume 1 copy move x 0 y 0 z " + str(f_height) + " repeat " + str(n_pellets -1) + " nomesh"
cubit.cmd(command)

command = "move volume all x 0 y 0 z " + str(f_height/2) 
cubit.cmd(command)

### create the cladding
# outer cylinder
vol_id = 3 + n_pellets
command = "create cylinder height " + str(c_height) + " radius " + str(c_out_radius)
cubit.cmd(command)
# inner cylinder
command = "create cylinder height " + str(c_height - 2*c_thick) + " radius " + str(c_in_radius)
cubit.cmd(command)
# subtract 
command = "subtract volume " + str(vol_id + 1) + " from volume " + str(vol_id)
cubit.cmd(command)

# do not change!
clad_id = vol_id + 2

command = "move volume " + str(clad_id) + "x 0 y 0 z " + str((c_height - 2*c_thick)/2)
cubit.cmd(command)


'''
Imprint & Merge
'''
command = "imprint volume all"
cubit.cmd(command)

command = "merge volume all"
cubit.cmd(command)

#command = "undo group end"
#cubit.cmd(command)
