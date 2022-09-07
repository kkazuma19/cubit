#!python
import numpy as np
import cubit

# define the parametric values
# fuel pellet
f_radius = 4.1
f_height = 11.9
n_pellets = 9
#
gap = 0.08
# cladding
c_thick = 0.56
c_plenum = 0.5
c_height = f_height * n_pellets + 2 * c_thick + c_plenum
c_in_radius = f_radius + gap
c_out_radius = c_in_radius + c_thick

# create the cladding
# outer cylinder
command = "create cylinder height " + str(c_height) + " radius " + str(c_out_radius)
cubit.cmd(command)
# inner cylinder
command = "create cylinder height " + str(c_height - 2*c_thick) + " radius " + str(c_in_radius)
cubit.cmd(command)
# subtract 
command = "subtract volume 2 from volume 1"
cubit.cmd(command)


command = "volume 3 scheme tetmesh"
cubit.cmd(command)
command = "mesh volume 3"
cubit.cmd(command)
