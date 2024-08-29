from color import Color


# NON-ORIENTED GRAPH IMPLEMENTED BY MATRIX
class Graph:
    def __init__(self):
        self.nodes  = []       # List to hold nodes
        self.matrix = []       # Adjacency Matrix
        self.node_colors = {}  # Dictionary to track colors of nodes

    def Init(self):
        for node in self.node_colors:
            self.node_colors[node] = Color.WHITE

    def _resize_matrix(self, new_size):
        old_size  = len(self.matrix)
        curr_size = new_size - old_size

        # Expand existing rows
        for row in self.matrix:
            row.extend([0] * curr_size)

        # Add new rows
        for _ in range(curr_size):
            self.matrix.append([0] * new_size)

    def addNode(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
            self._resize_matrix(len(self.nodes))
            self.node_colors[node] = Color.WHITE

    def addEdge(self, node1, node2):
        if node1 not in self.nodes:
            self.addNode(node1)
        if node2 not in self.nodes:
            self.addNode(node2)

        index1 = self.nodes.index(node1)
        index2 = self.nodes.index(node2)
        self.matrix[index1][index2] = 1
        self.matrix[index2][index1] = 1

    def show(self):
        col_width = max(len(str(node)) for node in self.nodes) + 2

        print(" " * (col_width + 1) + "|", end="")
        for node in self.nodes:
            print(f" {str(node):<{col_width}}", end="")
        print()

        print(" " * (col_width + 1) + "+" + "-" * ((col_width + 1) * len(self.nodes)))
        for i, row in enumerate(self.matrix):
            print(f"{str(self.nodes[i]):<{col_width}} |", end="")
            for val in row:
                print(f" {val:<{col_width}}", end="")
            print()

    def DfsVisit(self, node, map_func=None, fold_func=None, acc=None):
        if map_func is not None:
            map_func(node)  # APPLY MAP

        if fold_func is not None:
            fold_func(acc, node)  # APPLY FOLD

        self.node_colors[node] = Color.GRAY

        index = self.nodes.index(node)
        for i, connected in enumerate(self.matrix[index]):
            if connected and self.node_colors[self.nodes[i]] == Color.WHITE:
                acc = self.DfsVisit(self.nodes[i], map_func, fold_func, acc)

        self.node_colors[node] = Color.BLACK
        return acc

    # DFS WITH BOTH MAP AND FOLD
    def Dfs(self, map_func=None, fold_func=None, acc=None):
        self.Init()
        for node in self.nodes:
            if self.node_colors[node] == Color.WHITE:
                acc = self.DfsVisit(node, map_func, fold_func, acc)

        return acc

    # BFS WITH BOTH MAP AND FOLD
    def Bfs(self, start_node, map_func=None, fold_func=None, acc=None):
        if start_node not in self.nodes:
            return acc

        self.Init()
        queue = [start_node]
        self.node_colors[start_node] = Color.GRAY

        while queue:
            curr = queue.pop(0)
            if map_func is not None:
                map_func(curr)  # APPLY MAP

            if fold_func is not None:
                acc = fold_func(acc, curr)  # APPLY FOLD

            index = self.nodes.index(curr)
            for i, connected in enumerate(self.matrix[index]):
                if connected and self.node_colors[self.nodes[i]] == Color.WHITE:
                    queue.append(self.nodes[i])
                    self.node_colors[self.nodes[i]] = Color.GRAY

            self.node_colors[curr] = Color.BLACK
        return acc