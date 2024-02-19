import bpy
import addon_utils

from bpybb.addon import enable_addon
from bpybb.utils import clean_scene

clean_scene()

enable_addon(addon_module_name='add_curve_extra_objects')

bpy.ops.curve.spirals(
    spiral_type='LOG',
    radius=1.42,
    turns=256,
    steps=128,
    dif_z=0.1,
    B_force=0.99,
    edit_mode=False,
)

bpy.context.object.data.bevel_depth = 0.01