from color import Color


# NON-ORIENTED GRAPH IMPLEMENTED BY MATRIX
class Graph:
    def __init__(self):
        self.__nodes  = []       # List to hold nodes
        self.__matrix = []       # Adjacency Matrix
        self.__node_colors = {}  # Dictionary to track colors of nodes

    def Init(self):
        for node in self.__node_colors:
            self.__node_colors[node] = Color.WHITE

    def __resize_matrix(self, new_size):
        old_size  = len(self.__matrix)
        curr_size = new_size - old_size

        # Expand existing rows
        for row in self.__matrix:
            row.extend([0] * curr_size)

        # Add new rows
        for _ in range(curr_size):
            self.__matrix.append([0] * new_size)

    def addNode(self, node):
        if node not in self.__nodes:
            self.__nodes.append(node)
            self.__resize_matrix(len(self.__nodes))
            self.__node_colors[node] = Color.WHITE

    def addEdge(self, node1, node2):
        if node1 not in self.__nodes:
            self.addNode(node1)
        if node2 not in self.__nodes:
            self.addNode(node2)

        index1 = self.__nodes.index(node1)
        index2 = self.__nodes.index(node2)
        self.__matrix[index1][index2] = 1
        self.__matrix[index2][index1] = 1

    def show(self):
        col_width = max(len(str(node)) for node in self.__nodes) + 2

        print(" " * (col_width + 1) + "|", end="")
        for node in self.__nodes:
            print(f" {str(node):<{col_width}}", end="")
        print()

        print(" " * (col_width + 1) + "+" + "-" * ((col_width + 1) * len(self.__nodes)))
        for i, row in enumerate(self.__matrix):
            print(f"{str(self.__nodes[i]):<{col_width}} |", end="")
            for val in row:
                print(f" {val:<{col_width}}", end="")
            print()

    def __DfsVisit(self, node, map_func=None, fold_func=None, acc=None):
        if map_func is not None:
            map_func(node)

        if fold_func is not None:
            acc = fold_func(acc, node)

        self.__node_colors[node] = Color.GRAY

        index = self.__nodes.index(node)
        for i, connected in enumerate(self.__matrix[index]):
            if connected and self.__node_colors[self.__nodes[i]] == Color.WHITE:
                acc = self.__DfsVisit(self.__nodes[i], map_func, fold_func, acc)

        self.__node_colors[node] = Color.BLACK
        return acc

    # DFS WITH BOTH MAP AND FOLD
    def Dfs(self, map_func=None, fold_func=None, acc=None):
        self.Init()
        for node in self.__nodes:
            if self.__node_colors[node] == Color.WHITE:
                acc = self.__DfsVisit(node, map_func, fold_func, acc)

        return acc

    # BFS WITH BOTH MAP AND FOLD
    def Bfs(self, start_node, map_func=None, fold_func=None, acc=None):
        if start_node not in self.__nodes:
            return acc

        self.Init()
        queue = [start_node]
        self.__node_colors[start_node] = Color.GRAY

        while queue:
            curr = queue.pop(0)
            if map_func is not None:
                map_func(curr)

            if fold_func is not None:
                acc = fold_func(acc, curr)

            index = self.__nodes.index(curr)
            for i, connected in enumerate(self.__matrix[index]):
                if connected and self.__node_colors[self.__nodes[i]] == Color.WHITE:
                    queue.append(self.__nodes[i])
                    self.__node_colors[self.__nodes[i]] = Color.GRAY

            self.__node_colors[curr] = Color.BLACK
        return acc