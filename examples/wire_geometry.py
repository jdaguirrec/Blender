import bpy
import addon_utils

from bpybb.addon import enable_addon
from bpybb.utils import clean_scene

clean_scene()

enable_addon(addon_module_name='add_mesh_extra_objects')

for i in range(9,10):
    bpy.ops.mesh.primitive_solid_add(source='12', size=i*0.1)
    bpy.ops.object.modifier_add(type='WIREFRAME')