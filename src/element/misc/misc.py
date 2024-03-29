#---------------------------------------------
from src.element.misc.wallet import wallet
from src.element.misc.block import block


class Misc:
    def __init__(self, ID):
        self.ID = "misc_" + str(ID)
        self.wallet = wallet.Wallet()
        self.block = block.Block()

    # Window
    def build_windows(self):
        self.wallet.window.build()
    def update_windows(self):
        self.wallet.window.update()

    # Node
    def build_nodes(self):
        self.block.design_blocks()

    # Event
    def setup_handlers(self):
        pass
    def set_invisible_all(self):
        self.wallet.window.set_invisible()
