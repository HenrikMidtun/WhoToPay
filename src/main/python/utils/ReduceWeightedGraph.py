from utils.HomebrewUtils import WeightedGraph
from utils.WeightedRedirect import redirect
from utils.FindRemoveCycleWeighted import remove_cycles

def reduce(G: WeightedGraph):
    #print('Reducing Graph, Original Graph:\n' + str(G))
    #print('Removed Cycles, Resulting Graph:\n' + str(G))
    remove_cycles(G)
    #print('Redirected Edges, Final Graph:\n' + str(G))
    redirect(G)

