#---------------------------------------------
from src.param import param_control
from src.base import node
from src.gui.style import colorization
from src.gui.background import gui_ID
from src.gui.style import gui_color
from src.utils import parser_json
import dearpygui.dearpygui as dpg


class Network_node(node.Node):
    # Build function
    def build(self):
        self.ID.init_ID_icon()
        with dpg.node(label=self.ID.name, tag=self.ID.ID_node):
            self.build_table_kpi()
            self.build_table_database()
        self.position_node()
        self.colorize_node()
    def position_node(self):
        pose = parser_json.get_pos_from_json()
        dpg.set_item_pos(self.ID.ID_node, pose["edge"]["network"])
    def colorize_node(self):
        colorization.colorize_node(self.ID.ID_node, "network")

    # Table functions
    def build_table_kpi(self):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            # Icone & status button
            with dpg.table(header_row=False, borders_innerH=False, width=350):
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()
                with dpg.table_row():
                    dpg.add_image(self.ID.ID_icon_network, width=20, height=15)
                    dpg.add_text("Ground <-> Edge");
                    dpg.add_button(tag=self.ID.ID_status_light, width=15)

            # Table kpi
            with dpg.table(header_row=True, borders_innerH=True, width=350):
                dpg.add_table_column()
                dpg.add_table_column(label="Upload")
                dpg.add_table_column(label="Download")
                dpg.add_table_column(label="Required")
                # Throughput
                with dpg.table_row():
                    dpg.add_text("Throughput")
                    with dpg.group(horizontal=True):
                        dpg.add_text(0, tag=self.ID.ID_perf_throughput_up, color=gui_color.color_info);
                        dpg.add_text("Mb/s");
                # Latency
                with dpg.table_row():
                    dpg.add_text("Latency")
                    with dpg.group(horizontal=True):
                        dpg.add_text(0, tag=self.ID.ID_perf_latency_up, color=gui_color.color_info);
                        dpg.add_text("ms");
                    with dpg.group(horizontal=True):
                        dpg.add_text(0, tag=self.ID.ID_perf_latency_down, color=gui_color.color_info);
                        dpg.add_text("ms");
                    dpg.add_text("< 200 ms");
                # Reliability
                with dpg.table_row():
                    dpg.add_text("Reliability")
                    with dpg.group(horizontal=True):
                        dpg.add_text(0, tag=self.ID.ID_perf_reliability_up, color=gui_color.color_info);
                        dpg.add_text("%");
                    with dpg.group(horizontal=True):
                        dpg.add_text(0, tag=self.ID.ID_perf_reliability_down, color=gui_color.color_info);
                        dpg.add_text("%");
                    dpg.add_text(">= 99 %");

            with dpg.table(header_row=True, borders_innerH=True, width=350):
                dpg.add_table_column()
                dpg.add_table_column(label="Time")
                dpg.add_table_column(label="Required")
                # Interruption
                with dpg.table_row():
                    dpg.add_text("Interruption")
                    with dpg.group(horizontal=True):
                        dpg.add_text(0, tag=self.ID.ID_perf_time_interruption, color=gui_color.color_info);
                        dpg.add_text("s [max]");
                    dpg.add_text("< 1 s");
                # Time
                with dpg.table_row():
                    dpg.add_text("End-to-end")
                    with dpg.group(horizontal=True):
                        dpg.add_text(0, tag=self.ID.ID_perf_time_processing, color=gui_color.color_info);
                        dpg.add_text("ms")
                    dpg.add_text("[1.6, 2] s");
    def build_table_database(self):
        with dpg.node_attribute(attribute_type=dpg.mvNode_Attr_Static):
            with dpg.table(header_row=False, borders_innerH=False, width=350):
                dpg.add_table_column()
                dpg.add_table_column()
                dpg.add_table_column()
                with dpg.table_row():
                    dpg.add_image(self.ID.ID_icon_database, width=15, height=15)
                    dpg.add_text("MongoDB");
                    dpg.add_button(tag=self.ID.ID_mongo_status_light, width=15)

    # Update function
    def update(self):
        colorization.colorize_status_light(self.ID.ID_status_light, param_control.state_edge["interface"]["capture"]["http_connected"])
        colorization.colorize_status_light(self.ID.ID_mongo_status_light, param_control.state_network["mongodb"]["connected"])
        self.update_perf()
    def update_perf(self):
        lidar_main = param_control.state_edge["hub"]["socket"]["lidar_main"]
        if(param_control.state_edge["interface"]["capture"]["http_connected"]):
            throughput_up = "%.2f"% param_control.state_network["ground_to_edge"]["throughput"]["value"]
            latency_up = "%.2f"% param_control.state_network["ground_to_edge"]["latency"]["value"]
            latency_down = "%.2f"% param_control.state_network["edge_to_ground"]["latency"]["value"]
            reliability_up = "%.2f"% param_control.state_network["ground_to_edge"]["reliability"]["value"]
            reliability_down = "%.2f"% param_control.state_network["edge_to_ground"]["reliability"]["value"]
            time_interruption = "%.2f"% param_control.state_network["ground_to_edge"]["interruption"]["max"]
            time_processing = "%.2f"% param_control.state_network["time"]["total"]
        else:
            throughput_up = 0
            latency_up = 0
            latency_down = 0
            reliability_up = 0
            reliability_down = 0
            time_interruption = 0
            time_processing = 0

        dpg.set_value(self.ID.ID_perf_throughput_up, throughput_up)
        dpg.set_value(self.ID.ID_perf_latency_up, latency_up)
        dpg.set_value(self.ID.ID_perf_latency_down, latency_down)
        dpg.set_value(self.ID.ID_perf_reliability_up, reliability_up)
        dpg.set_value(self.ID.ID_perf_reliability_down, reliability_down)
        dpg.set_value(self.ID.ID_perf_time_interruption, time_interruption)
        dpg.set_value(self.ID.ID_perf_time_processing, time_processing)
