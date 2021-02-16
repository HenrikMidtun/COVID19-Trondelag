from controller import TrondelagController, HelsedirController

class COVIDTerminal:
    def __init__(self):
        self.controller = HelsedirController()
        print(self.controller.model.data)

covid = COVIDTerminal()