import bpy
import numpy as np
from bpybb.utils import clean_scene

clean_scene()


bpy.ops.mesh.primitive_xyz_function_surface(x_eq='u*sin(v)',
                                            y_eq='u*cos(v)', 
                                            z_eq='v',
                                            range_u_min=0, range_u_max=2*np.pi, range_u_step=10, wrap_u=False,
                                            range_v_min=0, range_v_max=4*np.pi, range_v_step=50, wrap_v=False)

bpy.ops.object.editmode_toggle()