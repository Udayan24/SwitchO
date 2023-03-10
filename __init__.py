'''
-----------------------------------------------------------------------
Created by Udayan Chavan 
(https://blender.community/udayanchavan/)
(https://blenderartists.org/u/udayan/)
-----------------------------------------------------------------------
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
-----------------------------------------------------------------------
'''

bl_info = {
    "name" : "SwitchO",
    "author" : "Udayan",
    "description" : "Switch between Portrait and Landscape Modes easily.",
    "blender" : (3, 0, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Render"
}

# -------------------------------------------------
import bpy
from . switchO_op import switchO_OP_Switch_Op
from . switchO_pnl import switchO_PT_Panel

classes = (switchO_OP_Switch_Op, switchO_PT_Panel)
# -------------------------------------------------

def register():
    for c in classes:
        bpy.utils.register_class(c)

def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
