import bpy
import numpy as np
from bpybb.utils import clean_scene

clean_scene()

# How I make science animations https://youtu.be/yaa13eehgzo?t=1626
bpy.ops.mesh.primitive_z_function_surface(equation='(e**((-((x - 0.25)**2))/(0.15**2)) + \
                                                    0.7*e**((-((x - 0.6)**2))/(0.12**2))) * \
                                                    (0.6*e**((-((y - 0.5)**2))/(0.3**2)) + \
                                                    e**((-((y - 0.15)**2))/(0.1**2)) + \
                                                    0.7*e**((-((y - 0.8)**2))/(0.1**2)))', 
                                                    div_x=500, div_y=500, size_x=2, size_y=2)