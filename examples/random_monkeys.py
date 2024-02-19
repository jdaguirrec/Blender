import bpy
import random
import math

from bpybb.utils import clean_scene

clean_scene()

max_rotation = math.radians(360)

for i in range(33):
    random_size = random.uniform(0.1, 2.0)
    random_location = (
        random.uniform(-5, 5),
        random.uniform(-5, 5),
        random.uniform(-5, 5),
    )
    random_rotation = (
        random.uniform(-max_rotation, max_rotation),
        random.uniform(-max_rotation, max_rotation),
        random.uniform(-max_rotation, max_rotation),
    )

    bpy.ops.mesh.primitive_monkey_add(
        size=random_size, location=random_location, rotation=random_rotation
    )

    material = bpy.data.materials.new(name=f"monkey_material_{i}")
    material.use_nodes = True
    bsdf_node = material.node_tree.nodes["Principled BSDF"]
    red = random.random()
    green = random.random()
    blue = random.random()
    bsdf_node.inputs["Base Color"].default_value = (red, green, blue, 1)

    active_object = bpy.context.active_object
    active_object.data.materials.append(material)