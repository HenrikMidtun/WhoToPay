from utils.HomebrewUtils import WeightedGraph, children_combination_with_sum_k
from utils.FindRemoveCycleWeighted import remove_cycles

'''
    If two subsequent edges are of the same weight, then the first one will be made parent to the last
    This allows us to remove the intermediate (second) edge.

    Use BFS because,
        If the sum of some set of childrens edges == Some parent edge
            -Distribute parent edge among children
        We need to find an efficient algorithm to compute ANY combination of children weights that equal ANY parent weight
        
'''
def redirect(G: WeightedGraph):

    vertices = list(G.keys())
    layer = []
    nodes_visited = []
    parent_vertices = {}

    for vertex in vertices:
        if vertex not in nodes_visited:
            layer.append(vertex)
            nodes_visited.append(vertex)
            parent_vertices[layer[0]] = {}

            while len(layer) > 0:
                #Do something with the first node in the layer, set discovered, change value etc.
                children = G.get(layer[0])
                parents = parent_vertices[layer[0]]

                if children != None:
                    #Search for appropriate combination of child nodes
                    for parent in parents:
                        parent_weight = parents.get(parent)
                        children_comb = children_combination_with_sum_k(children,parent_weight)
                        if len(children_comb) != 0:
                            for child in children_comb:
                                child_weight = G.get(layer[0]).get(child)
                                previous_edge_weight = G.get(parent).get(child)
                                if previous_edge_weight == None:
                                    G.add_edge(parent,child,child_weight,True)
                                else:
                                    G.add_edge(parent,child,child_weight + previous_edge_weight, True)
                                G.get(layer[0]).pop(child)
                            G.get(parent).pop(layer[0])

                    #Adding to stack and updating parents
                    for node in children:
                        
                        if node in parent_vertices:
                            parent_vertices[node][layer[0]] = G.get_weight(layer[0],node)
                        else:
                            parent_vertices[node] = {}
                            parent_vertices[node][layer[0]] = G.get_weight(layer[0],node)

                        if node not in nodes_visited:
                            layer.append(node)
                            nodes_visited.append(node)

                layer.remove(layer[0])
            
