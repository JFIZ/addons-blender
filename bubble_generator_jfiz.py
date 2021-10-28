""" Bubbles Generator by J.FIZ """

import bpy
from random import randint
from bpy.types import (Panel, Operator)

"INFO"
bl_info = {
    "name": "Bubble generator",
    "author": "J.FIZ <fizjuanfrancisco@gmail.com>",
    "version": (1, 0),
    "blender": (2, 93, 2),
    "category": "Mesh",
    "location": "Operator Search",
    "description": "Bbble Generator",
    "warning": "", 
    "doc_url": "",
    "tracker_url": "",
}


""" OPERATOR """
class MESH_OT_bubbleg(bpy.types.Operator):
    """Bubble Generator"""
    bl_idname="mesh.objeto_bubbles"
    bl_label="Bubbles everywhere"
    bl_options={'REGISTER','UNDO'}
    
    range: bpy.props.IntProperty(
        name="Amount",
        description="More Bubbles",
        default=100,
        min= 1,
        soft_max= 100,
        )
    sky: bpy.props.IntProperty(
        name="To the SKY!!!",
        description="Up to the sky",
        default=0,
        min= 0,
        soft_max= 50,
    )
    size: bpy.props.IntProperty(
        name="Random sizes",
        description="Bubble sizes",
        default=3,
        min= 1,
        soft_max= 10,
    )

    def execute(self, context):
        for i in range(self.range):
            randomSize = randint(0,self.size)
            x = randint(-40,40)
            y = randint(-40,40)
            z = randint(0,self.sky)
            bpy.ops.mesh.primitive_uv_sphere_add(radius=randomSize, enter_editmode=False, align='WORLD', location=(x, y, z))
            bpy.ops.object.shade_smooth()
            
        return {'FINISHED'}


""" PANEL """
class LateralPanel(bpy.types.Panel):
    bl_label = "Bubble everywhere"
    bl_idname = "OBJECT_PT_BubbleEW"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Bubble Party"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        row = layout.row()
        row.operator(MESH_OT_bubbleg.bl_idname, text="¡Bubble Party!", icon='SHADING_RENDERED')
        
from bpy.utils import register_class, unregister_class

_classes = [
    MESH_OT_bubbleg,
    LateralPanel
]

""" REGISTER """

def register():
    for cls in _classes:
        register_class(cls)
   
def unregister():
    for cls in _classes:
        unregister_class(cls)
  


if __name__ == "__main__":
    register()


