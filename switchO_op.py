import bpy

class switchO_OP_Switch_Op(bpy.types.Operator):
    
    bl_idname = "object.switch_o"
    bl_label = "Switch"
    bl_description = "Switch between Portrait and Landscape Orientation"

    # -------------------------------------------------------------------
    
    def execute(self, context):
        r = bpy.context.scene.render
        r.resolution_x, r.resolution_y = r.resolution_y, r.resolution_x
        
        return {'FINISHED'}