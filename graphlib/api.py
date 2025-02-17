from .graph import Graph


class UndirectedGraph:
    def __init__(self):
        self.__graph = Graph()

    def init(self):
        self.__graph.Init()

    def addNode(self, node):
        self.__graph.addNode(node)

    def removeNode(self, node):
        self.__graph.removeNode(node)

    def addEdge(self, node1, node2, weight):
        self.__graph.addEdge(node1, node2, weight)

    def size(self):
        return self.__graph.size()

    def empty(self):
        return self.__graph.empty()

    def getNodes(self):
        return self.__graph.getNodes()

    def getNodeColor(self, node):
        return self.__graph.getNodeColor(node)

    def dfs(self, start_node=None, map_func=None, fold_func=None, acc=None):
        return self.__graph.Dfs(start_node=start_node, map_func=map_func, fold_func=fold_func, acc=acc)

    def bfs(self, start_node, map_func=None, fold_func=None, acc=None):
        return self.__graph.Bfs(start_node, map_func=map_func, fold_func=fold_func, acc=acc)

    # GET MINIMUM PATH WITHOUT CONSIDERING WEIGTHS
    def getMinimumPath(self, start_node, end_node):
        return self.__graph.getMinimumPath(start_node, end_node)

    def getSCCs(self):
        return self.__graph.getSCCs()

    def dijkstra(self, start_node, end_node):
        return self.__graph.dijkstra(start_node, end_node)

    def show(self):
        self.__graph.showVisualization()