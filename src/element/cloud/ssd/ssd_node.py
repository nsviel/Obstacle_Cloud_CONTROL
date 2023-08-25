#---------------------------------------------
from src.gui.style import colorization
from src.element.base import node
from src.utils import parser_json
from src.gui.style import gui_color
import dearpygui.dearpygui as dpg


class Ssd_node(node.Node):
    def build(self):
        self.ID.init_ID_icon()
        with dpg.node(label=self.ID.name, tag=self.ID.ID_node):
            # Icone & status button
            with dpg.node_attribute(tag=self.ID.ID_node_input, attribute_type=dpg.mvNode_Attr_Input, shape=dpg.mvNode_PinShape_QuadFilled):
                with dpg.table(header_row=False, borders_innerH=False, policy=dpg.mvTable_SizingFixedFit):
                    dpg.add_table_column(label="Icone", width_fixed=True, init_width_or_weight=75)
                    dpg.add_table_column(label="Button", width_fixed=True, init_width_or_weight=15)
                    with dpg.table_row():
                        dpg.add_image(self.ID.ID_icon_hub, width=15, height=15)
                        dpg.add_button(tag=self.ID.ID_status_light, width=15)
                with dpg.drawlist(width=100, height=1):
                    dpg.draw_line([0, 0], [125, 0], color=gui_color.color_line)
        self.position_node()

    def position_node(self):
        data = parser_json.get_pos_from_json()
        dpg.set_item_pos(self.ID.ID_node, data["cloud"]["ssd"])

    def update_node(self):
        dpg.set_value(self.ID.ID_status, param_control.status_ssd)
        dpg.set_value(self.ID.ID_path, param_control.path_ssd)
        dpg.set_value(self.ID.ID_memory_total, param_control.state_control["ssd"]["space_total"])
        dpg.set_value(self.ID.ID_memory_used, param_control.state_control["ssd"]["space_used"])
        dpg.set_value(self.ID.ID_path_l1, param_control.state_control["path"]["dir_l1"])
        dpg.set_value(self.ID.ID_path_l2, param_control.state_control["path"]["dir_l2"])
        dpg.set_value(self.ID.ID_file_name, param_control.state_control["path"]["file_name"])

    def colorize_node(self):
        colorization.colorize_item(self.ID.ID_activated, "checkbox")
        colorization.colorize_item(self.ID.ID_path_add, "input_text")
        colorization.colorize_item(self.ID.ID_path, "input_text")

    def init_ID_icon(self):
        self.ID_icon_hub = texture.load_texture("hdd")