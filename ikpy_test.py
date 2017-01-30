#!/usr/bin/python

import ikpy
import numpy as np
import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D
from ikpy import plot_utils, geometry_utils

my_chain = ikpy.chain.Chain.from_urdf_file("./poppy_ergo.URDF")

target_vector = [ 0.1, -0.5, 0.1]
target_frame = np.eye(4)
target_frame[:3, 3] = target_vector

print("The angles of each joints are : ", my_chain.inverse_kinematics(target_frame))

real_frame = my_chain.forward_kinematics(my_chain.inverse_kinematics(target_frame))
print("Computed position vector : {0}\nOriginal position vector : {1}\n".format(real_frame[:3, 3], target_frame[:3, 3]))

print("target_frame: {0}".format(target_frame))
print("real_frame: {0}".format(real_frame))

ax = matplotlib.pyplot.figure().add_subplot(111, projection='3d')

my_chain_plot = my_chain.plot(my_chain.inverse_kinematics(target_frame), ax)

matplotlib.pyplot.show()
