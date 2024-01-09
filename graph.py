from color import Color
from queue import Queue

# IMPLEMENTATION BY ADJACENCY LIST

class Graph:
    def __init__(self, oriented=False):
        self.graph       = {} # Dictionary
        self.node_colors = {} # Dictionary
        self.oriented   = oriented

    def Init(self):
        for node in self.graph:
            self.node_colors[node] = Color.WHITE

    def addNode(self, nodo):
        if nodo not in self.graph:
            self.graph[nodo] = []

    def addEdge(self, nodo1, nodo2, oriented=None):
        if oriented is None:
            oriented = self.oriented

        if nodo1 in self.graph:
            self.graph[nodo1].append(nodo2)
        else:
            self.graph[nodo1] = [nodo2]

        if not oriented:
            if nodo2 in self.graph:
                self.graph[nodo2].append(nodo1)
            else:
                self.graph[nodo2] = [nodo1]

    def showStructure(self):
        for node, edges in self.graph.items():
            print(f"{node}: {edges}")

    # Dfs
    def DfsVisit(self, node, func=None):
        if func is not None:
            func(node)
        self.node_colors[node] = Color.GRAY

        for neighbor in self.graph[node]:
            if self.node_colors[neighbor] == Color.WHITE:
                self.DfsVisit(neighbor, func)

        self.node_colors[node] = Color.BLACK

    def DfsVisitTestGraphCyclic(self, node):
        self.node_colors[node] = Color.GRAY

        for neighbor in self.graph[node]:
            if self.node_colors[neighbor] == Color.WHITE:
                ret = self.DfsVisitTestGraphCyclic(neighbor)
                if ret == True:
                    return True
            elif self.node_colors[neighbor] == Color.GRAY:
                return True

        self.node_colors[node] = Color.BLACK
        return False

    def Dfs(self, func=None):
        self.Init()
        for node in self.graph:
            if self.node_colors[node] == Color.WHITE:
                self.DfsVisit(node, func)

    def DfsFromVertex(self, start_node, func=None):
        if start_node not in self.graph:
            return

        self.Init()
        self.DfsVisit(start_node, func)

    def isGraphAcyclic(self):
        self.Init()
        for node in self.graph:
            if self.node_colors[node] == Color.WHITE:
                ret = self.DfsVisitTestGraphCyclic(node) # Returns True if Graph is cyclic
                if ret == True:
                    return False
        
        return True

    # Bfs
    def Bfs(self, start_node, func=None):
        if start_node not in self.graph:
            return
        
        self.Init()

        queue = Queue()
        queue.put(start_node)
        self.node_colors[start_node] = Color.GRAY

        while not queue.empty():
            curr = queue.get()
            if func is not None:
                func(curr)
            
            for neighbor in self.graph[curr]:
                if self.node_colors[neighbor] == Color.WHITE:
                    queue.put(neighbor)
                    self.node_colors[neighbor] = Color.GRAY

            self.node_colors[curr] = Color.BLACK

# TODO: Add encapsulation (everything is public for now)
# TODO: Add Fold()
# TODO: In order:
    # Minimum Paths
    # Topological Sort
    # SCC
    # Graphics