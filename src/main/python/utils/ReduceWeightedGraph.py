from utils.HomebrewUtils import WeightedGraph
from utils.WeightedRedirect import redirect
from utils.FindRemoveCycleWeighted import remove_cycles

def reduce(G: WeightedGraph):
    remove_cycles(G)
    redirect(G)

