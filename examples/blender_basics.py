import bpy
import random
import math

from bpybb.utils import clean_scene

clean_scene()


bpy.ops.mesh.primitive_cube_add()

object = bpy.context.active_object


object.location[0] = 4      # X
object.location[1] = 2      # Y
object.location[2] = 5      # Z

radians = lambda x: math.radians(x)

object.rotation_euler[0] = radians(45)
object.rotation_euler[1] = radians(0)
object.rotation_euler[2] = radians(0)

# Crear modifier
modifier_subsurf = object.modifiers.new('My First Modifier', 'SUBSURF')
# Subdivisiones
modifier_subsurf.levels = 3

#mesh = object.data
#for face in mesh.polygons:
#    face.use_smooth = True

# La siguiente línea hace lo mismo que el bloque anterior que está comentado
bpy.ops.object.shade_smooth()

# https://docs.blender.org/api/current/bpy.types.Modifier.html
# Crear displacement modifier
modifier_displacement = object.modifiers.new('My Displacement', 'DISPLACE')

# https://docs.blender.org/api/current/bpy.types.Texture.html
# Crear textura
new_texture = bpy.data.textures.new('My Texture', 'DISTORTED_NOISE')

# Cambiando la configuración de la textura
new_texture.noise_scale = 2.0

# Asignar la textura al displacement modifier
modifier_displacement.texture = new_texture

# Crear material
new_material = bpy.data.materials.new(name='My Material')
object.data.materials.append(new_material)

new_material.use_nodes = True
nodes = new_material.node_tree.nodes

material_output = nodes.get('Material Output')
node_emission = nodes.new(type='ShaderNodeEmission')

node_emission.inputs[0].default_value = (0.0, 0.3, 1.0, 1)
node_emission.inputs[1].default_value = 500.0 # strength

links = new_material.node_tree.links
new_link = links.new(node_emission.outputs[0], material_output.inputs[0])