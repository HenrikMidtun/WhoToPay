from utils.HomebrewUtils import Stack, WeightedGraph, Graph
import random

def remove_cycles(G: WeightedGraph):
    
    #Run other path reduction algorithm first
    #DFS to find and eliminate cycles

    vertices = list(G.keys())
    visited = {}

    for root in vertices:

        stack = Stack()
        stack.push(root)
        while stack.count != 0:
            current_vertex = stack.peek()
            children = G.get(current_vertex)
            if current_vertex in vertices:
                vertices.remove(current_vertex)
            if current_vertex not in visited:
                visited[current_vertex] = []
            if children != None and children != {}:
                child_keys = list(children.keys())
                for child in child_keys:
                    if child not in visited.get(current_vertex):
                        
                        if stack.contains(child): #Found cycle -> Remove Cycle
                            child_stack_index = stack.spill().index(child)
                            cycle_members = stack.spill()[:child_stack_index+1]
                            small_edge = float('inf')
                            for k,v in enumerate(cycle_members):
                                inspected_edge = G.get(v).get(cycle_members[k-1])
                                if  inspected_edge < small_edge:
                                    small_edge = inspected_edge
                            for k,v in enumerate(cycle_members):
                                new_weight = G.get(v)[cycle_members[k-1]] - small_edge
                                G.add_edge(v, cycle_members[k-1], new_weight, True)
                                
                                if G.get(v)[cycle_members[k-1]] == 0:
                                    G.get(v).pop(cycle_members[k-1])
                            stack.clear()
                            stack.push(child)
                            visited = {}
                        else:
                            visited.get(current_vertex).append(child)
                            stack.push(child)
                        break
                    if child == child_keys[-1]:
                        stack.pop()
            else:
                stack.pop()
