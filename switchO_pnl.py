import bpy

class switchO_PT_Panel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_so"
    bl_label = "Switch Orientation"

    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"

    bl_context = "output"
    bl_parent_id = "RENDER_PT_format"

    # ------------------------------------

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(icon='FILE_REFRESH')
        row.operator("object.switch_o")        