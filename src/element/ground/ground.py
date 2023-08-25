#---------------------------------------------
from src.element.ground.capture import capture
from src.element.ground.lidar import lidar
from src.element.ground import link
from src.utils import parser_json


class Ground:
    def __init__(self, ID):
        self.ID_ground = "ground_" + str(ID)
        self.capture = capture.Capture()
        self.lidar_1 = lidar.Lidar(1)
        self.lidar_2 = lidar.Lidar(2)
        self.link = link.Link(self)
        self.state = parser_json.load_state("src/element/ground/state.json")

    def build_nodes(self):
        self.capture.node.build()
        self.lidar_1.node.build()
        self.lidar_2.node.build()

    def build_windows(self):
        self.capture.window.build()
        self.lidar_1.window.build()
        self.lidar_2.window.build()

    def setup_handlers(self):
        self.capture.setup_handler()
        self.lidar_1.setup_handler()
        self.lidar_2.setup_handler()