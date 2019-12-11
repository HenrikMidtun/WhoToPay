import collections
from itertools import combinations

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args,**kwargs)
        return cls._instances[cls]

class Graph:    
    DEFAULT_LIST = {
        0: [False,1,2],
        1: [False,3],
        2: [False,5],
        3: [False,4],
        4: [False,1],
        5: [False,6],
        6: [False,2,5]
       }
    
    def __init__(self, adj_list = None):
        self.adj_list = adj_list if adj_list is not None else self.DEFAULT_LIST

    def get_children(self, number):
        if number in self.adj_list:
            return self.adj_list[number]
        return [True]
    
    def set_discovered(self,number):
        self.adj_list[number][0] = True

class WeightedGraph:

    def fill_test(self):
        self.add_edge(0,1,3,True)
        self.add_edge(0,0,2,True)
        
    def __init__(self):
        self.graph = collections.defaultdict(dict)
    
    def add_edge(self, u, v, weight, directed = False):
        self.graph[u][v] = weight
        if not directed:
            self.graph[v][u] = weight
        if v not in self.graph:
            self.graph[v] == {}
    
    def remove_node(self, u):
        if u in self.graph:
            self.graph.pop(u)

            associated_nodes = []
            for node in self.graph:
                for edge in self.graph.get(node):
                    if edge == u:
                        associated_nodes.append(node)
                        break
            for node in associated_nodes:
                self.graph.get(node).pop(u)
        
    def get(self, foo):
        return self.graph.get(foo)

    def get_weight(self, u, v):
        return self.graph.get(u)[v]

    def keys(self):
        return self.graph.keys()
    def __str__(self):
        rs = ''
        for vertex in self.graph:
            rs += str(vertex) + ':    '
            for edge in self.graph[vertex]:
                ss = '({:>2},{:>3})'.format(edge,self.graph[vertex][edge])
                ss += '    '
                rs += ss
            rs += '\n'
        return rs

class Stack:

    head = None
    count = 0

    def empty(self):
        return self.head == None
    
    def push(self, item):
        old_head = self.head
        self.head = self.Node(item)
        self.head.next = old_head
        self.count+=1

    def pop(self):
        old_head = self.head
        self.head = old_head.next
        self.count-=1
        return old_head.item

    def peek(self):
        if(self.head != None):
            return self.head.item
        return None

    def contains(self, item):
        node = self.head
        if node.item == item: return True
        while node.next != None:
            if node.next.item == item: return True
            node = node.next
        return False
    
    def spill(self, stop = None):
        if stop == None:
            stop = self.count
        rlist = []
        node = self.head
        for i in range(stop):
            rlist.append(node.item)
            node = node.next
        return rlist
    
    def clear(self):
        self.head = None
        self.count = 0
    
    class Node:
        next = None
        item = None
        def __init__(self, item):
            self.item = item
    
    def __str__(self):
        if self.head == None: return "Empty stack >:("
        rstr = "" + str(self.head.item)
        node = self.head  
        while node.next != None:
            rstr += "->" + str(node.next.item)
            node = node.next   
        return rstr

def children_combination_with_sum_k(children: {}, sum_k: int, r: int = 3):
    children_keys = list(children.keys())
    r_list = []
    for i in range(1,r+1):
        combs = combinations(children_keys,i)
        for comb in combs:
            temp_list = [children.get(x) for x in comb]
            if sum(temp_list) == sum_k:
                return list(comb) #Because we only need a single combination
                r_list.append(list(comb)) #shhh...
    return(r_list)


#Must fix, use combinations from itertools instead
def k_combinations(arr:[], k:int):
    r_list = []
    for i in range(len(arr)):
        if len(arr) - i < k:
            break
        temp_list = [arr[i]]
        if len(temp_list) != k:
            for y in range(i+1,len(arr)):
                temp_list.append(arr[y])
                if(len(temp_list) == k):
                    r_list.append(temp_list)
                    temp_list = [arr[i]]
        else:
            r_list.append(temp_list)               
    return r_list
 
if __name__ == "__main__":
    pass
    