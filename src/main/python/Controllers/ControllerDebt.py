from utils.ReduceWeightedGraph import reduce
from utils.HomebrewUtils import WeightedGraph, Singleton

class _ControllerDebt(metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.graph = WeightedGraph()

    def addDebt(self, u1, u2, debt: float):
        self.graph.add_edge(u1, u2, debt, True)
        print('debt from ',u1,' to ',u2,' = ',debt)

    def getDebt(self, id):
        return self.graph.get(id)

    def allocateDebt(self):
        reduce(self.graph)

    def removeUser(self, id):
        self.graph.remove_node(id)

Debt_Controller = _ControllerDebt()
